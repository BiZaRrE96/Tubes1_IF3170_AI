
class IllegalInputException(Exception):
    def __init__(self, index: int = None) -> None:
        self.description = "Invalid input!"
        if (index != None):
            self.description = self.description + f" ({chr(ord('x') + (index % 3)).upper()}{index // 3 + 1})"
        pass
    
    def __init__(self, context: str) -> None:
        self.description = f"Invalid input! ({context})"