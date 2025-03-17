from collections import deque

class TaskManager:
    def __init__(self):
        self.task_log = []
        self.task_stack = []
        self.task_queue = deque()

    def log_task(self, task):
        """Logs a task in the task log and adds to stack & queue."""
        self.task_log.append(task)
        self.task_stack.append(task)
        self.task_queue.append(task)
        print(f"Task Logged: {task}")

    def undo_last_task(self):
        """Undoes the last task using stack (LIFO)."""
        if self.task_stack:
            last_task = self.task_stack.pop()
            print(f"Undoing last task: {last_task}")
        else:
            print("No tasks to undo.")

    def show_logs(self):
        """Displays all logged tasks."""
        return self.task_log
