

# Я НЕ УСПЕЛ ДОДЕЛАТЬ ЭТО ЗАДАНИЕ, ВСЕ ЕЩЕ РРАЗБИРАЮСЬ !!!


def show_menu():
    print("\nВыбирите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти обонента по фамилии\n"
          "3. Найти обонента по номеру телефона\n"
          "4. Добавить обонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice



def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            fi_mail(phone_book)
            # last_name=input('lastname ')
            # print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
	    	
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)


        choice=show_menu()



def print_result(phone_book):
    print(phone_book)



def fi_mail(spisok):
    familia = input('Введите фамилию: ')
    for i in spisok:
        if familia in i:
            print(i.values)
        else:
            print('нет такого имени')
    
def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

	

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

            record = dict(zip(fields, line.split(','))) 
            # dict(( (Фамилия,Иванов),(Имя, Точка),(Номер,8928) ))
        phone_book.append(record)	
    return phone_book


def write_txt(filename , phone_book):

    with open('phonebook.txt','w' ,encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s='' 
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')





work_with_phonebook()
