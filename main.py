# список книг - словарь: ключ название, автор значение - {назв книги: автор}
# список читателей - {имя: {назв книги: автор}}
# функция которая выводит инфу о книгах которые есть и о читателях
# функция, которая регистрирует читателя и выдает книгу
# функция, которая возвращает книгу
# функция менеджер, которая расперделяет вызов других функций и задает вопрос взять или вернуть

books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Rober Kiosaki', 'Think and get rich': 'Napoleon Hill'}
readers = {}

def get_info():
    print('Список книг сейчас такой: ', books)
    print('Список читателей сейчас такой: ', readers)

def manager():
    global books
    book = input(f'You want to take book or return: ')
    name = input('Enter your name: ')
    if book in books:
        # readers[name] = {k: v for k, v in books.items()}
        print(f'Which book you want to take? Choose from: ', books)
        # books[name] = books
        book = input('Which book you want to take? Enter only name: ')
        name = input('Enter your name: ')
        print('You are registered successfully')
    else:
        book = input('Do you want to return this book? Yes/No: ')

get_info()        
manager()
    