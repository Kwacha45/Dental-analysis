import requests

flacFile = "output.flac"

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
headers = {"Authorization": "Bearer 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"}


def query(filename):
    with open(filename, "rb") as f:
        info = f.read()
    response = requests.post(API_URL, headers=headers, data=info)
    return response.json()


sentence = query(flacFile)["text"]
print(sentence)


