# Riverty Case Study: Agentic Knowledge Orchestrator

This repository contains the **Agentic Runtime Orchestrator**, a unified knowledge API designed to consolidate internal data sources (Code Repos, Confluence, Databases) into a single, authoritative source of truth. 

This system leverages a multi-agent architecture to allow stakeholders—from Developers to Product Managers—to query complex internal systems using natural language and receive LLM-ready JSON responses.

---

## 🛠 Tech Stack
* **Backend:** Python, FastAPI, Pydantic
* **AI/Agents:** LangChain, LangGraph (Multi-agent orchestration)
* **Infrastructure:** Docker, Terraform, Azure
* **Frontend:** React, TypeScript

---

## 🚀 Key Features
* **Multi-Agent Orchestration:** Uses LangGraph to manage complex search tasks and stateful reasoning.
* **Source Traceability:** Every response includes rich metadata, timestamps, and stable IDs to ensure data is interpretable and reusable.
* **Security First:** Containerized execution via Docker to isolate runtime environments.
* **API First:** Fully documented endpoints via FastAPI/Swagger.

---

## 🏗 Architecture Overview
```mermaid
graph TD
    A[User/Client] -->|Natural Language Query| B(FastAPI Orchestrator)
    B --> C{Agentic Brain}
    C -->|Search Task| D[LangGraph Workflow]
    D -->|Tool Call| E[Internal Knowledge Base]
    E -->|Structured Data| D
    D -->|LLM-Ready JSON| B
    B -->|Verified Response| A