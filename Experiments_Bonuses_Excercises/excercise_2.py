user_prompt = "Enter a todo:"

todos = []

while True:
    user_prompt = "Enter a todo:"
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
