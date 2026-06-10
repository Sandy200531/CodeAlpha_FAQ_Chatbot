# =============================================================================
# chatbot_engine.py — Core Chatbot Logic
# =============================================================================
# This module contains the FAQ matching engine using:
#   • TF-IDF Vectorization  — converts text into numerical vectors
#   • Cosine Similarity     — measures how similar two text vectors are
#   • NLTK preprocessing    — tokenizes and cleans user input
#
# How it works:
#   1. All FAQ questions are vectorized at startup using TF-IDF.
#   2. When a user asks something, their question is also vectorized.
#   3. Cosine similarity is computed between the user's question and all FAQs.
#   4. The FAQ with the highest similarity score is returned as the answer.
# =============================================================================

import re
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from faq_data import FAQ_DATA

# ── Download required NLTK resources ────────────────────────────────────────
# These are downloaded once and cached locally.
nltk.download("punkt",      quiet=True)
nltk.download("stopwords",  quiet=True)
nltk.download("wordnet",    quiet=True)
nltk.download("punkt_tab",  quiet=True)

from nltk.corpus   import stopwords
from nltk.stem     import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# ── Constants ────────────────────────────────────────────────────────────────
CONFIDENCE_THRESHOLD = 0.15   # Minimum similarity score to return an answer
STOP_WORDS = set(stopwords.words("english"))
LEMMATIZER = WordNetLemmatizer()


def preprocess_text(text: str) -> str:
    """
    Clean and normalize input text.

    Steps:
        1. Lowercase the text
        2. Remove special characters and digits
        3. Tokenize into words
        4. Remove stop words (e.g., 'the', 'is', 'at')
        5. Lemmatize — reduce words to their base form (e.g., 'running' → 'run')

    Args:
        text (str): Raw input string.

    Returns:
        str: Cleaned and normalized string.
    """
    # Step 1: Lowercase
    text = text.lower()

    # Step 2: Remove special characters (keep only letters and spaces)
    text = re.sub(r"[^a-z\s]", "", text)

    # Step 3: Tokenize
    tokens = word_tokenize(text)

    # Step 4 & 5: Remove stopwords and lemmatize
    tokens = [
        LEMMATIZER.lemmatize(token)
        for token in tokens
        if token not in STOP_WORDS and len(token) > 1
    ]

    return " ".join(tokens)


class FAQChatbot:
    """
    FAQ Chatbot using TF-IDF and Cosine Similarity.

    Attributes:
        faqs       (list[dict]): List of FAQ dictionaries with 'question' and 'answer'.
        vectorizer (TfidfVectorizer): Fitted TF-IDF vectorizer.
        faq_matrix (sparse matrix): TF-IDF matrix for all FAQ questions.
    """

    def __init__(self, faq_data: list[dict]):
        """
        Initialize the chatbot by building the TF-IDF index.

        Args:
            faq_data (list[dict]): FAQ dataset from faq_data.py
        """
        self.faqs = faq_data

        # Preprocess all FAQ questions
        processed_questions = [preprocess_text(item["question"]) for item in self.faqs]

        # Build TF-IDF vectorizer and fit it on all FAQ questions
        # TF-IDF stands for Term Frequency–Inverse Document Frequency.
        # It weighs words by how often they appear in a question (TF)
        # relative to how common they are across all questions (IDF).
        self.vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),   # Use single words and 2-word phrases
            min_df=1,
            max_features=5000,
        )
        self.faq_matrix = self.vectorizer.fit_transform(processed_questions)

    def get_response(self, user_input: str) -> dict:
        """
        Find the best matching FAQ for the user's question.

        Args:
            user_input (str): The question typed by the user.

        Returns:
            dict: {
                "answer"      : str   — best answer or fallback message,
                "confidence"  : float — similarity score (0.0 – 1.0),
                "matched_question": str — the FAQ question that was matched,
                "found"       : bool  — True if confidence >= threshold
            }
        """
        if not user_input.strip():
            return {
                "answer": "Please type a question so I can help you!",
                "confidence": 0.0,
                "matched_question": "",
                "found": False,
            }

        # Preprocess the user's question
        processed_input = preprocess_text(user_input)

        if not processed_input.strip():
            return {
                "answer": "I couldn't understand your question. Please try rephrasing.",
                "confidence": 0.0,
                "matched_question": "",
                "found": False,
            }

        # Convert user question to TF-IDF vector
        user_vector = self.vectorizer.transform([processed_input])

        # Compute cosine similarity between user question and all FAQ questions
        # Cosine similarity returns values between 0 (no match) and 1 (perfect match)
        similarities = cosine_similarity(user_vector, self.faq_matrix).flatten()

        # Find the index of the highest similarity score
        best_idx   = int(np.argmax(similarities))
        best_score = float(similarities[best_idx])

        if best_score >= CONFIDENCE_THRESHOLD:
            return {
                "answer":           self.faqs[best_idx]["answer"],
                "confidence":       round(best_score, 4),
                "matched_question": self.faqs[best_idx]["question"],
                "found":            True,
            }
        else:
            return {
                "answer": (
                    "I'm not confident enough to answer that question. "
                    "Please try rephrasing, or ask about AI/ML, Python, data science, or CodeAlpha internships."
                ),
                "confidence":       round(best_score, 4),
                "matched_question": "",
                "found":            False,
            }

    def get_all_questions(self) -> list[str]:
        """Return all FAQ questions (for displaying suggestions)."""
        return [item["question"] for item in self.faqs]

    def get_topics(self) -> list[str]:
        """Return broad topic categories based on the FAQ data."""
        return [
            "🤖 Artificial Intelligence",
            "📊 Machine Learning & Deep Learning",
            "🐍 Python Programming",
            "📈 Data Science",
            "💼 Internship & Career",
        ]
