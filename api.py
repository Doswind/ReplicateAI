import requests

api_token = "r8_VvL5FnrfzrJyiVOTDJjAsRvCYBuNiZa16JMQr"
model_version = "7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56"
model_id = "stability-ai/stable-diffusion"  # 假设模型 ID 是 "stability-ai/stable-diffusion"

input_data = {
    "image": "https://replicate.delivery/mgxm/7534e8f1-ee01-4d66-ae40-36343e5eb44a/003.png",
    "upscale": 2,
    "face_upsample": True,
    "background_enhance": True,
    "codeformer_fidelity": 0.1
}

url = "https://api.replicate.com/v1/predictions"
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}
data = {
    "version": model_version,
    "input": input_data,
    #"model": model_id
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("Prediction submitted successfully!")
    prediction_id = response.json()["id"]
    print(f"Prediction ID: {prediction_id}")
else:
    print(f"Error: {response.text}")


#api_token = "r8_VvL5FnrfzrJyiVOTDJjAsRvCYBuNiZa16JMQr"
#prediction_id = "YOUR_PREDICTION_ID"  # 替换为实际的预测 ID

url = f"https://api.replicate.com/v1/predictions/{prediction_id}"
headers = {
    "Authorization": f"Bearer {api_token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Prediction results:")
    print(response.json())
else:
    print(f"Error: {response.text}")
