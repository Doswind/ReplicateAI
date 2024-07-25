curl -s -X POST \
  -H "Authorization: Bearer r8_Tx7ACTPxyVx5zKphFP7wsmRM8Tp5dUz4EKhZn" \
  -H "Content-Type: application/json" \
  -d $'{
    "version": "0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c",
    "input": {
      "img": "https://replicate.delivery/mgxm/59d9390c-b415-47e0-a907-f81b0d9920f1/187400315-87a90ac9-d231-45d6-b377-38702bd1838f.jpg",
      "scale": 2,
      "version": "v1.4"
    }
  }' \
  https://api.replicate.com/v1/predictions
