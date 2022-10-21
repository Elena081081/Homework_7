import model, view

def operation(my_list, i, oper):
    if my_list[i] == oper:
        my_list[i-1] = model.operator.get(oper)(int(my_list[i-1]), int(my_list[i+1]))
        delete_item(my_list, i)
        return True
    return False
def delete_item(string, i):
    string.pop(i)
    string.pop(i)
def calculate(my_list: list):
    while len(my_list) > 1:
        if '*' in my_list or '/' in my_list:
            for i in range(len(my_list)):
                if operation(my_list, i, '*'): break
                if operation(my_list, i, '/'): break
        elif '+' in my_list or '-' in my_list:
            for i in range(len(my_list)):
                if operation(my_list, i, '+'): break
                if operation(my_list, i, '-'): break
    return my_list
def result_expression(expression: str):
    expression = model.string_my_list(expression)
    while len(expression) > 1:
        expression = calculate(expression)
    model.result = expression[0]
    view.print_result()


