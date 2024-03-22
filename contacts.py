contacts={
    "Ram":{
        "phone":"1234-567-890",
        "email":"ram18@gmail.com",
        "address":"1/1 mk street,nagari,India"
    },
    "Sita":{
        "phone":"1234-567-890",
        "email":"sita@gmail.com",
        "address":"1/2 mk street,nagari,India"
    }
}
def add_contact(name,phone,email,address):
    contacts[name]={
        "phone":phone,
        "email":email,
        "address":address
    }
    print("Contact added successfully!!")
def view_contacts():
    if contacts:
        for name,contact in contacts.items():
            print(f"Name:{name}")
            print(f"Phone:{contact['phone']}")
            print(f"Email:{contact['email']}")
            print(f"Address:{contact['address']}")
            print("-" * 20)
    else:
        print("Any contacts not found")
def search_contact(search_term):
    if contacts:
        for name, contact in contacts.items():
            if isinstance(contact['phone'], str) and (search_term.lower() in name.lower() or search_term in str(contact['phone'])):
                print(f"Name: {name}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                print("The contact is available!!")
                print("-" * 20)
    else:
        print("Contact not found.")
def update_contact(name, phone=None, email=None, address=None):
    if name in contacts:
        contact = contacts[name]
        if phone:
            contact['phone'] = phone
        if email:
            contact['email'] = email
        if address:
            contact['address'] = address
        print("Contact updated successfully!")
    else:
        print("Contact not found.")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully")
    else:
        print("Contact not found!!")
add_contact("yamu",2614357,"yamu@gmail.com","street")
view_contacts()
search_contact("Ram")
update_contact("Ram",phone=352476298,email="ajyetgiuahkleiu")
view_contacts()
delete_contact("Ram")
view_contacts()
