import os
import docker
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware # <--- ADD THIS LINE
from pydantic import BaseModel
from typing import List


app = FastAPI(title="Hitakshi- Riverty Agent Runtime", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your specific URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connect to my Mac's Docker engine
try:
    client = docker.from_env()
except Exception:
    client = None

class TaskRequest(BaseModel):
    tenant_id: str
    command: list[str]

# Simple Mock Blocklist
BANNED_TENANTS = {"malicious-actor-123"}

from pydantic import BaseModel
from typing import List

# This is the "AgentRequest" definition Python is looking for
class AgentRequest(BaseModel):
    tenant_id: str
    command: List[str]

@app.post("/execute")
async def execute_agent(request: AgentRequest):
    # 1. SECURITY GATE: Trip the "Kill Switch" before doing anything else
    if request.tenant_id == "malicious-actor-123":
        raise HTTPException(
            status_code=403, 
            detail="Tenant Blocked: Security Revocation"
        )

    # Initialize container as None so the 'except' block doesn't crash
    container = None 

    try:
        # 2. PROVISIONING: Run the Docker container
        # Use detach=True so 'container' becomes an object we can use
        container = client.containers.run(
            image="agent-runner:local",
            command=request.command,
            environment={
                "TENANT_ID": request.tenant_id,
                "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY")
            },
            detach=True, 
            remove=True,
            mem_limit="512m",
            nano_cpus=500000000
        )

        # 3. SUCCESS PATH: Return the 200 OK
        return {
            "status": "Secure Agent Provisioned",
            "container_id": str(container.id)[:12],
            "tenant": request.tenant_id
        }

    # 4. ERROR HANDLING: Catch Docker-specific failures
    except docker.errors.APIError as e:
        raise HTTPException(
            status_code=400, 
            detail=f"Infrastructure Error: {str(e)}"
        )
    except Exception as e:
        # This catches general Python errors so your server doesn't crash
        raise HTTPException(
            status_code=500, 
            detail=f"An unexpected error occurred: {str(e)}"
        )