import sqlite3

def create_new_db(db_name):
    """Sets up tables for new database"""
    
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()

        #create tasks table
        cursor.execute("""CREATE TABLE Tasks(
            TaskID integer,
            Description text,
            Deadline date,
            Created timestamp,
            Completed timestamp,
            ProjectID integer,
            PRIMARY KEY(TaskID),
            FOREIGN KEY(ProjectID) REFERENCES Projects(ProjectID));""")
        
        #create project table
        cursor.execute("""CREATE TABLE Projects(
            ProjectID integer,
            Description text,
            Deadline date,
            Created timestamp,
            Completed timestamp,
            PRIMARY KEY(ProjectID));""")
        
        db.commit()



        