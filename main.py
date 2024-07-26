import replicate
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "欢迎来到 FastAPI 页面！"}

@app.post("/predictions/")
async def restore(request: Request):
    # 获取请求头中的 Authorization 和 Content-Type
    authorization = request.headers.get("Authorization")
    content_type = request.headers.get("Content-Type")

    # 打印或处理请求头信息
    print(f"Authorization: {authorization}")
    print(f"Content-Type: {content_type}")

    # 解析请求体中的JSON数据
    json_data = await request.json()

    version = json_data.get("version")
    input = json_data.get("input")

    # 调用CodeFormer进行处理
    try:
        client =replicate.Client(api_token=authorization.replace("Bearer ", ""))
        output = client.run(version, input)
    except Exception as e:
        print(f"Error during CodeFormer processing: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

    return JSONResponse(content={"output": output})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

