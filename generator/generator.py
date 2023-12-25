import random
import sys

from data.data import Person
from faker import Faker

faker_ru = Faker('ru_RU')
Faker.seed()


def generated_person():
    yield Person(
        full_name=f"{faker_ru.last_name()} {faker_ru.first_name()} {faker_ru.middle_name()}",
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(10, 99),
        salary=random.randint(0, 300000),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


def generator_file():
    path = sys.path[1] + fr"\generated_files\upload_file{random.randint(1, 100)}.txt"
    with open(path, "w+") as file:
        file.write(f"It's a test file number{random.randint(1, 100)}")
    return file.name

