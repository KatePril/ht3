from module.schedule import schedule

def collect_the_bag():
    day_schedule = get_day_schedule()
    collected_books = []
    while True:
        try:
            collected_books = get_books(day_schedule, collected_books)
            break
        except TypeError:
            continue
    print_books(collected_books)
    print("Санько, удачі в школі")
    
    

def get_day_schedule():
    day = input("На який день тижня подрібна сумка? ").capitalize()
    print(day)
    try:
        print(list(schedule[day]))
        return list(schedule[day])
    except KeyError:
        print ("Саня, дивись на календар")
        get_day_schedule()

def get_books(day_schedule):
    collected_books = []
    while len(day_schedule) > 0:
            book_name = input("Введи назву підручника:").capitalize()
            if book_name in collected_books:
                print("Ти вже поклав цю книгу")
            elif book_name in day_schedule:
                collected_books.append(book_name)
                day_schedule.remove(book_name)
                print("Добре Саня, вгадав. Все ж таки задатки розуму присутні")
            else:
                print("Олух ти, Санек! Давай ще раз)")
    return collected_books

def print_books(books_list):
    string_books = f'{books_list[0]}'
    for i in range(1, len(books_list)):
        string_books += f', {books_list[i]}'