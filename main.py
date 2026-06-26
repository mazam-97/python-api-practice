from fastapi import FastAPI

# 1. Initialize the FastAPI app instance
app = FastAPI()

# 2. Define a GET endpoint for the root URL
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# 3. Define a dynamic GET endpoint with a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query_param": q}
