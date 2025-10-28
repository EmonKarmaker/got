import pickle
import pandas as pd

def load_data(filepath='data.pkl'):
    """Load and clean Game of Thrones dataset"""
    df = pickle.load(open(filepath, 'rb'))
    df = df.head(25)
    df['character'] = df['character'].replace({
        'Jaime': 'Jamie',
        'Lord Varys': 'Varys',
        'Bronn': 'Lord Bronn',
        'Sandor Clegane': 'The Hound',
        'Robb Stark': 'Rob Stark'
    })
    return df
