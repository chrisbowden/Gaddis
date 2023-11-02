# The get_login function accepts first name
# last name and ID as arguments. It returns
# a system login name

def get_login_name(first, last, idnumber):
    # Get the first three letters of the first name
    # If name less than 3 chars, get the whole name
    set1 = first[0:3]

    # Get first 3 letters of last name
    set2 = last[0:3]

    # Get the last three characters of the student ID
    set3 = idnumber[-3:]

    # Concatenate
    login_name = set1 + set2 + set3

    return login_name


# Valid password function accepts a password as an argument
# and returns either true or false depending if the password is valid
# Must be 7 characters, one upper, one lower, and one digit

def valid_password(password):
    # Set boolean flags
    correct_length = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    # Begin the validation. Start with password length
    if len(password) >= 7:
        correct_length = True

        # Test each character and set flag as required
        for ch in password:
            if ch.isupper():
                has_uppercase = True
            if ch.islower():
                has_lowercase = True
            if ch.isdigit():
                has_digit = True

    # Determine whether all requirements are met
    if correct_length and has_lowercase and has_lowercase and has_digit:
        is_valid = True
    else:
        is_valid = False

    # Return the result
    return is_valid
