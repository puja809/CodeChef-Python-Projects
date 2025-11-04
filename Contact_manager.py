def select_choice(choice):
    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contact()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    elif choice == 6:
        print('Goodbye!')
    else:
        print('Invalid choice. Select a number between 1-6!!')


def add_contact():
    """Add contacts"""
    name=input('Enter a name:')

    number=input('Enter a number:')
    if len(number)!=10:
        print('Invalid input! Please enter a valid name and 10-digit phone number.')
    else:
        contact[number]=name
        print(f"Contact '{name}' added successfully!")


def view_contact():
    """View Contacts"""
    print('Contact List: ')
    for key,value in contact.items():
        print(f'{value}: {key}')

def search_contact():
    """Search Contact"""
    name=input('Enter a name to search:')
    if contact == {} or name.lower() not in map(str.lower,list(contact.values())):
        print('Contact not found!')
    else:
        for key,value in contact.items():
            if value.lower()==name.lower():
                print(f'{value}: {key}')



def update_contact():
    """Update Contact"""
    name=input('Enter the contact name to update:')
    if name.lower() not in map(str.lower,list(contact.values())):
        print('Contact not found!')

    else:
        new_name=input('Enter the new name (press Enter to keep the same): ')
        new_number=input('Enter the new number (press Enter to keep the same): ')
        for key,value in list(contact.items()):
            if value.lower()==name.lower():
                contact[key] = new_name
                key=new_number

        print(f'Contact {name} updated successfully!')


def delete_contact():
    """Delete Contact"""
    name=input('Enter the name to delete:')
    if name.lower() not in map(str.lower, list(contact.values())):
        print('Contact not found!')
    else:
        for key,value in list(contact.items()):
            if value.lower()==name.lower():
                del contact[key]
        print(f'Contact {name} deleted successfully!')



if __name__=='__main__':
    contact ={}
    while True:
        print('Contact Manager Menu:')
        print('1.Add a Contact')
        print('2.View Contacts')
        print('3.Search for a Contact')
        print('4.Update a Contact')
        print('5.Delete a Contact')
        print('6.Exit')
        choice = int(input('Choose an Option: '))
        select_choice(choice)
        if choice == 6:
            break


