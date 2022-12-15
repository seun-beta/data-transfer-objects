import unittest
from typing import Any

from main import Customer, CustomerRepository


class CustomerTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """The setUp method of the Customer class"""

        self.customer_id: int = 123456
        self.username: str = "customer"
        self.customer: Customer = Customer(
            customer_id=self.customer_id, username=self.username
        )

    def test__init__(self) -> None:
        """Test the __init__ method of the Customer class"""

        self.assertIsInstance(self.customer, Customer)
        self.assertEqual(self.customer.customer_id, self.customer_id)
        self.assertEqual(self.customer.username, self.username)

    def test__str__(self) -> None:
        """Test the __str__ method of the Customer class"""

        self.assertEqual(
            self.customer.__str__(), f"{self.customer_id} --- {self.username}"
        )

    def test__init__error(self) -> None:

        with self.assertRaises(TypeError):
            Customer()


class CustomerRepositoryTestCase(unittest.TestCase):
    def setUp(self) -> None:
        """The setUp method of the CustomerRepository class"""

        self.customer_id1: int = 123456
        self.username1: str = "customer1"
        self.customer1: Customer = Customer(
            customer_id=self.customer_id1, username=self.username1
        )

        self.customer_id2: int = 1234567
        self.username2: str = "customer2"
        self.customer2: Customer = Customer(
            customer_id=self.customer_id2, username=self.username2
        )

        self.customer_id3: int = 12345678
        self.username3: str = "customer2"
        self.customer3: Customer = Customer(
            customer_id=self.customer_id3, username=self.username3
        )

        self.customer_repo: CustomerRepository = CustomerRepository()

    def test__init__(self) -> None:
        """Test the __init__ method of the CustomerRepository class"""

        self.assertIsInstance(self.customer_repo.customer_repository, dict)
        self.assertEqual(0, len(self.customer_repo.customer_repository))
        self.assertTrue(True, bool(self.customer_repo.customer_repository))

    def test_set(self) -> None:
        """Test the __init__ method of the CustomerRepository class"""

        customer_set1: Any = self.customer_repo.set(customer=self.customer1)
        customer_set2: Any = self.customer_repo.set(customer=self.customer2)
        self.assertEqual(customer_set1, self.customer1)
        self.assertEqual(customer_set2, self.customer2)

    def test_set_error(self) -> None:
        """Test the set method of the CustomerRepository class when no argument is passed into the method"""

        with self.assertRaises(TypeError):
            self.customer_repo.set()

    def test_get(self) -> None:
        """Test the get method of the CustomerRepository class"""

        self.test_set()
        customer_class1 = self.customer_repo.get(customer_id=self.customer_id1)
        customer_class2 = self.customer_repo.get(customer_id=self.customer_id2)

        self.assertEqual(customer_class1, self.customer1)
        self.assertEqual(customer_class2, self.customer2)

    def test_get_error(self) -> None:
        """Test the get method of the CustomerRepository class when a non-existent customer_id is passed"""

        with self.assertRaises(KeyError):
            self.customer_repo.get(customer_id=self.customer_id1)

    def test_pop(self) -> None:
        """Test the pop method of the CustomerRepository class"""

        self.test_set()
        customer_pop1 = self.customer_repo.pop(customer_id=self.customer_id1)
        customer_pop2 = self.customer_repo.pop(customer_id=self.customer_id2)

        self.assertEqual(customer_pop1, self.customer1)
        self.assertEqual(customer_pop2, self.customer2)
        self.assertEqual(0, len(self.customer_repo.customer_repository))

    def test_pop_error(self) -> None:
        """Test the pop method of the CustomerRepository class when a non-existent customer_id is passed"""

        with self.assertRaises(KeyError):
            self.customer_repo.pop(customer_id=self.customer_id1)

    def test_find(self) -> None:
        """Test the find method of the CustomerRepository class"""

        self.test_set()
        self.customer_repo.set(customer=self.customer3)

        username_list = self.customer_repo.find(username=self.username2)
        customer_list = []
        customer_list.append(self.customer2)
        customer_list.append(self.customer3)
        self.assertEqual(username_list, customer_list)
        self.assertTrue(customer_list)
        self.assertEqual(2, len(customer_list))

    def test_find_returns_no_value(self) -> None:
        """Test that the find method of the CustomerRepository class returns no value"""

        username_list = self.customer_repo.find(username=self.username1)

        self.assertEqual(0, len(username_list))
        self.assertFalse(username_list)


if __name__ == "__main__":
    unittest.main()
