"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder
import ast

def encode_target_variable(df):
    label_encoder = LabelEncoder()
    df['type1'] = label_encoder.fit_transform(df.type1)
    return df, label_encoder


def calculate_number_of_abilities(df): 
        ''' helper function for determining pokemon's number of abilities '''

        abilities = ast.literal_eval(df['abilities'])
        return len(abilities)

def create_number_of_abilities_feature(df):
    """add abilitie feature column to dataframe"""
    df2 = df.assign(
        number_of_abilities=df.apply(
            calculate_number_of_abilities,
            axis=1
        )
    )
    return df2