import numpy as np
def recommend_character(selected_character,df):
    """find the closesr matching character"""
    x=df[['x','y']].values
    character_id=np.where(df['character'].values==selected_character)[0][0]
    distances=[np.linalg.norm(x[character_id]-x[i]) for i in range(len(x))]
    recommended_id=sorted(list(enumerate(distances)),key=lambda x:x[1])[1][0]
    return df['character'].values[recommended_id]