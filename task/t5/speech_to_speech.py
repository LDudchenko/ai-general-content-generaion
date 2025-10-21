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


class SpeechToSpeechOpenAIClient:

    def __init__(self):
        api_key = OPENAI_API_KEY
        if not api_key:
            raise ValueError("API key cannot be null or empty")

        self._api_key = "Bearer " + api_key
        self._endpoint = OPENAI_HOST + "/v1/chat/completions"

    def call(self, print_request = True, print_response = True, **kwargs):
        headers = {
            "Authorization": self._api_key,
            "Content-Type": "application/json"
        }

        if print_request:
            print(json.dumps(kwargs, indent=2))

        response = requests.post(url=self._endpoint, headers=headers, json=kwargs)

        if response.status_code == 200:
            data = response.json()
            if print_response:
                print(json.dumps(data, indent=2))

            return data["choices"][0]["message"]["audio"]["data"]

        raise Exception(f"HTTP {response.status_code}: {response.text}")

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

client = SpeechToSpeechOpenAIClient()
audio_data = client.call(**payload)
audio_bytes = base64.b64decode(audio_data)

with open("answer.mp3", "wb") as f:
    f.write(audio_bytes)