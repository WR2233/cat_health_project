import os
import pandas as pd

def filename_to_csv(directory, output_csv, delimiter="_"):
    """
    Extracts metadata from filenames in a directory and saves it as a CSV file.
    
    Parameters:
        directory (str): Path to the directory containing .wav files.
        output_csv (str): Path to save the resulting CSV file.
        delimiter (str): Delimiter used to split the filename into metadata parts.
    """
    data = []
    
    # Iterate through all .wav files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            # Remove file extension and split the filename into parts
            parts = os.path.splitext(filename)[0].split(delimiter)
            parts += [filename]  # Add the filename to the parts
            data.append(parts)
    
    # Create a DataFrame and save it to CSV
    df = pd.DataFrame(data)
    df.to_csv(output_csv, index=False, header=False)
    print(f"CSV file saved to: {output_csv}")

if __name__ == "__main__":
    wav_directory = "/Users/ryuhei/newPractice/cat_health_project/voice_learning/datasets/cat_voice"
    output_csv_path = "/Users/ryuhei/newPractice/cat_health_project/voice_learning/datasets/metadata.csv"
    filename_to_csv(wav_directory, output_csv_path) 