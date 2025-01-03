def email_slicer(email):
    try:
        username,domain =email.split('@')
        return f"Username: {username}\nDomain: {domain}"
    except ValueError:
        return "Entered email is not valid"
    
if __name__ == "__main__":
    try:
        email = input("Enter your email: ")
        print(email_slicer(email))
    except Exception as e:
        
        print(e)