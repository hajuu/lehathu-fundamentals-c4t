users = {"user1":"password1","user2":"password2","user3":"password3"}
def accept_login(username,password):
    if username in users and users[username]==password:
        return True
    else:
        return False

username=input("Nhap ten nguoi dung: ")
password=input("Nhap mat khau: ")

if accept_login(username,password):
    print("login successful")
else:
    print("login failed")