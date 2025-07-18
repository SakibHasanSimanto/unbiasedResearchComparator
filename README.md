# 🧠 PaperRanker: An Unbiased Research Quality Comparison Tool

**PaperRanker** is a lightweight academic tool built with [Streamlit](https://streamlit.io/) that uses large language models (LLMs) to compare and analyze the scientific quality of two research works—*without considering author reputation, journal prestige, or citation count*. It treats all submissions as preprints and provides a fair evaluation purely based on content.

---

## ✨ Features

- 🔬 **Content-based Comparison Only** – Ignores author/journal reputation, compares based on research contributions.
- 🧾 **Simple Interface** – Users enter summaries or abstracts of two papers.
- 🤖 **LLM-powered Judgement** – Uses free-to-use LLMs via [Groq API](https://console.groq.com/).
- 🧠 **Optional Model Thinking** – Displays or separates model "thought process" (like DeepSeek's `<think>` content).
- 🔄 **Switchable LLMs** – Choose from 4 high-performing models:
  - 🦙 LLaMA 3 (8B)
  - 📘 Gemma 2 (9B)
  - 🤔 DeepSeek LLaMA-70B (Recommended)
  - 🧪 Mistral-SABA 24B (Terms acceptance required)

---

## 🚀 Demo

Live demo on GitHub-hosted Streamlit app (replace with your link):  
📍 https://unbiased-research-comparator.streamlit.app/ 

---

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend API:** [Groq LLM API](https://console.groq.com/)
- **Languages:** Python 3.10+
- **Model Options:** LLaMA3, Gemma2, DeepSeek, Mistral (via Groq)

---


