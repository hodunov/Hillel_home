prompt_text = "Enter a number: "
user_num = 0 # default value
try:
    user_num = int(input(prompt_text))
except ValueError:
    print("Error")
print(user_num)