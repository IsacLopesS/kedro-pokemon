"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.14
"""

from kedro.pipeline import Pipeline, pipeline, node
from pokemon_project.pipelines.predict.nodes import batch_predict

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=batch_predict,
            inputs=['model_classifier','X_test','label_encoder'],
            outputs= 'predictions',
            name="batch_predict_node"
        )
    ])
