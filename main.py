from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import app.codeformer as cf
import app.gfpgan as gf

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "欢迎来到 FastAPI 页面！"}

@app.post("/predictions/")
async def restore(request: Request):
    # 解析请求体中的JSON数据
    json_data = await request.json()

    # 调用CodeFormer进行处理
    try:
        output = gf.run(json_data)
    except Exception as e:
        print(f"Error during CodeFormer processing: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

    # 打印输出内容（可选）
    print(f"Output: {output}")

    return JSONResponse(content={"output": output})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
