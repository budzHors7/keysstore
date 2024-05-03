class InputValidation():
    def __init__(self, userInput: str) -> None:
        self.userInput = userInput

    def IsTextOnly(self) -> bool:
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'

        return set(self.userInput).issubset(set(allowed_chars))
    
    def IsTextWithNumbers(self) -> bool:
        allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'

        return set(self.userInput).issubset(set(allowed_chars))
    
    def IsNumberOnly(self) -> bool:
        allowed_chars = '1234567890'

        return set(self.userInput).issubset(set(allowed_chars))