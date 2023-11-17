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

    from pokemon_project.pipelines import pre_processing
    pre_processing_pipeline = pre_processing.create_pipeline()


    return {'pp': pre_processing_pipeline,
            "__default__": pre_processing_pipeline}
