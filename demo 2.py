
with open("text.txt") as f:
    with open('text.txt', 'r') as f3:
        print(f3.read())
    with open("text_out.txt", "w") as f1:
        for line in f:
            f1.write(line)
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
