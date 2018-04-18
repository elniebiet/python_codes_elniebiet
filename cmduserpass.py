import getpass

user = getpass.getuser()
passwd = getpass.getpass()

def svc_login(user, passwd):
    
    if(passwd == "abhay"):
        print("success!")
    else:
        print("failed")
        
svc_login(user, passwd) # You must write svc_login()
    