# 1. Нужно реализовать класс Stack со следующими методами:

# 2. Используя стек из задания 1, решите задачу на проверку
# сбалансированности скобок. Сбалансированность скобок означает,
# что каждый открывающий символ имеет соответствующий ему закрывающий,
# и пары скобок правильно вложены друг в друга

from stack import Stack


if __name__ == '__main__':

    # Задание 1
    stack = Stack()
    print('Решение задачи №1\n')

    print('Стек заполнен?', stack.is_empty())
    print('Стек = ', stack.list_stack)

    print('\nЗаносим элемент 59')
    stack.push(59)
    print('Стек = ', stack.list_stack)

    print('\nЗаносим элемент 11')
    stack.push(11)
    print('Стек = ', stack.list_stack)

    print('\nУдаляем 1-й элемент')
    print(stack.pop())
    print('Стек = ', stack.list_stack)

    print('\nВозвращаем 1-й элемент')
    print(stack.peek())
    print('Стек = ', stack.list_stack)

    print('\nДлина стека =', stack.size())



    # Задание 2

    # Экземпляр Класса
    stack_1 = Stack()

    print('\nРешение задачи №2\n')

    while True:
        if stack.is_empty() == False:
            print('Стек пуст, длина =', stack.size())
            break
        stack.pop()

    string = input('\nВведите строку для проверки на сбалансированность:\n')
    # string_1 = '(((([{}]))))'

    if len(string) % 2 == 1:
        print('Несбалансированно')
    else:
        for item in string[::-1]:
            # print(item)
            stack_1.push(item)
            # print(item, "Стека 1")

        print('\nДлина стека =', stack_1.size())
        print('Стек = ', stack_1.list_stack)
        # len_ = stack_1.size()

        sum_balans = 0
        # Предыдущий ключ для проверки на (])[
        key_1 = 0

        while True:
            if stack_1.is_empty() == False:
                break

            elem = stack_1.pop()

            if elem == '(':
                sum_balans += 1
                key = 1
            if elem == ')':
                sum_balans += -1
                key = -1

            if elem == '[':
                sum_balans += 2
                key = 2
            if elem == ']':
                sum_balans += -2
                key = -2

            if elem == '{':
                sum_balans += 3
                key = 3
            if elem == '}':
                sum_balans += -3
                key = -3

            # Проверка на: ( } ) {
            if key_1 != 0:
                if abs(key) != abs(key_1):
                    if (key > 0 and key_1 < 0) or (key < 0 and key_1 > 0):
                        break
            key_1 = key


        if sum_balans == 0:
            print('Сбалансированно')
        else:
            print('Несбалансированно')

