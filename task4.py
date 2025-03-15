contacts = {}

def input_error(func):
    # Decorator
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."
    return inner

def main():
    print("Welcome to the assistant bot!")
    
    commands = {
        "hello": greet,
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
        "all": show_all,
        "close": goodbye,
        "exit": goodbye
    }
    
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print("Please enter a valid command.")
            continue

        cmd, *args = parse_input(user_input)

        if cmd in commands:
            print(commands[cmd](*args))
            if cmd in {"close", "exit"}:
                break
        else:
            print(f"Invalid command. Available commands: {', '.join(commands.keys())}")

def parse_input(user_input):
    # Getting command and arguments
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(name=None, phone=None):
    if not name or not phone:
        raise ValueError

    if name in contacts:
        return f"Contact '{name}' already exists."
    
    contacts[name] = phone
    return f"Contact '{name}' added."

@input_error
def change_contact(name=None, phone=None):
    if not name or not phone:
        raise ValueError

    if name not in contacts:
        raise KeyError

    contacts[name] = phone
    return f"Contact '{name}' updated."

@input_error
def show_phone(name=None):
    if not name:
        raise IndexError
    
    return contacts[name]

def show_all():
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) if contacts else "No contacts available."

def greet():
    return "How can I help you?"

def goodbye():
    return "Goodbye!"

if __name__ == "__main__":
    main()