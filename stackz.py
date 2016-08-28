from flask import Flask
from flask import render_template, request

from stackbuilder import get_stack_for_letter

app = Flask(__name__, static_url_path = "", static_folder = "tmp")

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/stack', methods=['POST'])
def build_stack():
    submitted_stack_name = request.form['stackName']
    stack_name_letters = remove_non_letters(submitted_stack_name)
    stack = [get_stack_for_letter(l) for l in stack_name_letters]

    stack_name = ''.join(stack_name_letters)
    return render_template('stack.html', stack=stack, stack_name=stack_name)


@app.route('/your-stack')
def display_stack():
    return render_template('stack.html')


def remove_non_letters(stack_name):
    return [letter.upper() for letter in stack_name if letter.isalpha()]
