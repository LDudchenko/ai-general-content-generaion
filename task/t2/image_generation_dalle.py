import base64

from task.client import OpenAIClient
from task.constants import OPENAI_HOST

class Size:
    """
    The size of the generated image.
    """
    square: str = '1024x1024'
    height_rectangle: str = '1024x1792'
    width_rectangle: str = '1792x1024'


class Style:
    """
    The style of the generated image. Must be one of vivid or natural.
     - Vivid causes the model to lean towards generating hyper-real and dramatic images.
     - Natural causes the model to produce more natural, less hyper-real looking images.
    """
    natural: str = "natural"
    vivid: str = "vivid"


class Quality:
    """
    The quality of the image that will be generated.
     - ‘hd’ creates images with finer details and greater consistency across the image.
    """
    standard: str = "standard"
    hd: str = "hd"

# https://platform.openai.com/docs/guides/image-generation?image-generation-model=dall-e-3
# Request:
# curl https://api.openai.com/v1/images/generations \
#   -H "Content-Type: application/json" \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -d '{
#     "model": "dall-e-3",
#     "prompt": "smiling catdog",
#     "size": "1024x1024",
#     "style": "natural",
#     "quality": "standard"
#   }'

#TODO:
# You need to create some images with `dall-e-3` model:
#   - Generate an image with 'Smiling catdog'
#   - Play with configurations (size, style, quality)
# ---
# Hints:
#   - Use OpenAIClient to connect to OpenAI API
#   - Use /v1/images/generations endpoint
#   - The link with generated image will be returned in response

url = "/v1/images/generations"
client = OpenAIClient(OPENAI_HOST + url)
completion=client.call(model="dall-e-3", prompt="smiling catdog.", size=Size.square, style=Style.vivid, quality=Quality.hd)

# generated image: https://oaidalleapiprodscus.blob.core.windows.net/private/org-SLikGSZZXF1yDs26kPfi9MhU/user-5lrZEcQnIohFZaxPhMajZekB/img-6jo2m2JSHqOotkPZd1BohXZn.png?st=2025-10-20T19%3A07%3A41Z&se=2025-10-20T21%3A07%3A41Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=77e5a8ec-6bd1-4477-8afc-16703a64f029&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-10-20T19%3A27%3A32Z&ske=2025-10-21T19%3A27%3A32Z&sks=b&skv=2024-08-04&sig=2MhV4EUruc%2B6jcoGjHwaREPWm3cUBJCcMYkZ8xC4iNc%3D
img_url=completion["url"]
print(img_url)

