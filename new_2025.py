def start_menu():
    print("=== Library Management System ===")
    print("Press '1' to add a book")
    print("press '2' to show all books")
    print("press '3' to search for a book")
    print("press '4' to Delete a book")
    print("press '5' to Exit")
    
library = {"Name" : [] , "Author" : [] , "Publish year" : []}
while True:
    start_menu()
    try:
        x=int(input("Choose: "))

        if(x==1):
            name = input("Enter 'Book title' : ")
            author = input("Enter 'author name' :")
            year = int(input("Enter 'publish year' :"))
            library["Name"].append(name)
            library["Author"].append(author)
            library["Publish year"].append(year)
            print("Book added successfully!\n\n\n")
        if(x==2):
            for i in range(len(library)):
                print("Book name :",library["Name"][i] , " ,Author name :",library["Author"][i] , " ,Publish year :",library["Publish year"][i],"\n")
        if(x==3):
            search = input("Enter book name to search: ")
            if search in library["Name"]:
                index = library["Name"].index(search)
                print("\nBook found!")
                print("Book name :",library["Name"][index] , " ,Author name :",library["Author"][index] , " ,Publish year :",library["Publish year"][index],"\n\n\n")
            else:
                print("Book not found.")
        if(x==4):
            delete = input("Enter book name to delete: ")
            if delete in library["Name"]:
                index = library["Name"].index(delete)
                library["Name"].pop(index)
                library["Author"].pop(index)
                library["Publish year"].pop(index)
                print("Book deleted successfully!")
            else:
                print("Book not found.")
        if(x==5):
            break
    except:
        print("something went wrong, try again.")
        