"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from pokemon_project.pipelines.data_engineering.nodes import encode_target_variable
from pokemon_project.pipelines.data_engineering.nodes import create_number_of_abilities_feature


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
                func=encode_target_variable,
                inputs="pp_pokemon_dataset", 
                outputs=[
                    "encoded_pokemon_dataset", 
                    "label_encoder"],  					
                name="encoding_target_variable_node" 
            ),
        node(
                func=create_number_of_abilities_feature,
                inputs="pp_pokemon_dataset", 
                outputs="pokemon_features", 		
                name="pokemon_features_node" 
            )
    ])





