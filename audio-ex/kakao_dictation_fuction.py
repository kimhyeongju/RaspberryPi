import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = '747821f9995b94f6ccfdd46b1c7b226c'

headers = {
"Content-Type": "application/octet-stream",
"X-DSS-Service": "DICTATION",
"Authorization": "KakaoAK 747821f9995b94f6ccfdd46b1c7b226c"
}

def dictation(audio):
    res = requests.post(kakao_speech_url, headers=headers, data=audio)
    result_json_string = res.text[
    res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1
    ]

    result = json.loads(result_json_string)
    return result["value"]

if __name__ == "__main__":
    with open('heykakao.wav', 'rb') as fp:
        audio = fp.read()
        result = dictation(audio)
        print(result)