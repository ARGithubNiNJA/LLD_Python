from abc import ABC, abstractmethod

class Oven(ABC):
    @abstractmethod
    def start_oven(self):
        ...

    @abstractmethod
    def end_oven(self, order):
        ...

class Order(ABC):
    @abstractmethod
    def receive_order(self):
        ...

class Restaurant(Order, Oven):
    def __init__(self, order):
        self.order = order

    def receive_order(self):
        return "Order Received"

    def start_oven(self):
        return "Oven Started"

    def end_oven(self, order):
        return f"{order} prepared"

if __name__ == "__main__":
    while True:
        ordering = input("Do you have an Order?\n")

        if ordering.strip().upper() == "YES":
            requested_for = input("What is your Order?\n")

            if len(requested_for.strip()) < 1:
                print("Order cannot be empty. Please try again.\n")
                continue

            restaurant = Restaurant(requested_for)
            print(restaurant.receive_order())
            print(restaurant.start_oven())
            print(restaurant.end_oven(requested_for))

        else:
            print("Thank you for your visit\n")
            break