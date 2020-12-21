 
#   |3|2|8|5|   Argument
#   |!|+|-|**|  Operator
#   |W|4|2|7|   Argument2
#     |W|W|W|   w

argument = 0


argument = input("podaj argument ")
operator = input("podaj operator |!|+|-|**| ")
if(operator == '!'):
    print("wybrałeś |!|")
    argument = int(argument)
    for wynik17 in range(argument):

        tablica = []
        tablica = wynik17
        print(tablica,end="|")
        
        n = [0] + 1
        tablica[n]

if(operator == '+'):
    print("wybrałeś |+|")
    argument2 = input("podaj 2 argument ")
    wynik = int(argument) + int(argument2)
    print("wynik = ",wynik)

if (operator == '-'):
    print("wybrałeś |-|")
    argument2 = input("podaj 2 argument ")
    wynik = int(argument) - int(argument2)
    print("wynik = ", wynik)

if (operator == '**'):
    print("wybrałeś |**|")
    argument2 = input("podaj 2 argument ")
    wynik = int(argument) ** int(argument2)
    print("wynik = ", wynik)
