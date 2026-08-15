# 📋 VBA Spec Assistant — AI-Powered EDI 834 Documentation Agent

> **An intelligent RAG (Retrieval-Augmented Generation) agent that interprets complex healthcare EDI specifications**  
> Ask natural language questions about VBA 834 Companion Guide — get instant, citation-backed answers.

---

## 🧠 AI Agent Architecture

```mermaid
graph TB
    subgraph INPUT["📄 Knowledge Base"]
        I1[VBA 834 Companion\nGuide PDF]
        I2[EDI Segment\nDefinitions]
        I3[Loop Structure\nDocumentation]
    end

    subgraph INGESTION["📚 Ingestion Agent Pipeline"]
        P1[PDF Parser Agent\nPyPDF2 Extraction]
        P2[Text Cleaner Agent\nNormalization]
        P3[Page Ranker Agent\nRelevance Indexing]
    end

    subgraph QUERY["🔍 Query Processing"]
        Q1[Natural Language\nQuery Agent]
        Q2[Keyword Context\nRetrieval Agent]
        Q3[Page Ranking\nAlgorithm]
    end

    subgraph LLM["🧠 Local LLM Agent"]
        L1[Context Assembly\nAgent]
        L2[Subject Matter\nExpert Agent]
        L3[Citation Generator\nAgent]
    end

    subgraph OUTPUT["📤 Response"]
        O1[Answer with\nSegment References]
        O2[Loop Location\nCitations]
        O3[Implementation\nGuidance]
    end

    I1 --> P1
    I2 --> P1
    I3 --> P1
    P1 --> P2
    P2 --> P3
    Q1 --> Q2
    Q2 --> Q3
    Q3 --> L1
    P3 --> L1
    L1 --> L2
    L2 --> L3
    L3 --> O1
    L3 --> O2
    L3 --> O3

    style P1 fill:#4CAF50,stroke:#333,color:#fff
    style Q2 fill:#2196F3,stroke:#333,color:#fff
    style L2 fill:#FF9800,stroke:#333,color:#fff
    style L3 fill:#9C27B0,stroke:#333,color:#fff
```

## 🤖 What the AI Agents Do

| Agent | Function |
|-------|----------|
| **PDF Ingestion Agent** | Parses 100+ page VBA 834 Companion PDF, extracts and normalizes text, indexes pages by segment/loop |
| **Context Retrieval Agent** | Instead of sending the entire document (which exceeds context windows), dynamically ranks pages based on relevance to your query using a keyword-driven algorithm |
| **Subject Matter Expert Agent** | Local LLM (via LM Studio) acts as an EDI specialist — System Prompt engineered for precision over creativity |
| **Citation Agent** | Every answer includes exact segment/loop references — "Loop 2300, Segment REF, Element REF02" |

## 🔄 Before vs After

```mermaid
graph LR
    subgraph BEFORE["❌ Before (Manual)"]
        BM[CTRL+F through\n100+ page PDFs\nHours of research\nInconsistent interpretation\nBetween engineers]
    end

    subgraph AFTER["✅ After (AI Agent)"]
        AM[Natural language query\nInstant cited answers\nStandardized interpretation\n100% offline & private]
    end

    BM -->|VBA Spec Assistant| AM
```

## 🛠 Tech Stack

| Component | Technology | Agent Role |
|-----------|-----------|------------|
| **PDF Processing** | PyPDF2 | Document ingestion agent |
| **AI Engine** | OpenAI SDK (Local Endpoint) | LLM inference agent |
| **Retrieval** | Custom keyword ranking | Context retrieval agent |
| **Privacy** | 100% offline (LM Studio) | Security isolation agent |
| **Language** | Python 3.10+ | Agent framework |

## ⚡ Quick Start

```bash
# Ask a question about EDI 834 specs
python assistant.py "What is the REF segment in Loop 2300?"
# Output: Answer with citations to specific pages/segments
```

## 💡 Why This Matters

Healthcare interoperability projects often fail due to misinterpretation of EDI specs. This AI agent:
1. **Reduces Research Time:** No more CTRL+F through 100+ page PDFs
2. **Standardizes Interpretation:** Every engineer gets the same answer from the official guide
3. **Privacy-First:** Runs 100% offline using local inference — no proprietary docs leave your environment

---

Built by **[Shazaly Musa](https://github.com/SparkSpheartech)** — Founder, SparkSphear Tech  
*AI Agents for Healthcare EDI & Compliance*