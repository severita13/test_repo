books = {'Financial': 'Theodor Draiser', 'Rich dad, poor dad': 'Rober Kiosaki', 'Think and get rich': 'Napoleon Hill'}
readers = {}

def get_info():
    print(f'Список книг сейчас такой: {books}')
    print(f'Список читателей сейчас такой: {readers}')
    manager()

# def take():
#     take_book = 'take'
# def return_():
#     return_book = 'return'

def reg_user():
    global books
    global readers
    
    # print(f'Which book you want to take? Choose from: {books}')
    book = input('Which book you want to take? Enter only TITLE: ')
    name = input('Enter your name: ')
    
    if book in books:
        readers[name] = {book: books[book]}
        if name in readers:   
        # readers[name] = {k: v for k, v in books.items()}
            readers[name].update({book:books[book]})
        # books[name] = books
            books.pop(book)
            print(f'{name} you have been registered successfully!')
            get_info()
        else:
            reg_user(name, book)
            books.pop(book)
            print(f'{name} you have been registered successfully!')
            get_info()
    else:
        print(f'{book} was not found. Please enter the title correctly')

def remove_user():
    global books
    global readers
    name = input('To return the book please enter YOUR name: ')
    book = input('Which book you want to return? Enter only TITLE: ')
    # if book in books:
    #     readers[name] = {book: books[book]}
    if name in readers:
        books.update(readers[name])
        readers.pop(name)
        print('You have returned the book successfully!')
    else:
        print('Yor name was not found in the list of readers')

def manager():
    global books
    global readers
    # print(f'The list of books is: {books}')
    library = input('Do you want to take or return book? Enter only take/return: ')
    if library == 'take':
        reg_user()
    elif library == 'return':
        remove_user()
    else:
        print('You can only take or return books')
    get_info()
get_info()
manager()


# get_info()        
# manager()