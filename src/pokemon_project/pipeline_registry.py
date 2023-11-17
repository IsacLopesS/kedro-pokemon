"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline



def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    #pipelines = find_pipelines()
    #pipelines["__default__"] = sum(pipelines.values())

    from pokemon_project.pipelines import pre_processing as pp
    from pokemon_project.pipelines import data_engineering as de
    
    pre_processing_pipeline = pp.create_pipeline()
    data_engineering = de.create_pipeline()

    return {'pp': pre_processing_pipeline,
            'de': data_engineering,
            'pp_e_de':(pre_processing_pipeline + data_engineering),
            "__default__": pre_processing_pipeline 
            }
