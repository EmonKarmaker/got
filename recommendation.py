import numpy as np

def get_closest_character(df, selected_character):
    """
    Return the most similar character based on t-SNE coordinates (x, y)
    """
    character_id = np.where(df['character'].values == selected_character)[0][0]
    x = df[['x','y']].values
    
    distances = []
    for i in range(len(x)):
        distances.append(np.linalg.norm(x[character_id] - x[i]))
    
    # Skip first (distance 0 to itself)
    recommended_id = sorted(list(enumerate(distances)), key=lambda x: x[1])[1][0]
    return df['character'].values[recommended_id]
