import utility

def process(audio_data): # np.array -> pd.array
    
    # MLの前処理を行う
    # 具体的にはMLの期待する入力形式に変換する pd.array(128,920)
    melsp = utility.calculate_melsp(audio_data)
    return melsp
    