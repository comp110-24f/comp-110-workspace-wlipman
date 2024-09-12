"""First Challenge Question."""

__author__ = "730521633"


def mimic(message: str) -> str:
    """Take a function and repeat it back to me"""
    return message


def main() -> None:
    """Print the result of calling mimic."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
