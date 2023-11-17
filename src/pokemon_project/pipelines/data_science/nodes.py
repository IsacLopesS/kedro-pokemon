"""
This is a boilerplate pipeline 'data_science'
generated using Kedro 0.18.14
"""
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

def split_data(df, test_size=0.3, random_state=9999):
    
    #split train test
    X = df.drop('type1', axis=1)
    y = df.type1

    X_train,X_test,y_train,y_test = train_test_split(
        X,y, test_size=0.3, random_state=9999)#stratify=y
    
    return X_train,X_test,y_train,y_test

def fit_model(X_train,X_test,y_train,y_test):
    
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(X_train,y_train)
    
    # predicts test set
    y_pred = classifier.predict(X_test)
    
    # Report score
    score = accuracy_score(y_test,y_pred)
    print(score)
    return classifier