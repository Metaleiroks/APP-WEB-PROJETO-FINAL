import os
import requests
import base64
from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)

usuario = "senai"
senha = "senai123"


app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


@app.route('/alunos', methods=['Get','POST'])  
def alunos():

    if request.method == 'POST':  
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        cpf = request.form.get('cpf')
        

        api_url = "https://projeto-final-icec.onrender.com/alunos/"


        payload = {
            "id": 0,
            "nome": nome,
            "idade": int(idade),
            "cpf": cpf
        }

        response = requests.post(api_url, json=payload)
        print(response.json)
        
        return render_template('aluno.html')
    else:
        return render_template('aluno.html')

if __name__ == '__main__':
   app.run()
