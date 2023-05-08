from module.schedule import schedule
from module.books import books

def collect_the_bag():
    print(string_books(books))
    collected_books = []
    day_schedule = get_day_schedule()
    # варіант з одиницею не обробляла, бо, нажаль, шкіл з одним уроком в день не існує(
    if len(day_schedule) < 5:
        print(f"Санько, в тебе {len(day_schedule)} спроби")
    else:
        print(f"Санько, в тебе {len(day_schedule)} спроб")
    print_line()
    for _ in range(len(day_schedule)):
        book_name = input("Введи назву підручника:").capitalize()
        if book_name in books:
                if book_name in collected_books:
                    print("Ти вже поклав цю книгу")    
                else:
                    collected_books.append(book_name)
                    print("Добре Саня, вгадав. Все ж таки задатки розуму присутні") 
                    if book_name in day_schedule:
                        print("Та не вже, це навіть потрібний підручник")
        else:
            print("Олух ти, Санек! Давай ще раз)")
    print_line()
    print(f"{string_books(collected_books)}.\nСанько, удачі в школі)")  

def get_day_schedule():
    day = input("На який день тижня подрібна сумка? ").capitalize()
    try:
        return schedule[day]
    except KeyError:
        print ("Саня, дивись на календар")
        return get_day_schedule()
    
def string_books(books_list):
    string_books = f'{books_list[0]}'
    for i in range(1, len(books_list)):
        string_books += f', {books_list[i]}'
    return string_books

def print_line():
    print("-" * 50)