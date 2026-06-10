# =============================================================================
# app.py — Main Streamlit Application — FAQ Chatbot
# =============================================================================
# Run this file with:  streamlit run app.py
#
# This is the main UI file. It uses Streamlit to build an interactive
# chatbot interface with:
#   • A dark, modern chat UI
#   • Persistent chat history across the session
#   • Confidence score display with color-coded badges
#   • Suggested questions for quick access
#   • A clear chat button
# =============================================================================

import streamlit as st
from chatbot_engine import FAQChatbot
from faq_data import FAQ_DATA

# ── Page Configuration ───────────────────────────────────────────────────────
# Must be the FIRST Streamlit command in the script
st.set_page_config(
    page_title="FAQ Chatbot | CodeAlpha",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS — Modern Dark Theme ───────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Global font & background ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* ── Main background ── */
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        min-height: 100vh;
    }

    /* ── Sidebar ── */
    [data-testid="stSidebar"] {
        background: rgba(255,255,255,0.05);
        backdrop-filter: blur(20px);
        border-right: 1px solid rgba(255,255,255,0.1);
    }

    /* ── Header banner ── */
    .header-banner {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 24px 32px;
        margin-bottom: 24px;
        text-align: center;
        box-shadow: 0 8px 32px rgba(102,126,234,0.3);
    }
    .header-banner h1 {
        color: #ffffff;
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
        letter-spacing: -0.5px;
    }
    .header-banner p {
        color: rgba(255,255,255,0.85);
        margin: 8px 0 0 0;
        font-size: 0.95rem;
    }

    /* ── Chat container ── */
    .chat-container {
        max-height: 520px;
        overflow-y: auto;
        padding: 8px 0;
        scrollbar-width: thin;
        scrollbar-color: #667eea transparent;
    }

    /* ── User message bubble ── */
    .user-bubble {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 16px;
    }
    .user-bubble .bubble {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: #fff;
        padding: 12px 18px;
        border-radius: 18px 18px 4px 18px;
        max-width: 70%;
        font-size: 0.92rem;
        line-height: 1.5;
        box-shadow: 0 4px 15px rgba(102,126,234,0.35);
    }

    /* ── Bot message bubble ── */
    .bot-bubble {
        display: flex;
        justify-content: flex-start;
        margin-bottom: 16px;
        gap: 12px;
    }
    .bot-avatar {
        width: 36px;
        height: 36px;
        background: linear-gradient(135deg, #f093fb, #f5576c);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 16px;
        flex-shrink: 0;
    }
    .bot-bubble .bubble {
        background: rgba(255,255,255,0.08);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.12);
        color: #e8e8f0;
        padding: 14px 18px;
        border-radius: 4px 18px 18px 18px;
        max-width: 70%;
        font-size: 0.92rem;
        line-height: 1.6;
    }

    /* ── Confidence badge ── */
    .confidence-badge {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 20px;
        font-size: 0.72rem;
        font-weight: 600;
        margin-top: 8px;
        letter-spacing: 0.5px;
    }
    .confidence-high   { background: rgba(52,211,153,0.2); color: #34d399; border: 1px solid rgba(52,211,153,0.3); }
    .confidence-medium { background: rgba(251,191, 36,0.2); color: #fbbf24; border: 1px solid rgba(251,191,36,0.3); }
    .confidence-low    { background: rgba(248,113,113,0.2); color: #f87171; border: 1px solid rgba(248,113,113,0.3); }

    /* ── Matched question ── */
    .matched-q {
        font-size: 0.75rem;
        color: rgba(255,255,255,0.45);
        margin-top: 4px;
        font-style: italic;
    }

    /* ── Input box override ── */
    .stTextInput > div > div > input {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 12px;
        color: #ffffff;
        padding: 14px 18px;
        font-size: 0.95rem;
    }
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 2px rgba(102,126,234,0.25);
    }
    .stTextInput > div > div > input::placeholder { color: rgba(255,255,255,0.35); }

    /* ── Buttons ── */
    .stButton > button {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 22px;
        font-weight: 600;
        font-size: 0.9rem;
        cursor: pointer;
        transition: opacity 0.2s ease;
        width: 100%;
    }
    .stButton > button:hover { opacity: 0.88; }

    /* ── Suggestion chip ── */
    .suggestion-chip {
        display: inline-block;
        background: rgba(102,126,234,0.15);
        border: 1px solid rgba(102,126,234,0.35);
        color: #a5b4fc;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 0.78rem;
        margin: 3px;
        cursor: pointer;
    }

    /* ── Stats card ── */
    .stats-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 12px;
        padding: 16px;
        text-align: center;
        color: #e8e8f0;
    }
    .stats-number { font-size: 1.8rem; font-weight: 700; color: #a5b4fc; }
    .stats-label  { font-size: 0.78rem; color: rgba(255,255,255,0.5); margin-top: 4px; }

    /* ── Section labels ── */
    .section-label {
        color: rgba(255,255,255,0.5);
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        margin-bottom: 8px;
    }

    /* ── Divider ── */
    hr { border-color: rgba(255,255,255,0.08); }

    /* ── Scrollbar ── */
    ::-webkit-scrollbar        { width: 5px; }
    ::-webkit-scrollbar-track  { background: transparent; }
    ::-webkit-scrollbar-thumb  { background: #667eea; border-radius: 4px; }
    </style>
    """,
    unsafe_allow_html=True,
)


# ── Session State Initialization ─────────────────────────────────────────────
# st.session_state persists data across Streamlit reruns (every interaction)

if "chatbot" not in st.session_state:
    # Initialize the chatbot engine (builds TF-IDF index)
    st.session_state.chatbot = FAQChatbot(FAQ_DATA)

if "messages" not in st.session_state:
    # Start with a welcome message from the bot
    st.session_state.messages = [
        {
            "role": "bot",
            "text": (
                "👋 Hello! I'm your AI FAQ Assistant, trained on topics like **AI/ML**, "
                "**Python**, **Data Science**, and **CodeAlpha internships**.\n\n"
                "Ask me anything, or click a suggested question below!"
            ),
            "confidence": 1.0,
            "matched_question": "",
            "found": True,
        }
    ]

if "total_queries" not in st.session_state:
    st.session_state.total_queries = 0

if "answered" not in st.session_state:
    st.session_state.answered = 0

if "prefill_question" not in st.session_state:
    st.session_state.prefill_question = ""


# ── Helper: render a confidence badge ───────────────────────────────────────
def confidence_badge(score: float, found: bool) -> str:
    """Return HTML for a color-coded confidence badge."""
    if not found:
        return '<span class="confidence-badge confidence-low">🔴 Low Confidence</span>'
    if score >= 0.6:
        css   = "confidence-high"
        label = "🟢 High Confidence"
    elif score >= 0.3:
        css   = "confidence-medium"
        label = "🟡 Medium Confidence"
    else:
        css   = "confidence-low"
        label = "🔴 Low Confidence"
    return f'<span class="confidence-badge {css}">{label} — {score:.0%}</span>'


# ── Helper: render chat history ──────────────────────────────────────────────
def render_chat():
    """Render all messages in the chat history."""
    html_parts = ['<div class="chat-container">']

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            html_parts.append(
                f'<div class="user-bubble">'
                f'  <div class="bubble">{msg["text"]}</div>'
                f'</div>'
            )
        else:
            badge   = confidence_badge(msg["confidence"], msg["found"])
            matched = ""
            if msg.get("matched_question"):
                matched = (
                    f'<div class="matched-q">📌 Matched: "{msg["matched_question"]}"</div>'
                )
            # Convert **text** markdown to <strong>
            answer_html = msg["text"].replace("**", "<strong>", 1)
            while "**" in answer_html:
                answer_html = answer_html.replace("**", "</strong>", 1)

            html_parts.append(
                f'<div class="bot-bubble">'
                f'  <div class="bot-avatar">🤖</div>'
                f'  <div>'
                f'    <div class="bubble">{answer_html}</div>'
                f'    {badge}'
                f'    {matched}'
                f'  </div>'
                f'</div>'
            )

    html_parts.append("</div>")
    st.markdown("".join(html_parts), unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        '<div class="section-label">📊 Session Stats</div>',
        unsafe_allow_html=True,
    )
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            f'<div class="stats-card">'
            f'<div class="stats-number">{st.session_state.total_queries}</div>'
            f'<div class="stats-label">Total Queries</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
    with col2:
        pct = (
            int(st.session_state.answered / st.session_state.total_queries * 100)
            if st.session_state.total_queries > 0
            else 0
        )
        st.markdown(
            f'<div class="stats-card">'
            f'<div class="stats-number">{pct}%</div>'
            f'<div class="stats-label">Answered</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<div class="section-label">💡 Topics Covered</div>',
        unsafe_allow_html=True,
    )
    for topic in st.session_state.chatbot.get_topics():
        st.markdown(f"<small style='color:#a5b4fc'>• {topic}</small>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f'<div class="section-label">📚 FAQ Database</div>'
        f'<p style="color:rgba(255,255,255,0.5);font-size:0.82rem">'
        f'{len(FAQ_DATA)} questions indexed</p>',
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = [
            {
                "role":             "bot",
                "text":             "Chat cleared! Ask me anything about AI, ML, Python, or CodeAlpha. 🚀",
                "confidence":       1.0,
                "matched_question": "",
                "found":            True,
            }
        ]
        st.session_state.total_queries = 0
        st.session_state.answered      = 0
        st.rerun()

    st.markdown("---")
    st.markdown(
        '<p style="color:rgba(255,255,255,0.3);font-size:0.75rem;text-align:center">'
        'Built by Dola Sangeetha<br>CodeAlpha AI Internship 2026</p>',
        unsafe_allow_html=True,
    )


# ── Main Layout ──────────────────────────────────────────────────────────────
# Header
st.markdown(
    '<div class="header-banner">'
    '<h1>🤖 AI FAQ Assistant</h1>'
    '<p>Powered by TF-IDF & Cosine Similarity · NLTK · Scikit-learn</p>'
    '</div>',
    unsafe_allow_html=True,
)

# Suggested questions (first 6 FAQs shown as clickable chips)
st.markdown(
    '<div class="section-label">💬 Suggested Questions</div>',
    unsafe_allow_html=True,
)
suggestions = st.session_state.chatbot.get_all_questions()[:6]

# Display suggestions in two rows of 3 columns
cols = st.columns(3)
for i, suggestion in enumerate(suggestions):
    with cols[i % 3]:
        short = suggestion if len(suggestion) <= 42 else suggestion[:39] + "…"
        if st.button(short, key=f"suggestion_{i}"):
            # Inject the suggestion as a question
            st.session_state.prefill_question = suggestion

st.markdown("<br>", unsafe_allow_html=True)

# Chat history
render_chat()

st.markdown("---")

# ── Chat Input ───────────────────────────────────────────────────────────────
with st.form(key="chat_form", clear_on_submit=True):
    input_col, button_col = st.columns([5, 1])
    with input_col:
        user_input = st.text_input(
            label="Your question",
            placeholder="Ask me anything about AI, ML, Python, or CodeAlpha…",
            label_visibility="collapsed",
            value=st.session_state.prefill_question,
        )
    with button_col:
        submitted = st.form_submit_button("Send ➤")

# Reset prefill after injection
st.session_state.prefill_question = ""

# Process the submitted question
if submitted and user_input.strip():
    # Record the user message
    st.session_state.messages.append(
        {"role": "user", "text": user_input.strip()}
    )

    # Get the chatbot's response
    result = st.session_state.chatbot.get_response(user_input.strip())

    # Record the bot message
    st.session_state.messages.append(
        {
            "role":             "bot",
            "text":             result["answer"],
            "confidence":       result["confidence"],
            "matched_question": result["matched_question"],
            "found":            result["found"],
        }
    )

    # Update stats
    st.session_state.total_queries += 1
    if result["found"]:
        st.session_state.answered += 1

    # Rerun to refresh the chat display
    st.rerun()
