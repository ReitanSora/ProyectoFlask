from flask import Blueprint, render_template

main = Blueprint('home_blueprint', __name__)

@main.route('/')
def home():
    return render_template('index.html')