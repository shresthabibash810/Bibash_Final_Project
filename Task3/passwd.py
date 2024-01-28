import codecs
import getpass
def change_password():
    username = input("User: ")
    current_password = input("Current Password: ")
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm: ")

    # Encoding the current and new password using rot-13
    encode_current_pw = codecs.encode(current_password, 'rot_13')
    encode_new_pw = codecs.encode(new_password, 'rot_13')

    # Reading the file
    with open("passwd.txt", "r") as file:
        lines = file.readlines()

    found = False
    with open("passwd.txt", "w") as file:
        for line in lines:
            parts = line.split(":")
            if parts[0] == username:
                if parts[2].strip() == encode_current_pw:
                    found = True
                    file.write(f"{parts[0]}:{parts[1]}:{encode_new_pw}\n")
                    print("Password changed.")
                else:
                    print("Invalid current password. Nothing changed.")
            else:
                file.write(line)

    if not found:
        print("User not found. Nothing changed.")

if __name__ == "__main__":
    change_password()