# =============================================================================
# faq_data.py — FAQ Dataset for the Chatbot
# =============================================================================
# This file contains the FAQ dataset used by the chatbot.
# You can extend this list with your own questions and answers.
# Each entry is a dictionary with "question" and "answer" keys.
# =============================================================================

FAQ_DATA = [
    # ── AI & Machine Learning ────────────────────────────────────────────────
    {
        "question": "What is Artificial Intelligence?",
        "answer": (
            "Artificial Intelligence (AI) is the simulation of human intelligence in machines "
            "that are programmed to think, learn, and solve problems. It includes subfields like "
            "Machine Learning, Deep Learning, Natural Language Processing, and Computer Vision."
        ),
    },
    {
        "question": "What is Machine Learning?",
        "answer": (
            "Machine Learning (ML) is a subset of AI that enables systems to learn from data "
            "and improve performance over time without being explicitly programmed. Common types "
            "include supervised, unsupervised, and reinforcement learning."
        ),
    },
    {
        "question": "What is Deep Learning?",
        "answer": (
            "Deep Learning is a subset of Machine Learning that uses neural networks with many "
            "layers (deep neural networks) to learn complex patterns from large datasets. It powers "
            "applications like image recognition, speech recognition, and language translation."
        ),
    },
    {
        "question": "What is Natural Language Processing?",
        "answer": (
            "Natural Language Processing (NLP) is a branch of AI that deals with the interaction "
            "between computers and human language. It enables machines to read, understand, and "
            "generate human language. Applications include chatbots, translation tools, and sentiment analysis."
        ),
    },
    {
        "question": "What is a neural network?",
        "answer": (
            "A neural network is a computing system inspired by the biological neural networks in "
            "the human brain. It consists of layers of interconnected nodes (neurons) that process "
            "and transmit information, enabling the system to learn from data."
        ),
    },
    {
        "question": "What is overfitting in machine learning?",
        "answer": (
            "Overfitting occurs when a model learns the training data too well, including its noise "
            "and outliers, resulting in poor performance on new, unseen data. It can be addressed "
            "using techniques like cross-validation, regularization, dropout, and using more training data."
        ),
    },
    {
        "question": "What is the difference between supervised and unsupervised learning?",
        "answer": (
            "Supervised learning uses labeled data where the model learns the mapping from inputs to "
            "outputs (e.g., classification, regression). Unsupervised learning uses unlabeled data "
            "and the model finds hidden patterns or structure on its own (e.g., clustering, dimensionality reduction)."
        ),
    },
    {
        "question": "What is TensorFlow?",
        "answer": (
            "TensorFlow is an open-source machine learning framework developed by Google. It provides "
            "tools to build and train machine learning and deep learning models. It supports Python and "
            "is widely used in research and production AI systems."
        ),
    },
    {
        "question": "What is a convolutional neural network?",
        "answer": (
            "A Convolutional Neural Network (CNN) is a type of deep learning model primarily used for "
            "image and video recognition tasks. It uses convolutional layers to automatically detect "
            "spatial features like edges, textures, and shapes from images."
        ),
    },
    {
        "question": "What is transfer learning?",
        "answer": (
            "Transfer learning is a technique where a pre-trained model (trained on a large dataset) "
            "is fine-tuned for a new, related task. It saves time and computational resources, and "
            "works well when you have limited training data."
        ),
    },
    # ── Python Programming ───────────────────────────────────────────────────
    {
        "question": "What is Python?",
        "answer": (
            "Python is a high-level, interpreted, general-purpose programming language known for its "
            "simplicity and readability. It is widely used in AI, data science, web development, and "
            "automation. Popular libraries include NumPy, Pandas, Scikit-learn, TensorFlow, and Flask."
        ),
    },
    {
        "question": "What is a Python virtual environment?",
        "answer": (
            "A Python virtual environment is an isolated environment that allows you to install packages "
            "specific to a project without affecting the global Python installation. You create one using "
            "`python -m venv env` and activate it with `env\\Scripts\\activate` (Windows) or `source env/bin/activate` (Mac/Linux)."
        ),
    },
    {
        "question": "What is Streamlit?",
        "answer": (
            "Streamlit is an open-source Python library that makes it easy to create and share beautiful "
            "web applications for machine learning and data science projects — all in pure Python, with no "
            "front-end experience required. You run a Streamlit app with `streamlit run app.py`."
        ),
    },
    {
        "question": "What is the difference between a list and a tuple in Python?",
        "answer": (
            "A list is mutable (can be changed after creation) and is defined with square brackets [ ]. "
            "A tuple is immutable (cannot be changed after creation) and is defined with parentheses ( ). "
            "Tuples are generally faster and used for fixed data."
        ),
    },
    {
        "question": "What are Python decorators?",
        "answer": (
            "A decorator in Python is a function that modifies or enhances another function without "
            "changing its source code. Decorators are applied using the @symbol above a function definition. "
            "Common examples include @staticmethod, @classmethod, and Flask's @app.route."
        ),
    },
    # ── Data Science ─────────────────────────────────────────────────────────
    {
        "question": "What is data preprocessing?",
        "answer": (
            "Data preprocessing is the process of cleaning and transforming raw data into a format suitable "
            "for machine learning models. It includes handling missing values, encoding categorical variables, "
            "feature scaling, and splitting data into training and testing sets."
        ),
    },
    {
        "question": "What is feature engineering?",
        "answer": (
            "Feature engineering is the process of using domain knowledge to select, modify, or create "
            "new input features from raw data to improve model performance. Good features can significantly "
            "boost the accuracy and efficiency of a machine learning model."
        ),
    },
    {
        "question": "What is a confusion matrix?",
        "answer": (
            "A confusion matrix is a table used to evaluate the performance of a classification model. "
            "It shows the number of true positives, true negatives, false positives, and false negatives. "
            "From it, you can derive metrics like accuracy, precision, recall, and F1-score."
        ),
    },
    {
        "question": "What is cross-validation?",
        "answer": (
            "Cross-validation is a technique to evaluate a model's performance by splitting the dataset "
            "into multiple folds. The model is trained on some folds and tested on the remaining fold, "
            "repeated multiple times. K-Fold cross-validation is the most common approach."
        ),
    },
    # ── Internship / Career ───────────────────────────────────────────────────
    {
        "question": "How do I prepare for an AI interview?",
        "answer": (
            "To prepare for an AI interview: (1) Revise ML fundamentals — algorithms, math, evaluation metrics. "
            "(2) Practice coding on LeetCode and HackerRank. (3) Build 2–3 strong projects with GitHub repos. "
            "(4) Study system design basics. (5) Be ready to explain your projects and the decisions you made."
        ),
    },
    {
        "question": "What skills are needed for an AI engineer?",
        "answer": (
            "Key skills for an AI engineer include: Python programming, Machine Learning algorithms, "
            "Deep Learning frameworks (TensorFlow, PyTorch), data preprocessing, NLP, Computer Vision, "
            "SQL/databases, REST API development, Git/GitHub, and strong problem-solving and math skills."
        ),
    },
    {
        "question": "What is CodeAlpha?",
        "answer": (
            "CodeAlpha is a leading software development company dedicated to driving innovation and excellence "
            "across emerging technologies. It offers internship programs in AI, Web Development, and other domains, "
            "providing students with hands-on real-world experience and completion certificates."
        ),
    },
    {
        "question": "How do I submit my CodeAlpha internship tasks?",
        "answer": (
            "To submit CodeAlpha tasks: (1) Upload source code to GitHub in a repo named CodeAlpha_ProjectName. "
            "(2) Post a LinkedIn video with the GitHub link, tagging @CodeAlpha. "
            "(3) Fill out the submission form shared in your WhatsApp group. Complete at least 2 out of 4 tasks."
        ),
    },
]
