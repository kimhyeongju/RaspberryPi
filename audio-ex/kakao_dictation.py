import requests
import json
kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"

rest_api_key = '747821f9995b94f6ccfdd46b1c7b226c'

headers = {
"Content-Type": "application/octet-stream",
"X-DSS-Service": "DICTATION",
"Authorization": "KakaoAK 747821f9995b94f6ccfdd46b1c7b226c"
}

with open('heykakao.wav', 'rb') as fp:
    audio = fp.read()

res = requests.post(kakao_speech_url, headers=headers, data=audio)

print(res.text)


# 결과
"""
<multypart/form-data>
------newtonexkJGUv6QSms058LT       # part 구분용 경계문자열
Content-Type: application/json; charset=UTF-8   # header

{"type":"beginPointDetection","value":"BPD"}    # body(json으로 돼있음)
------newtonexkJGUv6QSms058LT
Content-Type: application/json; charset=UTF-8

{"type":"partialResult","value":"헤이"}      
------newtonexkJGUv6QSms058LT
Content-Type: application/json; charset=UTF-8

{"type":"partialResult","value":"헤이 카카오"}
------newtonexkJGUv6QSms058LT
Content-Type: application/json; charset=UTF-8

{"type":"endPointDetection","value":"EPD"}
------newtonexkJGUv6QSms058LT
Content-Type: application/json; charset=UTF-8
Speech-Length: 2

{"type":"finalResult","value":"헤이 카카오","nBest":[{"value":"헤이 카카오","score":98},{"value":"헤이 카카오야","score":0}]}
    # 최종인식은 finalResult에서 몇개가 나옴(점수가 높은게 정확)
    # find나 인덱스를 이용하여 값을 찾으면 됨
------newtonexkJGUv6QSms058LT--
"""

# finalResul를 추출
result_json_string = res.text[
    res.text.index('{"type":"finalResult"'):res.text.rindex('}')+1
]   # 슬라이싱(:)을 이용. rindex -> 오른쪽부터 값을 찾음
result = json.loads(result_json_string)     # 반대는 json.dumps()
print(result)
print('최종 인식 문장:',result['value'])
