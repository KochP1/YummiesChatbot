from flask import Blueprint, request, redirect, render_template

chat = Blueprint('chat', __name__, template_folder='templates', static_folder="static")

@chat.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('chat/index.html')