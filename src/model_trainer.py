from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def treinar_modelo(X, y):
    """
    Treina um modelo RandomForest com dados de entrada X e y.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    return clf, X_test, y_test
