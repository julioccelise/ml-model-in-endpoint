# ml-model-in-endpoint
You can find more details about this project in https://devtods.com/how-to-create-an-endpoint-with-a-machine-learning-model---the-basic-way/

For this tutorial, we'll create an endpoint that will can predict type of iris plant based on the sepal and petal measures (yes, the classic iris problem with the classic [iris dataset](https://archive.ics.uci.edu/ml/datasets/iris)). You'll need Python for sure. I'll be using [scikit-learn](https://scikit-learn.org/) as machine learning library and [Flask](https://flask.palletsprojects.com/en/2.0.x/) as the web server. You can use the libraries of your choice ([TensorFlow](https://www.tensorflow.org/), [PyTorch](https://pytorch.org/), [Django](https://www.djangoproject.com/)...) since this post focuses on how to deploy the trained model.

## Requirements
You'll need:

`python >= 3.8`

### Installing required libraries
`pip install -r requirements.txt`

## Starting the endpoint
In your terminal/command line, navigate to the [endpoint](endpoint/) folder and [configure the Flask application](https://flask.palletsprojects.com/en/2.0.x/quickstart/):

### For Mac and Linux
```
$ export FLASK_APP=app
$ export FLASK_ENV=development
```
### For Windows
```
> set FLASK_APP=app
> set FLASK_ENV=development
```
After that, just execute the app:

`flask run`

The endpoint should start runnning in your local envionment.

## Calling the endpoint
You can call the endpoint in way you like, for example using [Postman](https://www.postman.com/) or your custom code. If you dom't have any, I've included a small tester of the endpoint.

In your terminal/command line, navigate to the [endpoint](endpoint/) folder and run:

`python endpoint_tester.py`

**Please share this repo if you find it useful or feel free to comment here or in the [blog post](https://devtods.com/how-to-create-an-endpoint-with-a-machine-learning-model---the-basic-way/) if you have any suggestion to improve my ideas.**
