from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI App",
    description="My FastAPI App",
    version="0.0.1",
)


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "Your server is working fine, and FastAPI working and running FINE!!!! :)"}