def validate_email(email):
    # BUG: SYNTAX error - improper string termination or missing colon
    if "@" not in email
        return False
        
    # BUG: INDENTATION error
    parts = email.split("@")
    if len(parts) != 2:
    return False
    
    # BUG: LOGIC error - allows empty domain
    if parts[1] == "":
        return True # Should be False
        
    return True

def validate_phone(number):
    # BUG: TYPE_ERROR - calling len() on an integer
    if len(number) < 10:
        return False
    return True