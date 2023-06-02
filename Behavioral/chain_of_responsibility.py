class Ticket:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority


class SupportAgent:
    def __init__(self, name):
        self.name = name
        self.next_agent = None

    def set_next_agent(self, next_agent):
        self.next_agent = next_agent

    def handle_ticket(self, ticket):
        pass


class Level1Agent(SupportAgent):
    def handle_ticket(self, ticket):
        if ticket.priority == 'low':
            print(f"{self.name} - Handling low priority tickets: {ticket.description}")
        elif self.next_agent is not None:
            self.next_agent.handle_ticket(ticket)
        else:
            print(f"{self.name} - Ticket cannot be handled at this level")


class Level2Agent(SupportAgent):
    def handle_ticket(self, ticket):
        if ticket.priority == 'medium':
            print(f"{self.name} - Handling medium priority tickets: {ticket.description}")
        elif self.next_agent is not None:
            self.next_agent.handle_ticket(ticket)
        else:
            print(f"{self.name} - Ticket cannot be handled at this level")


class Level3Agent(SupportAgent):
    def handle_ticket(self, ticket):
        if ticket.priority == 'high':
            print(f"{self.name} - Handling high priority tickets: {ticket.description}")
        elif self.next_agent is not None:
            self.next_agent.handle_ticket(ticket)
        else:
            print(f"{self.name} - Ticket cannot be handled at this level")



def main():
    ticket1 = Ticket("Website down", "medium")
    ticket2 = Ticket("Payment issue", "high")
    ticket3 = Ticket("General inquiry", "low")

    agent1 = Level1Agent("John")
    agent2 = Level2Agent("Amy")
    agent3 = Level3Agent("Lisa")

    agent1.set_next_agent(agent2)
    agent2.set_next_agent(agent3)

    agent1.handle_ticket(ticket1)
    agent1.handle_ticket(ticket2)
    agent1.handle_ticket(ticket3)

if __name__ == "__main__":
    main()