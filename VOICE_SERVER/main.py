from MIC.record import record_audio
from MIC.process import process
from ML.predict import predict_voice_class
from POSTING.post import send_prediction
import numpy as np 

def main():
    while True:
        audio_data = record_audio(duration=5, samplerate=48000, channels=1)
        audio_data_processed = process(audio_data)
        
        prediction = predict_voice_class(audio_data_processed)
        send_prediction(prediction)
        print(prediction)
    
if __name__ == "__main__":
    main()