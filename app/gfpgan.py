import replicate

REPLICATE_API_TOKEN = "r8_Tx7ACTPxyVx5zKphFP7wsmRM8Tp5dUz4EKhZn"
CODEFORMER_MODEL_ID = "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c"

client =replicate.Client(api_token=REPLICATE_API_TOKEN)

def demo():
	output = client.run(
        CODEFORMER_MODEL_ID,
		input={
			"img": "https://replicate.delivery/mgxm/59d9390c-b415-47e0-a907-f81b0d9920f1/187400315-87a90ac9-d231-45d6-b377-38702bd1838f.jpg",
			"scale": 2,
			"version": "v1.4"
		}
	)
	print(output)

def run(params):
    image_url = client.run(
        CODEFORMER_MODEL_ID,
        input=params
    )
    return image_url
