# Mediator Interface
class Mediator:
    def register_buyer(self, buyer):
        pass

    def register_seller(self, seller):
        pass

    def send_message(self, message, participant):
        pass

# Concrete Mediator Class
class AuctionMediator(Mediator):
    def __init__(self):
        self.buyers = []
        self.se