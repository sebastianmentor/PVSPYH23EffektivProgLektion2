from coder import Coder
from faker import Faker
import random

faker = Faker()


def create_list_of_n_coders(n:int) -> list[Coder]:
    return [Coder(faker.name, random.uniform(0,100)) for _ in range(n)]