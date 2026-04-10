# 1. Upgrade to the latest stable high-performance version
FROM python:3.13-slim

# 2. Fix 'Fixable' vulnerabilities by updating the OS (Debian)
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 3. Securely set up the working environment
RUN useradd -m agentuser
WORKDIR /home/agentuser

# 4. Patch Python's package manager itself
RUN pip install --no-cache-dir --upgrade pip

# 5. Install your agent requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6. Copy the LangGraph agent code
COPY run_task.py .

# 7. Switch to the non-root user for 2026 Secure Runtime standards
USER agentuser

# 8. Start the agent
CMD ["python", "run_task.py"]