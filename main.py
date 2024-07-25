from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import codeformer as cf

app = FastAPI()

@app.post("/predictions/")
async def restore(request: Request):
    # 解析请求体中的JSON数据
    json_data = await request.json()

    # 提取图像URL和其他参数
    image_url = json_data.get("image")
    upscale = json_data.get("upscale", 2)
    face_upsample = json_data.get("face_upsample", True)
    background_enhance = json_data.get("background_enhance", True)
    codeformer_fidelity = json_data.get("codeformer_fidelity", 0.1)

    # 打印输入参数（可选）
    print(f"Image URL: {image_url}")
    print(f"Upscale: {upscale}")
    print(f"Face Upsample: {face_upsample}")
    print(f"Background Enhance: {background_enhance}")
    print(f"Codeformer Fidelity: {codeformer_fidelity}")


    # 调用CodeFormer进行处理
    try:
        output = cf.run(json_data)
    except Exception as e:
        print(f"Error during CodeFormer processing: {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

    # 打印输出内容（可选）
    print(f"Output: {output}")

    return JSONResponse(content={"output": output})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)