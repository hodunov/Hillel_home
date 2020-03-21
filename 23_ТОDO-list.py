import re
import json
from termcolor import cprint


class Item:
    def __init__(self, name, done):
        self.name = name
        self.done = done

    def get_display(self):
        return f'{self.name}: {self.done}'


class TodoList:
    def __init__(self, owner_full_name, file_path):
        self.owner_full_name = owner_full_name
        self.file_path = file_path
        try:
            self.tasks = self.get_existing_tasks()
        except (FileExistsError, FileNotFoundError):
            self.tasks = {}

    def get_existing_tasks(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def write_to_file(self):
        with open(self.file_path, 'a+') as file:
            json.dump(self.tasks, file)

    def add_task(self, task_name, done):
        task_name = task_name.lstrip(' ').rstrip(' ')  # убираем пробелы в начале и конце (Если есть)
        for every_word in task_name.split(" "):  # Проверка каждого слова на ASCII
            if re.match(r'\w', every_word, flags=re.ASCII) is None:
                cprint("Input available in English only", color='red')
            else:
                task = Item(task_name, done)
                self.tasks.update({task.name: task.done})

    def show_tasks(self):
        tasks = []
        for k, v in self.tasks.items():
            tasks.append(Item(k, v).get_display())
        cprint(' | '.join(tasks), color='cyan')

    def make_task_done(self, task_name):
        self.tasks[task_name] = True

    def make_task_undone(self, task_name):
        self.tasks[task_name] = False

    def show_undone_tasks(self):
        undone_tasks = []
        for k, v in self.tasks.items():
            if not v:
                undone_tasks.append(Item(k, v).get_display())
        cprint(' | '.join(undone_tasks), color='magenta')

    def start_list(self):
        while True:
            opt = input('Input option add/show_all/show_undone/make_done/make_undone/exit\n')
            if opt == 'exit':
                self.write_to_file()
                break
            elif opt == 'add':
                self.add_task(input('Task_name\n'), bool(input('write smth if done\n')))
            elif opt == 'show_all':
                self.show_tasks()
            elif opt == 'show_undone':
                self.show_undone_tasks()
            elif opt == 'make_done':
                self.make_task_done(input('Task_name\n'))
            elif opt == 'make_undone':
                self.make_task_undone(input('make_undone\n'))


my_task_list = TodoList('Vitalii Fisenko', 'tasks.json')

my_task_list.start_list()
