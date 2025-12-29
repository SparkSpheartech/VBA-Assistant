# VBA Spec Assistant - AI-Powered Technical Documentation Bot

**VBA Spec Assistant** is a Retrieval-Augmented Generation (RAG) tool designed to simplify the interpretation of complex healthcare data specifications.

It serves as an intelligent interface between technical implementation teams and the dense "Virtual Benefits Administrator (VBA) 834 Companion Guide," allowing users to query specifications in natural language and receive instant, citation-backed answers.

## 🎯 Project Goal
Healthcare interoperability projects often fail due to misinterpretation of EDI specs. The goal of this project was to:
1.  **Reduce Research Time**: Cut down time spent `CTRL+F` searching through 100+ page PDFs.
2.  **Standardize Interpretation**: Ensure all engineers implement segments (e.g., Loop 2300) consistently based on the official guide.
3.  **Demonstrate AI Integration**: Showcase how Local LLMs can be integrated into enterprise workflows securely.

## 🏗 Technical Architecture

### 1. The Knowledge Base (Ingestion)
*   The system parses the **VBA 834 Companion Document** (PDF format) using `PyPDF2`.
*   It handles text extraction, cleaning, and normalization to prepare unstructured data for the AI model.

### 2. The Retrieval Engine (RAG)
*   Instead of sending the entire document (which exceeds context windows), the system uses a **Keyword-Driven Context Retrieval** algorithm.
*   It dynamically ranks pages based on relevance to the user's specific query (e.g., "Ref ID for plan coverage").

### 3. The Cognitive Engine (LLM)
*   Integrated with a **Local Large Language Model** (via LM Studio API) to ensure data privacy—no proprietary documentation leaves the local environment.
*   The System Prompt is rigorously engineering to act as a "Subject Matter Expert," prioritizing accuracy over creativity.

## � Key Features
*   **Context-Aware**: Understands the difference between "Group Number" in the Header (Loop 1000A) vs the Member Detail (Loop 2000).
*   **Privacy-First**: Designed to run 100% offline using local inference servers.
*   **Zero-Dependency**: Lightweight Python implementation without heavy vector database overhead (FAISS/Pinecone) for portability.

## 🛠 Tech Stack
*   **Language**: Python 3.10+
*   **PDF Processing**: PyPDF2
*   **AI Integration**: OpenAI SDK (Custom local endpoint)
*   **NLP Logic**: Custom keyword ranking algorithm

## 💡 Why this Matters
This project demonstrates the ability to not just *use* AI, but to **engineer tools** that solve domain-specific problems.
In the context of Benefit Enrollment (EDI 834), precision is critical. This assistant aids developers in adhering to strict compliance standards (HIPAA/X12) by providing instant access to the correct implementation rules.

---
*Created by Shazaly Musa*
