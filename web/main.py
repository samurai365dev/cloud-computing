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
        "metadata": {
            "public_ipv4": ec2_metadata.public_ipv4,
            "public_hostname": ec2_metadata.public_hostname,
            "region": ec2_metadata.region,
            "instance_id": ec2_metadata.instance_id,
            "domain": ec2_metadata.domain
        }
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
