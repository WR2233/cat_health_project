import pandas as pd
import os
import numpy as np        
import random
import pandas as pd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import seaborn as sn
from sklearn import model_selection
from sklearn import preprocessing
import IPython.display as ipd

# define directories
base_dir = "./"
esc_dir = os.path.join(base_dir, "ESC-50-master")
meta_file = os.path.join(esc_dir, "/Users/ryuhei/newPractice/cat_health_project/voice_learning/datasets/catvoice_y.csv")
audio_dir = os.path.join(esc_dir, "/Users/ryuhei/newPractice/cat_health_project/voice_learning/datasets/cat_voice")

# load metadata
meta_data = pd.read_csv(meta_file)

# get data size
data_size = meta_data.shape
print(data_size)

# arrange target label and its name
class_dict = {}
for i in range(data_size[0]):
    if meta_data.loc[i,"target"] not in class_dict.keys():
        class_dict[meta_data.loc[i,"target"]] = meta_data.loc[i,"category"]

