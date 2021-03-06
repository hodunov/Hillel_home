var1 = ' Python programming language '
print(len(var1))  # Длина строки
print(var1.isalpha())  # Состоит ли строка из букв
print(var1.islower())  # Состоит ли строка из символов в нижнем регистре
print(var1.isupper())  # Состоит ли строка из символов в верхнем регистре
print(var1.isdigit())  # Состоит ли строка из цифр
print(var1.isnumeric())  # Все символы строки числовые
print(var1.startswith('Python'))  # Начинается ли строка с шаблона
print(var1.endswith('language'))  # Заканчивается ли строка с шаблона
print(var1.lower())  # Состоит ли строка из символов в нижнем регистре
print(var1.upper())  # Преобразование строки к верхнему регистру
print(var1.title())  # Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
print(var1.capitalize())  # Переводит первый символ строки в верхний регистр, а все остальные в нижний
print(var1.lstrip())  # Удаление пробельных символов в начале строки
print(var1.rstrip())  # Удаление пробельных символов в конце строки
print(var1.strip())  # Удаление пробельных символов в начале и в конце строки
print(var1.ljust(50, '_'))  # Делает длину строки не меньшей width, по необходимости заполняя последние символы
print(var1.rjust(50, '_'))  # Делает длину строки не меньшей width, по необходимости заполняя первые символы
print(var1.center(50, '_'))  # Возвращает отцентрованную строку заполняя края
print(var1.find('programming'))  # Поиск подстроки в строке
print(var1.replace('Python', 'Python3'))  # Замена шаблона
print(var1.split('programming'))  # Разбиение строки по разделителю
print(var1.join('TEST'))  # Сборка строки из списка с разделителем
