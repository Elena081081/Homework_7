import view

string: str = ''
result: int = 0
operator = {'*': lambda x, y: int(x) * int(y),
            '/': lambda x, y: int(x) / int(y) if int(y) != 0 else view.division_by_zero(),
            '+': lambda x, y: int(x) + int(y),
            '-': lambda x, y: int(x) - int(y)}
def string_my_list(string: str):
    string = string.replace(' ', '').strip()
    string = string.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
    my_list = string.split()
    return my_list