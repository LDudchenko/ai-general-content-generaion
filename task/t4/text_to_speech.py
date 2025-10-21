import json
from datetime import datetime

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY


# https://platform.openai.com/docs/guides/text-to-speech
# Request:
# curl https://api.openai.com/v1/audio/speech \
#   -H "Authorization: Bearer $OPENAI_API_KEY" \
#   -H "Content-Type: application/json" \
#   -d '{
#     "model": "gpt-4o-mini-tts",
#     "input": "Why can't we say that black is white?",
#     "voice": "coral",
#     "instructions": "Speak in a cheerful and positive tone."
#   }' \
# Response:
#   bytes with audio

# TODO:
# You need to convert text to speech:
#   - Create Client that will go to speech OpenAI API
#   - Call API
#   - Get response and save as .mp3 file
# ---
# Hints:
#   - Use /v1/audio/speech endpoint
#   - Use gpt-4o-mini-tts model


class Voice:
    alloy: str = 'alloy'
    ash: str = 'ash'
    ballad: str = 'ballad'
    coral: str = 'coral'
    echo: str = 'echo'
    fable: str = 'fable'
    nova: str = 'nova'
    onyx: str = 'onyx'
    sage: str = 'sage'
    shimmer: str = 'shimmer'

class TextToSpeechOpenAIClient:

    def __init__(self):
        api_key = OPENAI_API_KEY
        if not api_key:
            raise ValueError("API key cannot be null or empty")

        self._api_key = "Bearer " + api_key
        self._endpoint = OPENAI_HOST + "/v1/audio/speech"

    def call(self, print_request = True, print_response = True, **kwargs):
        headers = {
            "Authorization": self._api_key,
            "Content-Type": "application/json"
        }

        if print_request:
            print(json.dumps(kwargs, indent=2))

        response = requests.post(url=self._endpoint, headers=headers, json=kwargs)

        if response.status_code == 200:
            if print_response:
                print(response)

            return response.content

        raise Exception(f"HTTP {response.status_code}: {response.text}")

payload = {
    "model": "gpt-4o-mini-tts",
    "input": "Why can't we say that black is white?",
    "voice": Voice.coral,
    "instructions": "Speak in a cheerful and positive tone."
}
client = TextToSpeechOpenAIClient()
response = client.call(**payload)

with open("answer.mp3", "wb") as f:
    f.write(response)