"""
Создать файл, в нем написать текст.
Считать данные с файла и вывести в консоль
Считать данные с этого же файла и записать в новый файл
Считать данные с этого же файла, преобразовать (любые операции) и
записать в этот же файл с разделителем в 2 отступа "\n"
"""

with open("text.txt") as f:
    with open('text.txt', 'r') as f3:
        print(f3.read())
    f3.close()
    with open("text_out.txt", "w") as f1:
        for line in f:
            f1.write(line)
        f1.close()
    with open("text_out.txt", "a+") as f4:
        for i in range(1, 3, 1):
            f4.write(f"Append line {i}\n")

with open('test.txt', 'r') as file_to_read, open('test_2.txt', 'w') as file_to_write:
    text = file_to_read.read()
    file_to_write.write(text)
    new_line = f'\n \n \n New line\n New second line'
    file_to_write.write(new_line)
    for item in text:
        file_to_write.write(item + '\n \n')
