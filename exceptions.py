
class IllegalInputException(Exception):
    def __init__(self, context: str) -> None:
        self.description = f"Invalid input! ({context})"