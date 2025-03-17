class Battery:
    def __init__(self, max_charge=100):
        self.max_charge = max_charge
        self.charge = max_charge

    def check_battery(self):
        """Returns battery level as a string."""
        return f"Battery level: {self.charge}%"

    def drain(self, amount):
        """Drains battery by a given amount."""
        self.charge -= amount
        if self.charge < 0:
            self.charge = 0
        print(f"Battery drained by {amount}%. Current level: {self.charge}%")

    def recharge(self):
        """Recharges battery to full."""
        self.charge = self.max_charge
        print("Battery recharged to 100%.")
