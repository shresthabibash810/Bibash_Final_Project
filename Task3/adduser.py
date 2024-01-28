import getpass
import codecs

def add_user():
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")

    #Check if the username already exists or not 
    with open("passwd.txt", "r") as file:
        for read in file.readlines():
            existing_usernames = read.split(":")[0] 

            if username in existing_usernames:
                print("Cannot add. Most likely username already exists.")
                return

    #Encode the password using ROT13
    encoded_password = codecs.encode(password, 'rot_13')

    # Appending the file and storing it at last of passwd,txt file
    with open("passwd.txt", "a") as file:
        file.write(f"{username}:{real_name}:{encoded_password}\n")

    print("User Created.")

if __name__ == "__main__":
    add_user()

