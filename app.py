# rodar no CMD
# pip install flask

from flask import Flask

# Cria uma instância da aplicação Flask
app = Flask(__Name__)
# Estte é um decorador que associa a url
# '/' (a URL raiz do site) à função que vem logo a baixo.
@app.route('/')
# A função que é executada quando a rota '/' é acessada.
# Ela retorna a string "hello world"
def hello_world():
    return 'Hello, world!'
    # executa o servidor de desenvolvimento
    if__name__=='__main__'
    app.run(debug=True)