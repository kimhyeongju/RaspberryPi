import pyaudio
import wave

MIC_DEVICE_ID = 1

CHUNK = 1024    # 버퍼의 크기(1K)
FORMAT = pyaudio.paInt16
CHANNELS = 1
# RATE = 44100     # 카카오 음성인식에서 요구하는 rate는 16000
RATE = 16000
SAMPLE_SIZE = 2  # 2byte

def record(record_seconds):     # 녹음할 시간을 매개변수로
    p = pyaudio.PyAudio()
    stream = p.open(input_device_index = MIC_DEVICE_ID,
                    format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("Start to record the audio.")
    frames = []

    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording is finished.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    return frames

# 녹음 데이터를 WAV 파일로 저장하기
def save_wav(target, frames):
    wf = wave.open(target, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(SAMPLE_SIZE)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))    # frames에 있는 녹음데이터(chunk)들을 byte데이터로 하나로 모음

    if isinstance(target, str):     # 문자열이 오면 닫고, ByteIO객체가 오면 안닫음
        wf.close()

if __name__ == '__main__':
    RECORD_SECONDS = 5
    frames = record(RECORD_SECONDS)

    WAVE_OUTPUT_FILENAME = "output.wav"
    save_wav(WAVE_OUTPUT_FILENAME, frames)