from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the route for the root URL
@app.route("/")
def hello():
    return "Hello Flask!"

# Run the app
if __name__ == "__main__":
    app.run(port=8080)
