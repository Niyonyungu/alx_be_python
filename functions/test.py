def function_name(parameters):
    # code block
    return

def login(email, password):
    # code block
    if email == "doe@alxafrica.com" and password == "123456":
        return True
    return False

# ternary operator example
def login2(email, password):
    # code block
    return True if email == "doe@alxafrica.com" and password == "123456" else False

def login3(email, password):
    # code block
    return email == "doe@alxafrica.com" and password == "123456"

# print(f"Can user login?: {login3('doe@alxafrica.com', '123456')}")
# return_value1 = login('fhdjhfdjfh', '123456')

def login_with_google(google_id):
    print(f"User Logged in succesfully with this Google ID: {google_id}")

    # return True if google_id == "1234567890abcdefg" else None

return_value2 = login_with_google("1234567890abcdefg")

if return_value2 is None:
    print("Access Denied")
else:
    print("Access Granted")


    







