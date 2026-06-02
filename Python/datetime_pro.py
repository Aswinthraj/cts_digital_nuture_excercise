from datetime import datetime


class Task:

    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

    def __str__(self):
        return (f"Task: {self.name}, "
                f"Due: {self.due_date.date()}, "
                f"Priority: {self.priority}")


tasks = [
    Task("Project Submission", "2026-06-10", "High"),
    Task("Assignment", "2026-06-05", "Medium"),
    Task("Exam Preparation", "2026-06-15", "High"),
    Task("Lab Record", "2026-05-25", "Low")
]

tasks.sort(key=lambda task: task.due_date)

print("Task Schedule")

for task in tasks:
    print(task)

today = datetime.today()

overdue_tasks = [
    task for task in tasks
    if task.due_date < today
]

print("\nOverdue Tasks")

for task in overdue_tasks:
    print(task)