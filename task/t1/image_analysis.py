import base64

from task.client import OpenAIClient
from task.constants import OPENAI_HOST

# https://platform.openai.com/docs/guides/images-vision?api-mode=chat#analyze-images
# https://platform.openai.com/docs/guides/images-vision?api-mode=chat&format=base64-encoded#analyze-images

# TODO:
# You need to analyse these 2 images:
#   - https://a-z-animals.com/media/2019/11/Elephant-male-1024x535.jpg
#   - in this folder we have 'banner.png', load it as encoded data (see documentation)
# ---
# Hints:
#   - Use OpenAIClient to connect to OpenAI API
#   - Use /v1/chat/completions endpoint
#   - Function to encode image to base64 you can find in documentation
# ---
# In the end load both images (url and base64 encoded 'banner.png'), ask "Generate poem based on images" and se what will happen?

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")



url = "/v1/chat/completions"
image_path = "banner.png"
base64_image = encode_image(image_path)
message = {
    "role": "user",
    "content": [
        {"type": "text", "text": "Generate poem based on images"},
        {
            "type": "image_url",
            "image_url": {
                "url": "https://a-z-animals.com/media/2019/11/Elephant-male-1024x535.jpg",
            },
        },
        {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}",
            },
        },
    ],
}
client = OpenAIClient(OPENAI_HOST + url)
client.call(model="gpt-4.1-mini", messages=[message])
