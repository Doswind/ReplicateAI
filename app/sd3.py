import replicate

REPLICATE_API_TOKEN = "r8_Tx7ACTPxyVx5zKphFP7wsmRM8Tp5dUz4EKhZn"
CODEFORMER_MODEL_ID = "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c"

client =replicate.Client(api_token=REPLICATE_API_TOKEN)

output = client.run(
    "stability-ai/stable-diffusion-3",
    input={
        "cfg": 3.5,
        "steps": 28,
        "prompt": "a photo of vibrant artistic graffiti on a wall saying \"SD3 medium\"",
        "aspect_ratio": "3:2",
        "output_format": "webp",
        "output_quality": 90,
        "negative_prompt": "",
        "prompt_strength": 0.85
    }
)
print(output)
