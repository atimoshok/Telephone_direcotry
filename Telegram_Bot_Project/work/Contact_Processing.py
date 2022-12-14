from Search_contact import Search_cont
from Display_Contacts import Print_contacts


def Add_contact():
    contact  = []
    name_surname_number_phone = input('Введите имя, контакта - ').split()
    contact.append(name_surname_number_phone)
    print(f'Контакт {contact} добавлен в справочник')
    return contact


def Delete_contact(base):
    contact = Search_cont(base, input('Что ищем? '))
    if len(contact) == 0:
        print('Такого контакта нет ')
    else:
        if len(contact) == 1:
            base.pop(int(contact[0][0])-1)
            print(f'{contact[0]}\n Этот контакт удалён')
        elif len(contact) > 1:
            Print_contacts(contact)
            choose_contact = int(input('Найдено несколько контактов, какой ID удалить? '))
            print(f'{base[choose_contact - 1]} контакт удалён')
            base.pop(choose_contact - 1)
    return base

def Sort_base_id(base):
    for id in range(len(base)):
        base[id][0] = id + 1
    return base