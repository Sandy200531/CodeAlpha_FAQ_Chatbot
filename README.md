# 🤖 FAQ Chatbot — CodeAlpha AI Internship Task 2

An intelligent FAQ chatbot built with **NLTK**, **TF-IDF Vectorization**, and **Cosine Similarity**, featuring a modern dark-themed **Streamlit** UI.

---

## 📌 Project Overview

This chatbot answers frequently asked questions about AI/ML, Python, Data Science, and CodeAlpha internships. Instead of using hardcoded keyword matching, it uses **NLP-powered semantic similarity** to find the best matching answer from an FAQ database — even when the user's phrasing differs from the stored questions.

---

## 🏗️ Project Architecture

```
User Input
    │
    ▼
┌─────────────────────────────────┐
│        Text Preprocessing       │  ← Lowercase, remove special chars,
│  (NLTK: tokenize, stopword      │    tokenize, remove stopwords,
│   removal, lemmatization)       │    lemmatize
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│       TF-IDF Vectorization      │  ← Convert text to numerical vectors
│       (sklearn TfidfVectorizer) │    using Term Frequency–Inverse
│                                 │    Document Frequency
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│       Cosine Similarity         │  ← Compare user vector to all FAQ
│  (sklearn cosine_similarity)    │    vectors, find best match
└──────────────┬──────────────────┘
               │
               ▼
┌─────────────────────────────────┐
│      Confidence Thresholding    │  ← Only return answer if score ≥ 0.15
│      + Answer Retrieval         │    Otherwise return fallback message
└──────────────┬──────────────────┘
               │
               ▼
       Streamlit Chat UI
```

---

## 📁 Folder Structure

```
faq_chatbot/
│
├── app.py               ← Main Streamlit application (UI + logic wiring)
├── chatbot_engine.py    ← Core FAQ matching engine (TF-IDF + Cosine Similarity)
├── faq_data.py          ← FAQ dataset (23 Q&A pairs across 5 topics)
├── requirements.txt     ← Python dependencies
└── README.md            ← This file
```

---

## 🛠️ Tech Stack

| Component       | Technology                      |
|----------------|---------------------------------|
| Language        | Python 3.10+                    |
| UI Framework    | Streamlit                       |
| NLP Library     | NLTK                            |
| ML Library      | Scikit-learn                    |
| Vectorization   | TF-IDF (TfidfVectorizer)        |
| Similarity      | Cosine Similarity               |
| Text Processing | Tokenization, Lemmatization     |

---

## 🚀 Installation Guide

### Step 1: Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_FAQChatbot.git
cd CodeAlpha_FAQChatbot
```

### Step 2: Create a virtual environment (recommended)
```bash
python -m venv env

# Windows
env\Scripts\activate

# Mac/Linux
source env/bin/activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the app
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

---

## 🎮 How to Use

1. **Type your question** in the input box at the bottom
2. **Press Enter or click Send** to get an answer
3. **Click suggested questions** for quick access
4. **View the confidence score** — Green (High), Yellow (Medium), Red (Low)
5. **See the matched FAQ question** below each answer
6. **Clear chat** anytime using the sidebar button

---

## 🧠 How It Works

### 1. TF-IDF (Term Frequency–Inverse Document Frequency)
- Converts text into a numerical matrix
- Gives higher weight to words that are important in a specific question but rare across all questions
- Bi-gram support (1–2 word combinations) for better matching

### 2. Cosine Similarity
- Measures the angle between two text vectors
- Score of 1.0 = identical meaning, 0.0 = completely unrelated
- Threshold of 0.15 is used to filter out low-confidence answers

### 3. NLTK Preprocessing
- **Tokenization** — splits text into individual words
- **Stopword removal** — removes filler words like "the", "is", "at"
- **Lemmatization** — reduces words to base form ("running" → "run")

---

## 📸 Screenshots to Capture

| Screenshot | Description |
|---|---|
| `screenshot_1_home.png` | App homepage with chat bubbles |
| `screenshot_2_answer.png` | High-confidence answer with green badge |
| `screenshot_3_suggestion.png` | Clicking a suggested question |
| `screenshot_4_low_conf.png` | Low-confidence fallback message |
| `screenshot_5_sidebar.png` | Sidebar with session stats |

---

## 📤 GitHub Upload Instructions

```bash
# Initialize repo
git init

# Add all files
git add .

# Commit
git commit -m "Add FAQ Chatbot - CodeAlpha AI Internship Task 2"

# Create repo on GitHub named: CodeAlpha_FAQChatbot
# Then push:
git remote add origin https://github.com/YOUR_USERNAME/CodeAlpha_FAQChatbot.git
git branch -M main
git push -u origin main
```

---

## 📝 LinkedIn Post Template

> 🤖 **Project 1 of 3 — FAQ Chatbot | CodeAlpha AI Internship**
>
> Built an intelligent FAQ Chatbot using **NLP + TF-IDF + Cosine Similarity** with a modern Streamlit UI!
>
> 🔹 NLTK for text preprocessing (tokenization, lemmatization)
> 🔹 TF-IDF vectorization for semantic text representation
> 🔹 Cosine similarity for finding the best FAQ match
> 🔹 Confidence score display with color-coded feedback
> 🔹 Dark-themed, interactive Streamlit chat UI
>
> 📂 GitHub: [link]
> 🎥 Demo: [video link]
>
> @CodeAlpha #AI #NLP #Python #MachineLearning #Internship #Streamlit

---

## 💼 Resume Bullet Points

- Developed an NLP-powered FAQ Chatbot using NLTK, TF-IDF vectorization, and cosine similarity achieving semantic question matching across 23+ FAQ entries
- Built an interactive Streamlit chat UI with confidence score display, session analytics, and dark-themed design for CodeAlpha AI Internship

---

## 🤝 Author

**Dola Sangeetha**  
B.Tech CSE (AI & ML) | St. Martin's Engineering College  
CodeAlpha AI Internship — June 2026
