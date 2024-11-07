from flask import Flask, Blueprint, redirect, request,render_template,url_for,session,abort,flash, make_response
from models.user import lst_usuarios

login_c=Blueprint('login', __name__)

#LOGIN
@login_c.route('/')
def inicial():
    return render_template('inicial.html')

@login_c.route('/login', methods=['GET','POST'])
def login():
    if request.method =="POST":
        nome = request.form.get("nome")
        senha = request.form.get("senha")
        for usuario in lst_usuarios:
            if usuario.nome == nome and usuario.senha == senha:
                session['name']= usuario.nome
                session['iduser']= usuario.id
                print('oi')
                flash('login realizado com sucesso', 'success')
                return redirect(url_for('login.dash'))
    print('sla')
    return render_template('login.html')
    
@login_c.route('/verifica', methods=['GET','POST'])
def verifica():
    pass
    
@login_c.route('/dash')
def dash():
    return render_template('dash.html')

#MIDDLEWARE
@login_c.before_request
def mid():
    print(4)
    if request.endpoint=='login.login' and 'iduser' in session:
        return redirect(url_for('login.inicial'))
    print(2)
    if request.endpoint in ROTAS_PUBLCAS:
        return 
    print(3)
    if 'iduser' not in session: #verifica se o user ta na sessão
        return redirect(url_for('login.inicial'))
    print('9')
    return#retornar flash mensagem ou pagina de erro (acesso não autorizado, tente fazer login)

ROTAS_PUBLCAS=['login.inicial', 'login.login'] 

@login_c.route('/logout')
def logout():
    session.pop('nome', None)
    session.pop('senha', None)
    return redirect(url_for('login.inicial'))

@login_c.route('/admin')
def admin():
    if session.get("iduser") == '1':
        return render_template('admin.html')
    abort(401)  
    
#BISCOITOS

@login_c.route('/set_cookie')
def set_cookie():
    nome = session.get('name')
    response = make_response('os cookies foram pegos')
    response.set_cookie('name', nome , max_age= 60*60*24)
    return response
