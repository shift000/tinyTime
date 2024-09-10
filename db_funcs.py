from tinydb import TinyDB, Query
from datetime import datetime
import os

def out(msg, title=""):
    print(f'{title}:: {msg}')

# Pfad zur TinyDB-Datenbank
DB_PATH = 'data/tinydb.json'

def initialize_db():
    if not os.path.exists('./data'):
        os.mkdir('./data')
    """Initialisiert die TinyDB-Datenbank und erstellt notwendige Tabellen."""
    db = TinyDB(DB_PATH)
    # Hier werden die Tabellen erstellt, wenn sie nicht existieren
    db.table('tasks').all()
    db.table('projects').all()
    db.table('time_entries').all()  # Stelle sicher, dass die Tabelle existiert
    db.close()

def add_time_entry(entry):
    """Fügt einen neuen Eintrag zur Datenbank hinzu."""
    db = TinyDB(DB_PATH)
    
    out(f"Füge {entry} hinzu", "add_time")
    db.table('time_entries').insert(entry)
    db.close()
    
def add_task(task_name):
    """Fügt eine neue Aufgabe (Tätigkeit) zur Datenbank hinzu, wenn sie nicht existiert."""
    db = TinyDB(DB_PATH)
    table = db.table('tasks')
    
    out(f"Füge {task_name} hinzu", "add_tasks")
    if not table.search(Query().name == task_name):
        table.insert({'name': task_name})
    db.close()

def add_project(project_name):
    """Fügt ein neues Projekt zur Datenbank hinzu, wenn es nicht existiert."""
    db = TinyDB(DB_PATH)
    table = db.table('projects')
    
    out(f"Füge {project_name} hinzu", "add_projects")
    if not table.search(Query().name == project_name):
        table.insert({'name': project_name})
    db.close()

def get_time_entries():
    """Liest alle Zeiteinträge aus der Datenbank."""
    db = TinyDB(DB_PATH)
    entries = db.table('time_entries').all()
    
    out(f"Hole {entries}", "get_entries")
    db.close()
    return entries

def get_tasks():
    """Holt alle Aufgaben (Tätigkeiten) aus der Datenbank."""
    db = TinyDB(DB_PATH)
    tasks = db.table('tasks').all()
    
    out(f"Hole {tasks}", "get_tasks")
    task_names = [task['name'] for task in tasks]
    db.close()
    return task_names

def get_projects():
    """Holt alle Projekte aus der Datenbank."""
    db = TinyDB(DB_PATH)
    projects = db.table('projects').all()
    
    out(f"Hole {projects}", "get_projects")
    project_names = [project['name'] for project in projects]
    db.close()
    return project_names

def delete_time_entry(entry_id):
    """Löscht einen Zeiteintrag anhand der ID."""
    db = TinyDB(DB_PATH)
    db.table('time_entries').remove(doc_ids=[entry_id])
    db.close()
