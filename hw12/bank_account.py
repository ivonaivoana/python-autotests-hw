class Bank:
    def __init__(self):
        self.clients = {}
        self.deposit_accounts = {}

    def register_client(self, client_id, name):
        if client_id in self.clients:
            raise ValueError(f"Client with the id {client_id} is already registered")
        self.clients[client_id] = {
            "name": name,
            "deposit": None
        }

    def open_deposit_account(self, client_id, start_balance, years):
        if client_id not in self.clients:
            raise ValueError(f"There is no client with the id {client_id} in the system")
        if client_id in self.deposit_accounts:
            raise ValueError(f"The deposit account with the id {client_id} is already registered")
        self.deposit_accounts[client_id] = {
            "start_balance": start_balance,
            "years": years
        }

    def calc_deposit_interest_rate(self, client_id):
        if client_id not in self.clients:
            raise ValueError(f"There is no client with the id {client_id} in the system")
        if client_id not in self.deposit_accounts:
            raise ValueError(f"There is no deposit account for the client with the id {client_id}")

        deposit = self.deposit_accounts[client_id]
        start_balance = deposit["start_balance"]
        years = deposit["years"]
        balance = start_balance
        months = years * 12

        for month in range(months):
            balance += balance * (0.10 / 12)

        return round(balance, 2)

    def close_deposit(self, client_id):
        if client_id not in self.deposit_accounts:
            raise ValueError(f"No deposit account exists for client {client_id}")
        del self.deposit_accounts[client_id]
        print(f"The deposit account for the client with the id {client_id} has been closed")


bank = Bank()
bank.register_client("0000001", "Siarhei")
bank.open_deposit_account("0000001", 1000, 1)
print(bank.calc_deposit_interest_rate("0000001"))  # → 1104.71
bank.close_deposit("0000001")
