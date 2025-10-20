import json

import requests

from task.constants import OPENAI_HOST, OPENAI_API_KEY

# https://platform.openai.com/docs/guides/speech-to-text?lang=curl

#TODO:
# You need to transcribe 'codeus_audio.mp3':
#   - Create Client that will go to transcriptions OpenAI API
#   - Call API and provide file (pay attention that you work with 'multipart/form-data')
#   - Get response with transcription
# ---
# Hints:
#   - Use /v1/audio/transcriptions endpoint
#   - Use whisper-1 or gpt-4o-transcribe model

url="/v1/audio/transcriptions"
with open("codeus_audio.mp3", "rb") as f:
    files = {
        "file": f,
    }
    data = {
        "model": "gpt-4o-transcribe"
    }
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    response = requests.post(OPENAI_HOST+url, headers=headers, files=files, data=data)

print(response.json())

