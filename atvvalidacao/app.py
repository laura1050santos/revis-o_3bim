from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    errors = {}
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if len(name) < 3:
            errors['name'] = 'Nome deve ter pelo menos 3 caracteres.'

        if not email or '@' not in email:
            errors['email'] = 'E-mail inválido.'
        if len(password) < 8 or len(password) > 12 or not any(c.isdigit() for c in password) or not any(c.isupper() for c in password) or not any(c in '!@#$%^&*()' for c in password):
            errors['password'] = 'Senha deve ter entre 8 e 12 caracteres, com pelo menos uma letra maiúscula, um número e um caractere especial.'

        if password != confirm_password:
            errors['confirm_password'] = 'Senhas não coincidem.'
        if not errors:
            
            return render_template ('termino.html')
    return render_template('form.html', errors=errors)

if __name__ == '__main__':
    app.run(debug=True)

   