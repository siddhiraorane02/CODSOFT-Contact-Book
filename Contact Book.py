
contacts={}

def add(contacts):
    Name=input("\nEnter a name: ")
    Phone_No=input("Enter a phone no: ")
    Email_id=input("Enter a Email ID: ")
    Address=input("Enter address: ")
    contacts[Name]=({"Name": Name,"Phone_No": Phone_No,"Email_id": Email_id,"Address": Address})
    print("Details added successfully!")
def show_contact(contacts):
    if contacts:
        print("\nCONTACT LISTS:")
        for Name, value in contacts.items():
            print("\nName:",Name)
            print("Phone No:",value['Phone_No'])
            print("Email ID:",value['Email_id'])
            print("Address:",value['Address'])
    else:
          print("No contacts found.")
          
def search(contacts):
    Name=input("Enter the name you want to search: ")
    if Name in contacts:
        for key, value in contacts[Name].items():
            print(f"{key}: {value}")
    else:
        print("This contact name is not found.")
        
def update(contacts):
    s=input("Select name you want to update: ")
    if s in contacts:
        Name=input("Enter new name: ")
        Phone_No=input("Enter new phone no: ")
        Email_id=input("Enter new Email ID: ")
        Address=input("Enter new address: ")
            
        contacts[Name]={"Name": Name,"Phone_No": Phone_No,"Email_id": Email_id,"Address": Address}
                                   
        contacts.pop(s)
            
    else:
        print("This contact name is not found.")
    
def delete():
    Name=input("Enter the name you want to delete: ")
    if Name in contacts:
        contacts.pop(Name)
        print("Deleted successfully!")
    else:
        print("This contact name is not found.")
    
ch=0
while(ch!=6):
    print("\n\n1.Add \n2.Show List \n3.Search \n4.Update \n5.Delete \n6.Exit")
    ch=int(input("\nEnter Your Choice: "))

    match ch:
        case 1:
            add(contacts)
        case 2:
            show_contact(contacts)
        case 3:
            search(contacts)
        case 4:
            update(contacts)
        case 5:
            delete()
        case 6:
            print("All Done")
        case _:
            print("Incorrect option")
            
                    
