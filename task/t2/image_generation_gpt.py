import base64
from datetime import datetime

from task.client import OpenAIClient
from task.constants import OPENAI_HOST

# https://platform.openai.com/docs/guides/image-generation?image-generation-model=gpt-image-1&api=image&multi-turn=imageid
# ---
# Request:
# curl -X POST "https://api.openai.com/v1/images/generations" \
#     -H "Authorization: Bearer $OPENAI_API_KEY" \
#     -H "Content-type: application/json" \
#     -d '{
#         "model": "gpt-image-1",
#         "prompt": "smiling catdog."
#     }'
# Response:
# {
#   "created": 1699900000,
#   "data": [
#     {
#       "b64_json": Qt0n6ArYAEABGOhEoYgVAJFdt8jM79uW2DO...,
#     }
#   ]
# }

#TODO:
# You need to create some images with `gpt-image-1` model:
#   - Generate an image with 'Smiling catdog'
#   - Decode and save it locally
# ---
# Hints:
#   - Use OpenAIClient to connect to OpenAI API
#   - Use /v1/images/generations endpoint
#   - The image will be returned in base64 format
url = "/v1/images/generations"
client = OpenAIClient(OPENAI_HOST + url)
completion=client.call(model="gpt-image-1", prompt="smiling catdog.")

img_data=completion["data"][0]["b64_json"]

image_bytes = base64.b64decode(img_data)

with open("result_gpt.png", "wb") as f:
    f.write(image_bytes)
