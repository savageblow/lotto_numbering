import random
import time
from typing import List, Dict, Optional


class KenyaLottoGenerator:
    """
    Kenya Lotto Number Generator

    Default rule:
    - Pick 6 unique numbers
    - Number range: 1 to 49
    - Optional bonus number: 0 to 9

    This generator is for entertainment only.
    It does not increase the chance of winning.
    """

    def __init__(
        self,
        min_number: int = 1,
        max_number: int = 49,
        pick_count: int = 6,
        use_bonus: bool = True,
        bonus_min: int = 0,
        bonus_max: int = 9
    ):
        self.min_number = min_number
        self.max_number = max_number
        self.pick_count = pick_count
        self.use_bonus = use_bonus
        self.bonus_min = bonus_min
        self.bonus_max = bonus_max

        self.validate_settings()

    def validate_settings(self) -> None:
        """Validate lotto generator settings."""

        if self.min_number >= self.max_number:
            raise ValueError("Minimum number must be smaller than maximum number.")

        total_numbers = self.max_number - self.min_number + 1

        if self.pick_count > total_numbers:
            raise ValueError("Pick count cannot be greater than the number range.")

        if self.pick_count <= 0:
            raise ValueError("Pick count must be greater than zero.")

        if self.use_bonus and self.bonus_min > self.bonus_max:
            raise ValueError("Bonus minimum number cannot be greater than bonus maximum number.")

    def generate_main_numbers(self) -> List[int]:
        """Generate unique main lotto numbers."""

        number_pool = list(range(self.min_number, self.max_number + 1))
        selected_numbers = random.sample(number_pool, self.pick_count)
        selected_numbers.sort()

        return selected_numbers

    def generate_bonus_number(self) -> Optional[int]:
        """Generate a bonus number if bonus mode is enabled."""

        if not self.use_bonus:
            return None

        return random.randint(self.bonus_min, self.bonus_max)

    def generate_ticket(self) -> Dict[str, object]:
        """Generate one lotto ticket."""

        main_numbers = self.generate_main_numbers()
        bonus_number = self.generate_bonus_number()

        ticket = {
            "main_numbers": main_numbers,
            "bonus_number": bonus_number,
            "game": "Kenya Lotto Style 6/49",
            "message": "Good luck!"
        }

        return ticket

    def generate_multiple_tickets(self, ticket_count: int = 5) -> List[Dict[str, object]]:
        """Generate multiple lotto tickets."""

        if ticket_count <= 0:
            raise ValueError("Ticket count must be greater than zero.")

        tickets = []

        for _ in range(ticket_count):
            ticket = self.generate_ticket()
            tickets.append(ticket)

        return tickets

    def display_ticket(self, ticket: Dict[str, object], ticket_number: int = 1) -> None:
        """Display a ticket in a nice format."""

        print("=" * 45)
        print(f"KENYA LOTTO TICKET #{ticket_number}")
        print("=" * 45)

        numbers = ticket["main_numbers"]
        bonus = ticket["bonus_number"]

        print("Main Numbers:")
        print("  " + " - ".join(str(number).zfill(2) for number in numbers))

        if bonus is not None:
            print(f"Bonus Number: {bonus}")

        print(ticket["message"])
        print("=" * 45)
        print()

    def animated_generate(self) -> Dict[str, object]:
        """Generate a ticket with a simple terminal animation."""

        print("Generating your lucky numbers", end="")

        for _ in range(5):
            time.sleep(0.3)
            print(".", end="", flush=True)

        print("\n")

        ticket = self.generate_ticket()
        return ticket


def main():
    generator = KenyaLottoGenerator(
        min_number=1,
        max_number=49,
        pick_count=6,
        use_bonus=True,
        bonus_min=0,
        bonus_max=9
    )

    print("Welcome to the Kenya Lotto Number Generator")
    print()

    single_ticket = generator.animated_generate()
    generator.display_ticket(single_ticket, 1)

    print("Generating 5 more tickets...")
    print()

    tickets = generator.generate_multiple_tickets(5)

    for index, ticket in enumerate(tickets, start=1):
        generator.display_ticket(ticket, index)


if __name__ == "__main__":
    main()
