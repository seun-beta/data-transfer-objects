from typing import Dict, Any


class Customer:
    def __init__(self, customer_id, username) -> None:
        self.customer_id: int = customer_id
        self.username: str = username

    def __str__(self) -> str:
        return f"{self.customer_id} --- {self.username}"


class CustomerRepository:
    def __init__(self) -> None:
        self.customer_repository: dict = {}

    def set(self, customer: Customer) -> Customer:
        set_result = self.customer_repository[customer.customer_id] = customer
        return set_result

    def get(self, customer_id: int) -> dict:
        customer = self.customer_repository[customer_id]
        return customer

    def pop(self, customer_id: int) -> dict:
        customer = self.customer_repository.pop(customer_id)
        return customer

    def find(self, username: str) -> list:
        result = []

        for key, values in self.customer_repository.items():
            if values.username == username:
                result.append(self.customer_repository[key])

        return result
