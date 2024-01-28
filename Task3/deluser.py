def delete_user():
    username = input("Enter username: ")

    with open("passwd.txt", "r") as file:
        read_file = file.readlines()

    found = False
    with open("passwd.txt", "w") as file:
        for read in read_file:
            if read.split(":")[0] != username:
                file.write(read)
            else:
                found = True
                

    if found:
        print("User Deleted.")
    else:
        print("User not found. Nothing changed.")

if __name__ == "__main__":
    delete_user()