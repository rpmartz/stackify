from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/stack', methods=['POST'])
def build_stack():
    pass

@app.route('/your-stack')
def display_stack():
    pass