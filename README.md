# VBA 834 Spec Assistant

A RAG (Retrieval Augmented Generation) Chatbot designed to answer questions about the **Virtual Benefits Administrator (VBA) 834 Benefit Enrollment** specifications.

It parses the official "VBA Companion Document" and uses a local LLM (via LM Studio) to provide expert answers.

## 🚀 Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start Local LLM**:
    *   Open **LM Studio**.
    *   Load a model (recommend `deepseek-r1-distill-qwen-7b` or similar).
    *   Start the **Local Inference Server** on `http://127.0.0.1:1234`.

3.  **Run the Assistant**:
    ```bash
    python assistant.py
    ```

## 📂 Documentation
The bot reads from `docs/vba_834_guide.pdf`. If you have newer specs, replace this file.

## 🧠 How it Works
1.  **Ingest**: Reads the PDF using `PyPDF2`.
2.  **Search**: Filters pages based on your question keywords.
3.  **Answer**: Sends the relevant context + your question to the AI to generate a precise response.
