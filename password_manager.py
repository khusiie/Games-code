master_pwd = input("what is the master password?  ")

def view():
     with open ('passwords.text', 'r') as f:
       for line in f.readlines():
          data = line.rstrip()
          user , passw = data.split("|")
          print("user:" ,user, " ,  password:",passw)


def add():

    name = input('Account Name: ')
    pwd  = input('password: ')

    with open ('passwords.text', 'a') as f:
        f.write(name + "|" + pwd + "\n")


while True:
   mode = input ("would you like to add a new password or view existing ones(view,add)?  ")
   if mode == "q":
      break
   
   if mode == "view":
      view()
   elif mode == "add":
      add()
   else:
      print("Invalid mode.")
      continue