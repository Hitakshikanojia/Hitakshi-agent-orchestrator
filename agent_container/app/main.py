import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Omni-Source Agentic Orchestrator", 
    description="A unified runtime for multi-agent knowledge retrieval.",
    version="1.0.0"
)

# Keep CORS for browser compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AgentRequest(BaseModel):
    tenant_id: str
    command: List[str]

BANNED_TENANTS = {"unauthorized-actor-000"}

@app.post("/execute")
async def execute_agent(request: AgentRequest):
    if request.tenant_id in BANNED_TENANTS:
        raise HTTPException(status_code=403, detail="Access Denied")

    # This is the "Mock" response that ensures your demo never crashes
    return {
        "status": "success",
        "request_id": f"job-{os.urandom(4).hex()}",
        "tenant_id": request.tenant_id,
        "agent_output": {
            "summary": f"Orchestrated task: '{request.command[0]}'",
            "data_retrieved": [
                {
                    "source": "Internal Knowledge Base",
                    "content": "System parameters verified. Environment stable.",
                    "relevance_score": 0.98
                }
            ],
            "execution_metadata": {
                "agent_chain": ["auth_validator", "logic_engine", "formatter"],
                "latency_ms": 142
            }
        },
        "timestamp": "2026-04-10T16:00:00Z"
    }