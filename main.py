import uvicorn
from fastapi import FastAPI

# Create the application instance
app = FastAPI()

# Define a route for the root URL
@app.get("/")
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    # Use "main:app" as a string to enable the reload feature
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
