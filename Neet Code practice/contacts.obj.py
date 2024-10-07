class Contact:
    def __init__(self, name: str, phone_number: str, email: str):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def update_phone_number(self, new_phone_number: str):
        self.phone_number = new_phone_number

    def update_email(self, new_email: str):
        self.email = new_email

    def get_contact_info(self) -> str:
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"

    def is_match(self, search_term) -> bool:
        return search_term.lower() in self.name.lower() or search_term in self.phone_number or search_term.lower() in self.email.lower()



managAther = Contact("ather", "123456789", "atherkhan@gmail.com")
managAadil= Contact("aadil","696942069", "aadil.farooq.rashid@gmail.com")

print(managAther.get_contact_info())
print(managAadil.get_contact_info())

managAther.update_email("akhan@sony.live")
managAadil.update_phone_number("9493781492")

print(managAther.get_contact_info())
print(managAadil.get_contact_info())

if managAther.is_match("9493466378") is True:
    print("your phone number is stored")
else: 
    print("we could not find a match")