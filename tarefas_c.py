from flask import Flask, Blueprint, redirect, request,render_template,url_for,session,abort,flash, make_response
from model.tarefas_m import lst_tarefa
tarefas_c=Blueprint('tarefas', __name__)
lst=[]
@tarefas_c.route('/add')
def add():
    if request.method =="POST":
        novaTarefa = request.form.get("novaTarefa")
        desc = request.form.get("desc")
        data = request.form.get("data")
        tarefas ={
            "Nome": novaTarefa,
            "decricao":desc,
            "data":data
        }
        lst.append(tarefas)
        session['lstTarefa']=lst
        flash('tarefa feita com sucesso', 'success')
        return render_template('form.html')
    return render_template('form.html')

@tarefas_c.route('/logout')
def logout():
    session.pop('lstTarefa', None)
    lst.clear
    return redirect(url_for('login.inicial'))

