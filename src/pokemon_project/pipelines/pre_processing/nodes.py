"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.14
"""
import pandas as pd

def preprocess_pokemon(df: pd.DataFrame, selected_generation=[1]):
    ''' This function cleans the pokemon raw data, removing NAs and unused columns'''
    # removing unused columns
    df = df.drop(columns = ['type2','pokedex_number'])
    
    # removing Null values
    df = df.dropna() 
    
    # select generation
    df  = df.loc[df.generation.isin(selected_generation)]
    return df