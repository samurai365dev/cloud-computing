import socket
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {"message": f"Hello, {ip_address} {hostname}"}

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")