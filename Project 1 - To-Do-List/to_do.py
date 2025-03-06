import sqlite3
from datetime import datetime 

class TaskManager:

    def __init__(self, db_path="tasks.db"):
        self.db_path = db_path
        self.setup_database()

    def setup_database(self):


        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Creates a 'tasks' table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    description TEXT NOT NULL,
                    completed INTEGER,
                    start_time TEXT,
                    end_time TEXT
                )''')
        
            conn.commit()

    def add_task(self, task):
        start_time = datetime.now().isoformat()

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Add New Task in 'tasks' Table
            cursor.execute('''INSERT INTO tasks
                (description, completed, start_time, end_time)
                VALUES (?, ?, ?, ?)''', (
                task, 0, start_time, None))
            
            conn.commit()

    def mark_completed(self, task):

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            # Marks a task as completed based on Task ID
            cursor.execute("UPDATE tasks SET completed = ?, end_time = ? WHERE id = ?", (1, datetime.now().isoformat(), task))

            conn.commit()
            print("Task Mark as Completed.")
        

    def view_task(self):

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM tasks")
            tasks = cursor.fetchall()

            if not tasks:
                print("\nNo Task Found.\n")
                return
            
            print("\n{:<4} | {:<40} | {:<10} | {:<25} | {:<25}".format(
                "ID", "Task", "Status", "Start Time & Date", "End Time & Date"))
            print("-" * 115)

            for task in tasks:
                task_id, description, completed, start_time, end_time = task

                # Checking - Task Status
                status = "Pending"
                if completed == 1:
                    status = "Completed"

                # Checking - If Task Availabel
                if start_time:
                    start_time = start_time[11:19] + " - " + start_time[:10] # Extracts date and time from ISO format
                else:
                    start_time = "Not Available"

                # Checking - If Task Completed
                if not end_time:
                    end_time = "Not Completed"
                else:
                    end_time = end_time[11:19] + " - " + end_time[:10] # Extracts date and time from ISO format

                print(f"{task_id:<4} | {description:<40} | {status:<10} | {start_time:<25} | {end_time:<25}")
            else:
                print()

    def show_pending_task(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM tasks WHERE completed == ?", (0,))
            pending_tasks = cursor.fetchall()

            # Checking - If pending task available
            if not pending_tasks:
                print("\nNo Pending Task Found.")
                return False            
            
            print("\nPending Tasks:")
            for task in pending_tasks:
                pending_task_id, description, _, start_time, _ = task
                start_time = start_time[11:19] + " - " + start_time[:10] # Extracts date and time from ISO format
                
                print(f"{pending_task_id}. {description:<40} | Started Time -> {start_time}")

            return True