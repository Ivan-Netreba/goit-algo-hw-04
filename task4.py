def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args   
        if args[0] in contacts.keys():
            contacts[name] = phone
            return "Contact update."
        else:
            contacts[name] = phone
            return "Contact added."
    else:
        return "Wrong input."

def show_phone(args, contacts):
    name = args[0]   
    if name in contacts.keys():
        return contacts[name]
    else:
        return "No user found."
    
def show_all(contacts):
    for key in contacts:
        return contacts
        # return f"{key:10} : {contacts[key]}"

       

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command  == "add":
            print(add_contact(args, contacts))
        elif command  == "change":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
