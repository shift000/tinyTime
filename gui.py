import csv
from io import StringIO
from flask import Flask, render_template, request, redirect, url_for, jsonify, Response
from db_funcs import add_time_entry, get_time_entries, get_tasks, get_projects

app = Flask(__name__)

@app.route('/')
def index():
    entries = get_time_entries()
    return render_template('index.html', entries=entries)

@app.route('/track')
def track():
    tasks = get_tasks()  # Holt eine Liste vorhandener Aufgaben aus der Datenbank
    projects = get_projects()  # Holt eine Liste vorhandener Projekte aus der Datenbank
    
    print(tasks)
    return render_template('track.html', tasks=tasks, projects=projects)

@app.route('/add_entry', methods=['POST'])
def add_entry():
    data = request.json
    task = data.get('task')
    project = data.get('project')
    duration = data.get('duration')
    start_time = data.get('start_time')
    end_time = data.get('end_time')
    date = data.get('date')
    add_time_entry({
        'task': task,
        'project': project,
        'duration': duration,
        'start_time': start_time,
        'end_time': end_time,
        'date': date
    })
    return jsonify({'status': 'success', 'task': task, 'project': project, 'duration': duration})

@app.route('/export_csv')
def export_csv():
    entries = get_time_entries()
    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['Task', 'Project', 'Duration', 'Start Time', 'End Time', 'Date'])
    
    for entry in entries:
        writer.writerow([
            entry.get('task'),
            entry.get('project'),
            entry.get('duration'),
            entry.get('start_time'),
            entry.get('end_time'),
            entry.get('date')
        ])
    
    output.seek(0)
    return Response(
        output,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=time_entries.csv"}
    )

def start_gui():
    app.run(debug=True)
