# Задание №1: Стек
class Stack:
    def __init__(self):
        self.item = []


    def __str__(self):
        return str(" ; ".join(self.item))

    def add(self, element):
        self.item.append(element)

    def pop(self):
        if len(self.item) == 0:
            return None
        return self.item.pop()


class TaskManager:
    def __init__(self):
        self.task = dict()

    def __str__(self):
        string = ""
        for element in sorted(self.task.keys()):
            string += str(element) + ": " + str(self.task[element]) + ";\n"
        return string

    def new_task(self, task, priority):
        if not priority in self.task.keys():
            self.task[priority] = Stack()
            self.task[priority].add(task)

        else:
            new_stack = Stack()
            while len(str(self.task[priority])) != 0:
                value = self.task[priority].pop()
                if value != task:
                    new_stack.add(value)
            new_stack.add(task)
            self.task[priority] = new_stack

    def delete_task(self, priority):
        if not priority in self.task.keys():
            print("С заданным приоритетом задача отсутствует ")
        else:
            print(f"Задача: '{self.task[priority].pop()}' - была удалена")
            if len(str(self.task[priority])) == 0:
                self.task.pop(priority)

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)


manager.new_task("помыть посуду", 4)
manager.delete_task(4)
manager.delete_task(2)
print(manager)


