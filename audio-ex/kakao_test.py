from kakao_dictation_fuction import *
from pyaudio_record import *
import io

audio_data = record(5)      # 녹음 데이터 리스트

# file_name = 'test.wav'
# save_wav(file_name, audio_data)
# f = open(filename,'rb')
# audio_data = f.read()

audio_stream = io.BytesIO()
save_wav(audio_stream, audio_data)  # 위에는 파일명을 주고, 여기선 파일 자체를 넘김
result = dictation(audio_stream.getvalue())        # wav 파일 내용 전달
print('인식결과:',result)