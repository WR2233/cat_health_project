import pyaudio
import wave
import numpy as np
def record_audio(duration=5, samplerate=48000, channels=1, filename="output.wav", state="return"):
    """
    pyaudioを使用して音声を録音し、
        state="reserve"で WAVファイルとして保存
        state="return" で np.arrayにして返す 

    :param duration: 録音時間（秒）
    :param samplerate: サンプリング周波数
    :param channels: チャンネル数（1: モノラル, 2: ステレオ）
    :param filename: 出力するファイル名
    """
    p = pyaudio.PyAudio()

    # 録音の設定
    stream = p.open(format=pyaudio.paInt16,  # 16ビット整数形式
                    channels=channels,
                    rate=samplerate,
                    input=True,
                    frames_per_buffer=1024)
    
    print(f"Recording for {duration} seconds...")

    # 音声データをフレーム単位で録音
    frames = []
    for i in range(0, int(samplerate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Recording complete.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    if state == "return":
        audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)
        return audio_data
    
    if state == "reserve":
        # 録音したデータをWAVファイルに保存
        with wave.open(filename, 'wb') as wf:
            wf.setnchannels(channels)  # チャンネル数（モノラルまたはステレオ）
            wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))  # サンプルサイズ（16ビット）
            wf.setframerate(samplerate)  # サンプリング周波数
            wf.writeframes(b''.join(frames))  # 録音データを書き込み
        print(f"Audio saved to {filename}")
        return None
    else: 
        print("state is invalid")
        return None

if __name__ == "__main__":
    record_audio(duration=5, samplerate=48000, channels=1, filename="output.wav", state="reserve")