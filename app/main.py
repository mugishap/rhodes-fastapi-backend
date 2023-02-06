from fastapi import FastAPI
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message":"Welcome to the Rhode API"}

@app.get("/docs")
def get_docs():
    return RedirectResponse(url="/docs/")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="0.0.0.0",port=8000)