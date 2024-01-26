from flask import render_template, request, redirect, url_for
from app import app
from app.models import Task

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = Task(content=request.form['content'])
        task.save()
        return redirect(url_for('index'))
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/delete/<id>')
def delete(id):
    task = Task.query.get(id)
    if task:
        task.delete()
    return redirect(url_for('index'))

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id):
    task = Task.query.get(id)
    if request.method == 'POST':
        task.content = request.form['content']
        task.save()
        return redirect(url_for('index'))
    return render_template('update.html', task=task)