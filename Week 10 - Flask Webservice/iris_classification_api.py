"""
To run this app, in your terminal:
> python iris_classification_api.py
"""
import connexion
from sklearn.externals import joblib

# Instantiate our Flask app object
app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app

# Load our pre-trained model
clf = joblib.load('./model/iris_classifier.joblib')

# Implement a simple health check function (GET)
def health():
    # Test to make sure our service is actually healthy
    try:
        predict(1, 1, 1, 1)
    except:
        return {"Message": "Service is unhealthy"}, 500

    return {"Message": "Service is OK"}

# Implement our predict function
def predict(sepal_length, sepal_width, petal_length, petal_width):
    # Accept the feature values provided as part of our POST
    # Use these as input to clf.predict()
    prediction = clf.predict([[sepal_length, sepal_width, petal_length, petal_width]])

    # Map the predicted value to an actual class
    if prediction[0] == 0:
        predicted_class = "Iris-Setosa"
    elif prediction[0] == 1:
        predicted_class = "Iris-Versicolour"
    else:
        predicted_class = "Iris-Virginica"

    # Return the prediction as a json
    return {"prediction" : predicted_class}

# Read the API definition for our service from the yaml file
app.add_api("iris_classification_api.yaml")

# Start the app
if __name__ == "__main__":
    app.run()
