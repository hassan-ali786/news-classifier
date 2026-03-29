import streamlit as st
import sys
import os

# Fix import path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))
from predict import predict_category

# Page config
st.set_page_config(
    page_title="News Classification System",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Premium CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

.title {
    text-align: center;
    font-size: 40px;
    font-weight: 700;
    margin-top: 20px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 40px;
}

/* Card */
.card {
    background: rgba(255, 255, 255, 0.05);
    padding: 30px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 6px 25px rgba(0,0,0,0.5);
}

/* Button */
.stButton>button {
    width: 100%;
    background: linear-gradient(90deg, #6366f1, #4f46e5);
    color: white;
    border-radius: 10px;
    padding: 12px;
    font-size: 16px;
    border: none;
}

/* Result Box */
.result-box {
    background: rgba(99,102,241,0.1);
    padding: 20px;
    border-radius: 10px;
    margin-top: 20px;
}

/* Labels */
.label {
    font-size: 14px;
    color: #94a3b8;
}

.value {
    font-size: 20px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title">News Classification System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Machine Learning based text classification</div>', unsafe_allow_html=True)

# Layout
left, center, right = st.columns([1,2,1])

with center:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    user_input = st.text_area("Enter News Article", height=180)

    if st.button("Analyze News"):
        if user_input.strip():
            category, confidence = predict_category(user_input)

            # ✅ FIX (without breaking UI)
            try:
                category = int(category)
            except:
                pass

            label_map = {
                1: "World",
                2: "Sports",
                3: "Business",
                4: "Technology"
            }

            category_name = label_map.get(category, "Unknown")

            st.markdown('<div class="result-box">', unsafe_allow_html=True)

            col1, col2 = st.columns(2)

            with col1:
                st.markdown('<div class="label">Category</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="value">{category_name}</div>', unsafe_allow_html=True)

            with col2:
                st.markdown('<div class="label">Confidence</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="value">{confidence:.2f}</div>', unsafe_allow_html=True)

            st.progress(int(confidence * 100))

            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.warning("Please enter text")

    st.markdown('</div>', unsafe_allow_html=True)