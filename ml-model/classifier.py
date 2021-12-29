import pandas as pd
import numpy as np

df = pd.read_csv('iris.csv')

X = df.iloc[:, :-1]
y = df['class']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""# Logistic Regression"""

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
cm = confusion_matrix(np.array(y_test).reshape(-1, 1), y_pred)

print('Confusion Matrix:')
cm

print('Accuracy: ' + str((cm[0, 0] + cm[1, 1] + cm[2, 2]) / y_test.shape[0]))

# Once we have a well trained model, we can serialize it to be unserialized by the endpoint
from joblib import dump

dump(sc, '../endpoint/predictor/standard_scaler.joblib')
dump(classifier, '../endpoint/predictor/classifier.joblib')