"""
This is a boilerplate pipeline 'pre_processing'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from pokemon_project.pipelines.pre_processing.nodes import preprocess_pokemon

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                func=preprocess_pokemon,#nome da função
                inputs=["raw_pokemon_dataset", "params:selected_generation"], #inputs da função: qualquer item de catalog.list() está acessível
                outputs="preprocessed_pokemon", #nome atribuído ao output da função. 					
                name="preprocess_pokemon_node" #nome do nó
            )
    ])
