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



class SpeechToTextOpenAIClient:

    def __init__(self):
        api_key = OPENAI_API_KEY
        if not api_key:
            raise ValueError("API key cannot be null or empty")

        self._api_key = "Bearer " + api_key
        self._endpoint = OPENAI_HOST + "/v1/audio/transcriptions"

    def call(self, file_path: str, print_response = True, **kwargs):
        headers = {
            "Authorization": self._api_key
        }
        with open(file_path, "rb") as f:
            files = {
                "file": f,
            }
            data = {
                "model": "gpt-4o-transcribe",
                **kwargs
            }

            response = requests.post(self._endpoint, headers=headers, files=files, data=data)

            if response.status_code == 200:
                data = response.json()
                if print_response:
                    print(json.dumps(data, indent=2))

                return data["text"]

        raise Exception(f"HTTP {response.status_code}: {response.text}")

client = SpeechToTextOpenAIClient()
text=client.call("codeus_audio.mp3")
print(text)