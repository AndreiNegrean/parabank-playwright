class User:
    def __init__(self, username: str, password: str, first_name: str, last_name: str, address: str, city: str,
                 state: str, zip_code: str, phone: str, ssn: str) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.ssn = ssn
