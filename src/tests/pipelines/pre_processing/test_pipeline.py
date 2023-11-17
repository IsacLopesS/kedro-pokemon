"""
This is a boilerplate test file for pipeline 'pre_processing'
generated using Kedro 0.18.14.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

import pandas as pd
from pokemon_project.pipelines.pre_processing.nodes import preprocess_pokemon

def test_preprocessing_expectations():
    test_dataset = pd.DataFrame({
        "name":["Charmander", "Bulbasaur", None],
        "generation": [1,2,3],
        "pokedex_number": [1,2,3],
        "type2": [True,False,True]
    })

    output = preprocess_pokemon(test_dataset, selected_generation=[1])
    print("AQUIIIIIIIIIIII-----> ",output)
    assert output.equals(
        pd.DataFrame({
            "name": ["Charmander"],
            "generation": 1
        })
    )