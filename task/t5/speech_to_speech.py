import base64
import json
from datetime import datetime

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/audio?example=audio-in#add-audio-to-your-existing-application

#TODO:
# You need to generate answer in audio format based on the audio message:
#   - Create Client that is similar with OpenAIClients but extracts from message audio (instead of content)
#   - Call API
#   - Get response as base64 content, decode and save as .mp3 file
# ---
# Hints:
#   - Use /v1/chat/completions endpoint
#   - Use gpt-4o-audio-preview model
#   - Use modalities=["text", "audio"]
#   - Use audio={"voice": "ballad", "format": "mp3"}
#   - Similar method to encode audio https://platform.openai.com/docs/guides/images-vision?api-mode=chat&lang=python

with open("question.mp3", "rb") as f:
    audio_base64 = base64.b64encode(f.read()).decode("utf-8")

payload = {
    "model": "gpt-4o-audio-preview",
    "modalities": ["text", "audio"],
    "audio": {
        "voice": "ballad",
        "format": "mp3"
    },
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "input_audio",
                    "input_audio": {
                        "data": audio_base64,
                        "format": "mp3"
                    }
                }
            ]
        }
    ]
}

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

url="/v1/chat/completions"
response = requests.post(OPENAI_HOST+url, headers=headers, json=payload)

result = response.json()
audio_data = result["choices"][0]["message"]["audio"]["data"]
audio_bytes = base64.b64decode(audio_data)

with open("answer.mp3", "wb") as f:
    f.write(audio_bytes)

