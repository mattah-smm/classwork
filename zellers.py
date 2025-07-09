# DateCalculator
class DateCalculator:
    def __init__(self, year: int, month: int, day: int):
        self.original_year = year
        self.original_month = month
        self.day = day

        # Adjust month and year for Zeller's formula
        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

        self.K = self.year % 100        # Year of the century
        self.J = self.year // 100       # Zero-based century

    def calculate_weekday(self) -> str:
        q = self.day
        m = self.month
        K = self.K
        J = self.J

        # Zeller's formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + 5 * J) % 7

        # Map result to weekday
        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[h-1]

    def display_result(self):
        weekday = self.calculate_weekday()
        print(f"The date {self.original_year}-{self.original_month:02d}-{self.day:02d} was a {weekday}.")


# Example usage
if __name__ == "__main__":
    # Test case: September 15, 1589
    calc = DateCalculator(1589, 9, 15)
    calc2 = DateCalculator(2025, 5, 8)
    calc.display_result()