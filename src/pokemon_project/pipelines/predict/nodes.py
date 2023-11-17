"""
This is a boilerplate pipeline 'predict'
generated using Kedro 0.18.14
"""

def batch_predict(model_artifact, dataset, encoder):
    '''This function takes a pre-trained model 
       and predicts an unknown dataset'''
    predictions = model_artifact.predict(dataset)

    #Inverse transform predictions
    predictions_string = encoder.inverse_transform(predictions)

    final_predictions = dataset
    final_predictions['type1'] = predictions_string
    return final_predictions