from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary="Welcome to the API", tags=["Simple"])
async def read_root():
    """
    This is the root path of the API
    ***args: None
    ***returns: {"message": "Hello World"}
    """
    return {"message": "Hello World"}
