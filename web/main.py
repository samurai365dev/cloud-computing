import socket
import uvicorn
from ec2_metadata import ec2_metadata
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {
        "message": f"Hello, {ip_address} {hostname}",
        "metadata": ec2_metadata.public_ipv4
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
