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


def remove_non_letters(stack_name):
    letters = [letter.upper() for letter in stack_name if letter.isalpha()]
    return ''.join(letters)
