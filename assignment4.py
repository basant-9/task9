contacts = {}

def add_contact (contacts , name , phone) :
    if name in contacts :
        return error 
    contacts[name] = phone

def remove_contact (contacts , name ) : 
    if name in  contacts  :
        del contacts[name]
        return True
    else :
        return False

def search (contacts , name ) :
    return [f"{name}: {contacts[name]}"]

def view (contacts) :
    return [f"{name} : {phone}" for name,phone in contacts.items()]

def update_contact(contacts , name , phone) :
    if name in contacts :
        contacts[name] = phone
        return True
    else :
        return False 


add_contact(contacts, "Raina", "12222")
add_contact(contacts, "Habeba", "12333")

print(view(contacts))

print(search(contacts, "Habeba")) 

update_contact(contacts, "Raina", "15555")

remove_contact(contacts, "Habeba")

print(view(contacts)) 