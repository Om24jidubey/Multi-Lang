



import streamlit as st
from deep_translator import GoogleTranslator

# 🌐 Supported languages for dropdown
language_options = [
    "english", "hindi", "french", "german", "spanish", "italian",
    "japanese", "korean", "chinese (simplified)", "arabic", "russian",
    "portuguese", "bengali", "turkish", "urdu"
]

# 🌟 Page Config
st.set_page_config(page_title="Om’s Multi-Language Translator", layout="centered", page_icon="🌍")

# 💡 Custom CSS for unique UI
st.markdown("""
    <style>
        .main {
            background-color: #f4f4f4;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            text-align: center;
            font-size: 2.8em;
            font-weight: bold;
            color: #4A90E2;
            margin-top: 10px;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #666;
            margin-bottom: 30px;
        }
        .stTextArea, .stSelectbox {
            border-radius: 10px !important;
        }
        .stButton>button {
            background-color: #4A90E2;
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #357ABD;
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Page Title
st.markdown('<div class="title">🌍 Om’s Multi-Language Translator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Translate text between your favorite languages for free.</div>', unsafe_allow_html=True)

# 📝 Input Section
text_to_translate = st.text_area("✏️ Enter text to translate:", key="input_text")
source_lang = st.selectbox("🌐 Source Language:", language_options, index=0)
target_lang = st.selectbox("🌐 Target Language:", language_options, index=1)

# 🚀 Translate Button
if st.button("🔄 Translate"):
    if text_to_translate and source_lang and target_lang:
        with st.spinner("Translating..."):
            try:
                translated_text = GoogleTranslator(
                    source=source_lang.lower(),
                    target=target_lang.lower()
                ).translate(text_to_translate)

                st.success("✅ Translation Complete!")
                st.text_area("📝 Translated Text:", translated_text, height=200, key="output_text")

            except Exception as e:
                st.error(f"❌ Translation failed: {e}")
    else:
        st.warning("⚠️ Please fill in all fields before translating.")
