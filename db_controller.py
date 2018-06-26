import sqlite3
from datetime import datetime

class DbController:
    """Allows user to update task and projects in database"""
    def __init__(self, db_name):
        self.db_name = db_name           

    def query(self, sql, data):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA Foreign_Keys = ON")
            cursor.execute(sql, data)
            db.commit()

    def select_query(self,sql,data=None):
        with sqlite3.connect(self.db_name) as db:
            cursor = db.cursor()
            cursor.execute("PRAGMA foreign_keys = ON")
            if data:
                cursor.execute(sql,data)
            else:
                cursor.execute(sql)
            results = cursor.fetchall()
        return results

    def add_task(self, description, deadline, project_id):
        created = datetime.now()
        sql_add_task =  "INSERT INTO Tasks (Description, Deadline, Created, ProjectID) VALUES (?,?,?,?)"
        self.query(sql_add_task, (description, deadline, created, project_id))

    def add_project(self, description, deadline):
        created = datetime.now()
        sql_add_project =  "INSERT INTO Projects (Description, Deadline, Created) VALUES (?,?,?)"
        self.query(sql_add_project, (description, deadline, created))

    def delete_task(self, task_id):
        self.query("DELETE FROM Tasks WHERE TaskID = ?", (task_id,))

    def delete_project_only(self, project_id):
        self.query("UPDATE Tasks SET ProjectID = NULL WHERE ProjectID = ?", (project_id,))
        self.query("DELETE FROM Projects WHERE ProjectID = ?", (project_id,))

    def delete_project_and_tasks(self, project_id):
        self.query("DELETE FROM Tasks WHERE ProjectID = ?", (project_id,))
        self.query("DELETE FROM Projects WHERE ProjectID = ?", (project_id,))

    def mark_task_completed(self, task_id):
        completed = datetime.now()
        sql_mark_completed =  "UPDATE Tasks SET Completed = ? WHERE TaskID = ?"
        self.query(sql_mark_completed, (completed, task_id))

    def mark_project_completed(self, project_id):
        completed = datetime.now()
        sql_mark_completed =  "UPDATE Projects SET Completed = ? WHERE ProjectID = ?"
        self.query(sql_mark_completed, (completed, project_id))

    def mark_project_tasks_completed(self, project_id):
        completed = datetime.now()
        sql_mark_completed =  "UPDATE Tasks SET Completed = ? WHERE ProjectID = ?"
        self.query(sql_mark_completed, (completed, project_id))

    def get_task_project_id(self, task_id):
        sql_get_project_id = "SELECT ProjectID FROM Tasks WHERE TaskID = ?"
        results = self.select_query(sql_get_project_id, (task_id,))
        return results[0][0]

    def check_project_completed(self, project_id):
        sql_check_project = "SELECT TaskID FROM Tasks WHERE ProjectID = ? AND Completed IS NULL"
        results = self.select_query(sql_check_project, (project_id,))
        if not results:
            return True
        return False
        
    def edit_task_description(self, task_id, description):
        sql_edit_descr = "UPDATE Tasks SET Description = ? WHERE TaskID = ?"
        self.query(sql_edit_descr, (description, task_id))

    def set_task_deadline(self, task_id, deadline):
        sql_set_deadline = "UPDATE Tasks SET Deadline = ? WHERE TaskID = ?"
        self.query(sql_set_deadline, (deadline, task_id))

    def assign_task_to_project(self, task_id, project_id):
        sql_assign_task = "UPDATE Tasks SET ProjectID = ? WHERE TaskID = ?"
        self.query(sql_assign_task, (project_id, task_id))

    def set_project_deadline(self, project_id, deadline):
        sql_set_deadline = "UPDATE Project SET Deadline = ? WHERE ProjectID = ?"
        self.query(sql_set_deadline, (deadline, project_id))

    def edit_project_description(self, project_id, description):
        sql_edit_descr = "UPDATE Projects SET Description = ? WHERE ProjectID = ?"
        self.query(sql_edit_descr, (description, project_id))

    def show_all_tasks(self):
        results = self.select_query("SELECT * FROM Tasks")
        return results

    def show_active_tasks(self):
        results = self.select_query("SELECT * FROM Tasks WHERE Completed IS NULL")
        return results

    def show_completed_tasks(self):
        results = self.select_query("SELECT * FROM Tasks WHERE Completed IS NOT NULL")
        return results

    def show_all_projects(self):
        results = self.select_query("SELECT * FROM Projects")
        return results

    def show_active_projects(self):
        results = self.select_query("SELECT * FROM Projects WHERE Completed IS NULL")
        return results

    def show_completed_projects(self):
        results = self.select_query("SELECT * FROM Projects WHERE Completed IS NOT NULL")
        return results
       
    def show_single_project(self, project_id):
        results = self.select_query("SELECT * FROM Projects WHERE ProjectID = ?", (project_id,))
        return results

    def show_project_tasks(self, project_id):
        results = self.select_query("SELECT * FROM Tasks WHERE ProjectID = ?", (project_id,))
        return results






