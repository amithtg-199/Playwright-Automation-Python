from faker import Faker
from datetime import date, timedelta

fake = Faker()


class RandomDataUtil:

    @staticmethod
    def first_name():
        return fake.first_name()

    @staticmethod
    def last_name():
        return fake.last_name()

    @staticmethod
    def email():
        return fake.email()

    @staticmethod
    def phone_number():
        return fake.phone_number()

    @staticmethod
    def integer(min_value=1, max_value=1000):
        return fake.random_int(
            min=min_value,
            max=max_value
        )

    @staticmethod
    def boolean():
        return fake.boolean()

    @staticmethod
    def checkin_date():
        return date.today().isoformat()

    @staticmethod
    def checkout_date():
        return (
            date.today() + timedelta(days=5)
        ).isoformat()

    @staticmethod
    def additional_needs():
        return fake.random_element([
            "Breakfast",
            "Lunch",
            "Dinner",
            "Extra bed"
        ])