import pandas

# Titanic dataset: https://www.kaggle.com/c/titanic/data
data = pandas.read_csv("titanic_train.csv")

'''
Explore this data set:
	data.head()
	data.shape
	data.columns
	data[0:5]
'''

# Predict survival based on age, number of siblings on board, and fare
y = data['Survived']
X = data[['Age','SibSp','Fare']].fillna(0)

from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
lr = LogisticRegression()
lr.fit(X_train, y_train)
print("Accuracy of logistic regression (skilearn):",
	accuracy_score(lr.predict(X_test), y_test))


## Using statsmodels
print("\nNow we will use statsmodels to do logistic regression.\n")
import statsmodels.formula.api as smf
Xy_train = pandas.DataFrame.join(X_train, y_train)
model = smf.logit(formula='Survived ~ Age + SibSp + Fare', data=Xy_train)
result = model.fit()
print(result.summary())
predicted = result.predict(X_test)
print("Predicted probabilities", predicted)
print("\n\nAccuracy based on predicted probabilities:",
	accuracy_score([ 1 if p > 0.5 else 0 for p in predicted ], y_test))
