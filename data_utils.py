import pandas as pd
import pickle

def load_data(file_path="got_characters.pkl"):
    """
    Load the preprocessed GOT characters DataFrame from pickle.
    """
    df = pd.read_pickle(file_path)
    
    # Standardize some names if needed
    df['character'] = df['character'].str.replace('Jaime','Jamie')
    df['character'] = df['character'].str.replace('Lord Varys','Varys')
    df['character'] = df['character'].str.replace('Bronn','Lord Bronn')
    df['character'] = df['character'].str.replace('Sandor Clegane','The Hound')
    df['character'] = df['character'].str.replace('Robb Stark','Rob Stark')
    
    return df
