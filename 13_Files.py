"""
Создать файл, в нем написать текст.
Считать данные с файла и вывести в консоль
Считать данные с этого же файла и записать в новый файл
Считать данные с этого же файла, преобразовать (любые операции) и
записать в этот же файл с разделителем в 2 отступа "\n"
"""


def open_txt(txt):
    with open(txt, 'r') as f3:
        print(f3.read())


def write_out_txt(txt_from, txt_to):
    with open(txt_from, 'r') as f, open(txt_to, 'w') as f1:
        for line in f:
            f1.write(line)


def add_str_txt(txt):
    with open(txt, "a+") as f4:
        for i in range(1, 4, 1):
            f4.write(f"\n This is append line {i}\n")


open_txt('text.txt')
write_out_txt('text.txt', 'text_out.txt')
add_str_txt('text_out.txt')
