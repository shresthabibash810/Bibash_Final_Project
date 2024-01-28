import codecs
import getpass
def login():
    username = input("User: ")
    password = getpass.getpass("Password: ")

    #Encoding the password using rot-13
    encode_password = codecs.encode(password, 'rot_13')

    # Check if the user exists and the password is correct
    with open("passwd.txt", "r") as file:
        for line in file:
            parts = line.split(":")
            if parts[0] == username and parts[2].strip() == encode_password:
                print("Access granted.")
                return

    print("Access denied.")

if __name__ == "__main__":
    login()
