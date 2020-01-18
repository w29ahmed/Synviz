from flask import Flask

# Initialize flask app
app = Flask(__name__)

# Homepage URL routing
@app.route('/', methods=['GET'])
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)