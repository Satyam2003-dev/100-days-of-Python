#   Function with output


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You did not provide any input please provide valid input"
    formated_f_name = f_name.title()         # title() is used to convert string into title
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
# print(format_name("SATYAM", "kumar"))


print(format_name(input("What is your first name? "), input("What is your last name? ")))
