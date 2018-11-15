"""
To run this app, in your terminal:
> python connexion_demo.py
"""

import connexion

# Instantiate our Flask app object
app = connexion.FlaskApp(__name__, port=8080, specification_dir='swagger/')
application = app.app

# Implement a simple health check function (GET)
def health():
    # Test to make sure our service is actually healthy
    if multiply(2, 1) == {"product" : 2}:
        return {"Message": "Service is OK"}
    else:
        return {"Message": "Service is crazy and can't perform multiplications"}, 500

# Implement our multiplication function (POST)
def multiply(multiplicand, multiplier):
    product = multiplier * multiplicand
    return {"product" : product}

# Read the API definition for our service from the yaml file
app.add_api("demo_api.yaml")

# Start the app
if __name__ == "__main__":
    app.run()
