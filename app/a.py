import replicate

# 设置你的 API 令牌
REPLICATE_API_TOKEN = "r8_Tx7ACTPxyVx5zKphFP7wsmRM8Tp5dUz4EKhZn"
CODEFORMER_MODEL_ID = "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c"

# 初始化 Replicate 客户端
client = replicate.Client(api_token=REPLICATE_API_TOKEN)

# 获取模型
model = client.models.get("tencentarc/gfpgan")

# 查看模型的版本
versions = model.versions.list()
for version in versions:
    print(version.id)

# 使用最新版本进行预测
latest_version = versions[0]

# 进行预测
inputs = {
    "input_key1": "input_value1",
    "input_key2": "input_value2",
    # 添加更多的输入参数
}

#output = latest_version.predict(**inputs)
#print(output)
