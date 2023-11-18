class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        if item in self.stack:
            self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


class TaskManager:
    def __init__(self):
        self.tasks = Stack()

    def new_task(self, task, priority):
        self.tasks.push((priority, task))

    def __str__(self):
        sorted_tasks = sorted(self.tasks.stack)
        dic = {priority: [x[1] for x in sorted_tasks if x[0] == priority] for priority, task in sorted_tasks}
        string = ""

        for priority, task in dic.items():
            string += f"{priority} - {', '.join(task)}\n"

        return string


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)

print(manager)
