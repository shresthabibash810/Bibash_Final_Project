import codecs
import getpass
def change_password():
    username = input("User: ")
    current_password = input("Current Password: ")
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm: ")

    # Hash the passwords
    current_hash = codecs.encode(current_password, 'rot_13')
    new_hash = codecs.encode(new_password, 'rot_13')

    # Read the file
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("passwd.txt", "w") as file:
        for line in lines:
            parts = line.split(":")
            if parts[0] == username:
                if parts[2].strip() == current_hash:
                    found = True
                    file.write(f"{parts[0]}:{parts[1]}:{new_hash}\n")
                    print("Password changed.")
                else:
                    print("Invalid current password. Nothing changed.")
            else:
                file.write(line)

    if not found:
        print("User not found. Nothing changed.")

if __name__ == "__main__":
    change_password()