class RationalNumber: 
    def __init__(self, numerator: int = 0, denominator: int = 1) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def is_valid_rational_number(self) -> bool : # Predicate function to confirm q is not equal to 0
        if self.denominator > 0: 
            return True
        else:
            return False

test = RationalNumber(2,0)
print(test.is_valid_rational_number())
