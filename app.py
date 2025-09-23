# rodar no CMD
# pip install flask

from flask import Flask

app = Flask(__Name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'
return render_template ('index.html')

@app.route ('/login', methods == ['GET','POST'])
def login ():
    error = None
    if request.methods == 'POST':
        username = request.form['username']
        password = request.form['password']
if username == 'admin' and password == 'password'
else:
    error='Você errou suas credenciais meu pitelzinho, meu xuxu.'
    return render_template ('login.html', error=error)

    if__name__=='__main__'
    app.run(debug=True)