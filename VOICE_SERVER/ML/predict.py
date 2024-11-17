from keras.models import load_model
import numpy as np

def predict_voice_class(mfcc): 
    model = load_model('ML/voice/learning_voice_class/models/voice_class_model_01.keras')
    input_data = np.expand_dims(mfcc, axis=0)  # (1, 時間軸, 特徴量の次元数)
    prediction = model.predict(input_data)
    return prediction

if __name__ == "__main__":
    # ここに音声データの特徴量（MFCC）を入力
    mfcc = np.random.rand(100, 20)
    print(predict_voice_class(mfcc))
    