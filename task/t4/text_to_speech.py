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


payload = {
    "model": "gpt-4o-mini-tts",
    "input": "Why can't we say that black is white?",
    "voice": Voice.coral,
    "instructions": "Speak in a cheerful and positive tone."
}

headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json"
}

response = requests.post(OPENAI_HOST+"/v1/audio/speech", headers=headers, json=payload)

with open("answer.mp3", "wb") as f:
    f.write(response.content)
