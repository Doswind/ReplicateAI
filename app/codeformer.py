import replicate


REPLICATE_API_TOKEN = "r8_VvL5FnrfzrJyiVOTDJjAsRvCYBuNiZa16JMQr"
CODEFORMER_MODEL_ID = "sczhou/codeformer:7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56"

cf_client =replicate.Client(api_token=REPLICATE_API_TOKEN)

def demo():
    image_url = cf_client.run(
        CODEFORMER_MODEL_ID,
        input={
            "image": "https://c-ssl.duitang.com/uploads/item/201806/01/20180601131710_vwZvZ.jpeg",
            #"image": "https://replicate.delivery/mgxm/7534e8f1-ee01-4d66-ae40-36343e5eb44a/003.png",
            "upscale": 2,
            "face_upsample": True,
            "background_enhance": True,
            "codeformer_fidelity": 0.1
        }
    )
    return image_url

def run(params):
    image_url = cf_client.run(
        CODEFORMER_MODEL_ID,
        input=params
    )
    return image_url

