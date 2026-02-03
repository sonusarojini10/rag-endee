# Retrieval-Augmented Generation (RAG) using Endee Vector Database

## Project Overview
This project demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline built using **Endee** as the vector database. The system retrieves semantically relevant document chunks using vector similarity search and prepares them as contextual input for downstream language model–based answer generation.

The goal of this project is to showcase how Endee can be effectively used as the core vector storage and retrieval engine in modern AI/ML applications.

---

## Problem Statement
Traditional keyword-based search systems fail to capture semantic meaning, leading to inaccurate or incomplete results when querying unstructured text. This project addresses this limitation by using vector embeddings and semantic similarity search to retrieve contextually relevant information.

---

## System Design and Technical Approach

The system follows the standard RAG architecture:

1. Input documents are split into text chunks
2. Each chunk is converted into a dense vector embedding
3. Embeddings are stored in an **Endee vector index**
4. User queries are embedded using the same model
5. Endee performs similarity search to retrieve the most relevant document chunks
6. Retrieved context can be used by an LLM to generate final answers

### Architecture Flow
Documents → Embeddings → Endee Index
User Query → Embedding → Endee Search → Relevant Context

---

## Role of Endee in This Project
Endee is used as the **vector database** for this RAG system. Specifically, it is responsible for:

- Creating and managing vector indexes
- Storing document embeddings
- Performing cosine similarity–based semantic search
- Returning top-k relevant document chunks for retrieval

The project uses the **official Endee Python SDK** and follows Endee’s index-based API design.

---

## Project Structure

rag_app/
├ data/
│ └ sample.txt
├ ingest.py
├ query.py
├ requirements.txt
└ README.md


- `ingest.py`: Handles document embedding and ingestion into Endee
- `query.py`: Performs semantic retrieval using Endee
- `data/`: Sample input documents for ingestion

---

## Setup Instructions

### Environment Setup
```bash
conda create -n endee-rag python=3.10 -y
conda activate endee-rag
pip install -r requirements.txt
```

Endee Server Dependency

Endee operates as a client–server vector database.
The Python client communicates with an Endee server over HTTP.

The docker-compose.yml provided in the Endee repository references an internal Endee OSS image that may require authenticated access. As a result, the Endee server may not be publicly runnable in all environments.

For this project, the focus is on demonstrating:

Correct usage of the Endee Python SDK

Index-based vector ingestion and retrieval

RAG system design using Endee as the vector database

When an Endee server is available, the ingestion and query scripts run end-to-end without modification.

Future Enhancements

Integration with an LLM for complete answer generation

Support for PDF and multi-document ingestion

Web-based interface for interactive querying

Scalable deployment with remote Endee clusters

Conclusion

This project demonstrates a clean and practical implementation of a Retrieval-Augmented Generation pipeline using Endee as the vector database. It highlights Endee’s role in semantic retrieval and its applicability in real-world AI/ML systems.

