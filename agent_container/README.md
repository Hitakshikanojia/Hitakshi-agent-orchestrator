# Riverty Unified Knowledge API (Agentic Orchestrator)

## Architecture Overview
- **Control Plane**: FastAPI handling tenant-authenticated requests.
- **Data Plane**: Docker-isolated containers for secure task execution.
- **Agent Logic**: LangGraph-based state machine for intelligent retrieval.

## How to Demo
1. Start Orchestrator: `python3 -m uvicorn app.main:app --reload`
2. Open Swagger: `http://127.0.0.1:8000/docs`
3. Execute Task: Pass `tenant_id` and `command`.