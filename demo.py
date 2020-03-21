import json
import re
from jsonbox import JsonBox
from termcolor import cprint

# generate unique box id
MY_BOX_ID = JsonBox.get_new_box_id()

# create instance
jb = JsonBox()

data = [
    {"Task ": True}
]

# write data
result = jb.write(data, MY_BOX_ID)

# get record id of written data
record_ids = jb.get_record_id(result)


class Item:
    """
    Class for contain some information
    """

    def __init__(self, name, done):
        self.name = name
        self.done = done

    def get_display(self):
        return f'{self.name}: {self.done}'


class TodoMain:
    """
    Main logic
    """

    def __init__(self, owner_full_name, file_path):
        self.owner_full_name = owner_full_name
        self.file_path = file_path
        try:  # не уверен, это нужно или нет
            self.tasks = self.get_existing_tasks()
        except (FileExistsError, FileNotFoundError):
            self.tasks = {}

    def get_existing_tasks(self):
        """
        Get existing task from json file
        :return: json file
        """
        return jb.read(MY_BOX_ID)

    def write_to_file(self):
        """
        Write something to json
        :return: json
        """
        with open(self.file_path, 'a+') as file:
            jb.write(self.tasks, file)

    def add_Todo(self, task_name, done):
        """
        Add new task
        :param task_name:
        :param done:
        :return:
        """
        task_name = task_name.lstrip(' ').rstrip(' ') # убираем пробелы в начале и конце (Если есть)
        for every_word in task_name.split(" "):  # Проверка каждого слова на ASCII
            if re.match(r'\w', every_word, flags=re.ASCII) is None:
                return cprint("Input available in English only", color='red')
            return jb.write({task_name: done}, MY_BOX_ID)

    def remove_Todo(self):
        pass

    def show_Todo(self):
        print(type(jb.read(MY_BOX_ID)))
        print(type(MY_BOX_ID))
        print(MY_BOX_ID)

    def make_task_done(self, task_name):
        self.tasks[task_name] = True

    def make_task_undone(self, task_name):
        self.tasks[task_name] = False

    def show_undone_tasks(self):
        undone_tasks = []
        for k, v in self.tasks.items():
            if not v:
                undone_tasks.append(Item(k, v).get_display())
        print(' | '.join(undone_tasks))

    def start_list(self):
        while True:
            opt = input('Input option add/show_all/show_undone/make_done/make_undone/exit\n')
            if opt == 'exit':
                self.write_to_file()
                break
            elif opt == 'add':
                self.add_Todo(input('Task_name '), bool(input('write smth if done ')))
            elif opt == 'show_all':
                self.show_Todo()
            elif opt == 'show_undone':
                self.show_undone_tasks()
            elif opt == 'make_done ':
                self.make_task_done(input('Task_name'))
            elif opt == 'make_undone ':
                self.make_task_undone(input('make_undone '))


my_task_list = TodoMain('Vitalii Fisenko', 'tasks.json')

my_task_list.start_list()
