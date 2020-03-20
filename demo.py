import json
import re
from jsonbox import JsonBox

# generate unique box id
MY_BOX_ID = JsonBox.get_new_box_id()

# create instance
jb = JsonBox()

data = [{"name": "first", "age": 25}]

# write data
result = jb.write(data, MY_BOX_ID)

# get record id of written data
record_ids = jb.get_record_id(result)
object_1 = {"ARTEM": "HODUNOV", "age": 25}
object_2 = {"dddddd": "HODUNOV", "age": 25}

jb.update(object_1, MY_BOX_ID, record_id=['5e74d4cb622c0800173390a5'])
jb.update(object_2, MY_BOX_ID, record_id=['5e74d4cb622c0800173390a5'])



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
        try:
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
        Write some inf to json
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
        for every_word in task_name.split(" "):
            if re.match(r'\w', every_word, flags=re.ASCII) is None:
                raise BaseException('Not match reg exp(((')
        else:
            task = Item(task_name, done)
            jb.update({task.name: task.done}, MY_BOX_ID, record_ids[0])
        return

    def remove_Todo(item):
        pass

    def show_Todo(self):
        print(jb.read(MY_BOX_ID))

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
            opt = input('Input option add/show_all/show_undone/make_done/make_undone/exit')
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
