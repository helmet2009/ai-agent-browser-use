# backend/main.py
from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.post("/api/agent/task")
async def run_agent_task(task: dict):
    try:
        # ตัวอย่าง: รัน container ที่ใช้โมเดล DeepSeek-R1
        result = subprocess.run(["docker", "run", "--rm", "ai-model:deepseek"], capture_output=True, text=True)
        return {"status": "success", "output": result.stdout}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
