f=open("a.txt","a")
email=input("enter the email to be validated: ")
has_uppercase = 0
has_space = 0
if len(email)>=6:
    if email[0].isalpha():
        if email.count("@")==1:
            if (email[-3]==".") ^ (email[-4]==".") and email.count(".")==1:
                for i in email:
                    if i.isupper():
                        has_uppercase=1
                    elif i.isspace():
                        has_space=1
                    elif i.isalnum() or i=="_" or i=="@" or i==".":
                        continue
                    else:
                        print("you can not put special characters")
                if has_uppercase==1:
                    print("there should be no uppercase letters in your email")
                if has_space==1:
                    print("there should be no spaces in your email")
                else:
                    f.write(email+"\n")
                    print("email is correct and has been saved")
            else:
                print("error realted to dot")
        else:
            print("@ count has to be 1")
    else:
        print("the first character of email has to be an alphabet")
else:
    print("email is shorter than 6 characters")