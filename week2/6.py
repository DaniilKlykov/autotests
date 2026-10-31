class Lead:
    def __init__(self, name):
        self.name = name


def change_name(lead: Lead, new_name: str) -> None:
    lead.name = new_name


if __name__ == "__main__":
    original_lead = Lead("Иван")
    print(f"До вызова функции: {original_lead.name}")

    change_name(original_lead, "Пётр")
    print(f"После вызова функции: {original_lead.name}")
