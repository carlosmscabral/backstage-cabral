import os
import yaml
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI(
    title="pet-do-cabral-api",
    description="Auto-scaffolded FastAPI service for Cloud Run"
)

# Optional: You can load the bundled OpenAPI spec if you want to strictly use it,
# but FastAPI generates its own docs out of the box.
@app.get("/")
def read_root():
    return {"message": "Hello from pet-do-cabral-api! Running strictly in Cloud Run."}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
