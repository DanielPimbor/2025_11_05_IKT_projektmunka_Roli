email = input("Your email address: ")

length_of_email = len(email)
number_of_at_characters = email.count("@")
number_of_dot_characters = email.count(".")
position_of_at = email.find("@")

position_of_first_dot = email.find(".")
position_of_last_dot = email.rfind(".")
position_of_first_dot_after_the_at = email.find(".", position_of_at)


error_message_no_at = "An email address has to contain a '@' character!"
error_message_too_many_at = "An email address cannot contain more than one '@' characters!"
error_message_no_dot = "An email address has to contain at least one '.' character!"
error_message_no_username = "The username before the '@' character cannot be empty!"
error_message_no_dot_in_domain = "The domain has to contain at least one '.' character!"
error_message_no_server_name = "The domain cannot start with a '.' character!"
error_message_no_tld = "The top-level domain cannot be empty!"
error_message_short_tld = "The top-level domain has to be at least two characters long!"
error_message_no_domain = "The domain after the '@' character cannot be empty!"
error_message_invalid_username = "The username cannot start with a '.' character!"

ok_message = "Valid email address :)"
is_valid = True

hibak = 0

while is_valid:
    if number_of_at_characters == 0:
        print(error_message_no_at)
        hibak += 1

    elif number_of_at_characters > 1:
        print(error_message_too_many_at)
        hibak += 1

    else:
        username, domain = email.split("@")

        if len(username) == 0:
            print(error_message_no_username)
            hibak += 1

        if username[0] == ".":
            print(error_message_invalid_username)
            hibak += 1

        if len(domain) == 0:
            print(error_message_no_domain)
            hibak += 1

        else:
            if "." not in domain:
                print(error_message_no_dot_in_domain)
                hibak += 1
            else:
                domain_parts = domain.split(".")
                if len(domain_parts[0]) == 0:
                    print(error_message_no_server_name)
                    hibak += 1

                if len(domain_parts[-1]) == 0:
                    print(error_message_no_tld)
                    hibak += 1

                elif len(domain_parts[-1]) < 2:
                    print(error_message_short_tld)
                    hibak += 1

    if number_of_dot_characters == 0:
        print(error_message_no_dot)
        hibak += 1

    break

if hibak == 0:
    print(ok_message)
