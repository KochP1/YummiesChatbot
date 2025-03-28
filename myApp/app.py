from flask import Flask
import os
import google.generativeai as genai

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
    genai.configure(api_key=os.getenv('API_KEY'))


    # Importar y registrar blueprints
    from myApp.blueprints.chat.routes import chat
    app.register_blueprint(chat, url_prefix='/')


    return app