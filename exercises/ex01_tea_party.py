"""Creating a Tea Party, and planning the quantities of items pricing."""

__author__: str = "730521633"


def main_planner(guests: int) -> None:
    """Print information about Tea Party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """Compute number of tea bags needed per person."""
    return people * 2


def treats(people: int) -> int:
    """Compute number of treats needed per person."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Compute tea bag + treat cost."""
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
