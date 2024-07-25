from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "欢迎来到我的简单FastAPI应用！"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
