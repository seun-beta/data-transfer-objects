from dataclasses import dataclass, field
import random
from typing import Union


def id_generator() -> int:
    return random.randint(1000, 9999)


@dataclass
class Customer:

    customer_id: int = field(init=False, default_factory=id_generator)
    username: str


customer_dict = {}


@dataclass
class CustomerRepository:
    def set(self, customer: Customer) -> dict:
        customer_dict[customer.customer_id] = customer
        return customer_dict

    def get(self, customer_id: int) -> Union[Customer, str]:
        try:
            customer = customer_dict[customer_id]
            return customer
        except KeyError:
            return "No customer found"

    def pop(self, customer_id: int) -> None:
        customer_dict.pop(customer_id)

    def find(self, username: str) -> dict:
        find_customer_dict = {}
        for key, value in customer_dict.items():
            if value.username == username:
                find_customer_dict[key] = value
            else:
                pass

        return find_customer_dict


username1: str = "customer"
customer1: Customer = Customer(username=username1)

username2: str = "customer"
customer2: Customer = Customer(username=username2)
