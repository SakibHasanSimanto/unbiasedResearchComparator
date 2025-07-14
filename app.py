import streamlit as st
import requests
import os
import re

# --- Groq API settings ---
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # or hardcode for testing
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# --- Supported Models ---
MODEL_OPTIONS = {
    "DeepSeek R1 (70B Distill) ✅ [Recommended]": "deepseek-r1-distill-llama-70b",
    "Meta LLaMA 3 (8B)": "llama3-8b-8192",
    "Google Gemma 2 (9B Instruct)": "gemma2-9b-it",
    "Mistral SABA (24B)": "mistral-saba-24b"
}

# --- UI Header ---
st.set_page_config(page_title="Unbiased Research Comparator", layout="centered")
st.title("🔬 Unbiased Research Comparison Tool")
st.markdown("Compare two research summaries without author or journal bias.")

# --- Model Selector ---
selected_model_label = st.selectbox("🤖 Choose a Model", list(MODEL_OPTIONS.keys()), index=0)
LLM_MODEL = MODEL_OPTIONS[selected_model_label]

# --- Input Sections ---
with st.form("comparison_form"):
    paper_a = st.text_area("📝 Paper A Summary (Structured) / Abstract", height=300, placeholder="Title:\nAbstract:\nMethods:\nResults:\nContributions:\nLimitations:")
    paper_b = st.text_area("📝 Paper B Summary (Structured) / Abstract", height=300, placeholder="Title:\nAbstract:\nMethods:\nResults:\nContributions:\nLimitations:")
    submitted = st.form_submit_button("Compare")

# --- Prompt Template ---
def build_prompt(paper_a, paper_b):
    return f"""
Compare the two research papers below *strictly* based on their scientific content, and rate on a scale of 10. Include final rating in the end of your response. Be very concise with your response.

Explain shortly, evaluate, and compare the following dimensions:
1. Novelty and originality
2. Scientific rigor and methodology
3. Clarity of research goal and execution
4. Depth of analysis and significance of findings
5. Limitations and transparency
6. Potential research impact

### Paper A
{paper_a}

### Paper B
{paper_b}
"""

# --- Groq API Call ---
def query_groq(prompt, model):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a professional scientific reviewer. Do not think aloud or explain your process—just provide the direct comparison output in structured form."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        st.error(f"❌ Error {response.status_code}: {response.text}")
        return None

# --- Extract <think> section and separate ---
def split_thoughts(output):
    match = re.search(r"<think>(.*?)</think>", output, flags=re.DOTALL)
    if match:
        thinking = match.group(1).strip()
        final_output = re.sub(r"<think>.*?</think>", "", output, flags=re.DOTALL).strip()
        return thinking, final_output
    return None, output

# --- Display Output ---
if submitted:
    if not paper_a.strip() or not paper_b.strip():
        st.warning("Please fill in both paper summaries.")
    else:
        with st.spinner(f"Analyzing with {selected_model_label}..."):
            full_prompt = build_prompt(paper_a, paper_b)
            result = query_groq(full_prompt, LLM_MODEL)

        if result:
            thinking, final_output = split_thoughts(result)

            st.markdown("### 🧾 Final Comparison Result")
            st.markdown(final_output)

            if thinking:
                with st.expander("🧠 Model's Internal Thought Process (click to expand)"):
                    st.markdown(thinking)
