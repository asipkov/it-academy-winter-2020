# Оформите решение задач из прошлых домашних
# работ в функции. Напишите функцию runner.
import tasks_functions


def runner(*args):
    list_func = []
    if not args:
        for func in dir(tasks_functions):
            if '__' not in func:
                list_func.append(func)
        for el in list_func:
            print('Result', el, ':', )
            getattr(tasks_functions, el)()
    else:
        for func in args:
            print('Result', func, ':', )
            getattr(tasks_functions, func)()


runner()
runner('search_nod', 'order_list')