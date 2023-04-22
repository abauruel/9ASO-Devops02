import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    title = 'Laboratório Pipeline DevOps ' + os.getenv('ENV_NAME','') + ' vFinal'
    return title


if __name__ == '__main__':
    app.run()