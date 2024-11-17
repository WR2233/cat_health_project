import time
import json

def send_prediction(prediction):
    now = time.time()
    prediction = {
        "timestamp": now,
        "prediction": prediction
    }
    
    with open("prediction.json", "w") as f:
        json.dump(prediction, f)
    print(f"Prediction saved to prediction.json")
    