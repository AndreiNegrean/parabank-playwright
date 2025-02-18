from faker import Faker
from support.user import User


def generate_fake_user(valid_user: bool) -> User:
    faker = Faker()
    username = faker.user_name() if valid_user else ''
    return User(username=username,
                password=faker.password(),
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                address=faker.address(),
                city=faker.city(),
                state=faker.state(),
                zip_code=faker.zipcode(),
                phone=faker.phone_number(),
                ssn=faker.ssn())

