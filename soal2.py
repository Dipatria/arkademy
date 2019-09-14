import re

def is_username_valid(text):
    exp = r'^[A-Za-z][A-Za-z0-9]{4,8}$'
    return (True if re.match(exp, text) else False)
    
def is_password_valid(text):
    exp = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@])(?=.*[@!#\$%\^&\*])(?=.{8,})'
    return (True if re.match(exp, text) else False)

print(is_username_valid('@sony'))
print(is_username_valid('Ayu99v'))
print(is_password_valid('C0d3YourFuture!#'))
print(is_password_valid('p@ssW0rd#'))