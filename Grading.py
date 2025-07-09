import math
from typing import List, Tuple

def prompt_names_and_scores() -> Tuple[List[str], List[float]]:
    while True:
        try:
            count = int(input("Enter Number of students to grade: "))
            if count > 0:
                break
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Enter a whole number.")

    names, scores = [], []
    print("\nEnter student names and scores:")

    for i in range(count):
        name = input(f"Student {i + 1} name: ").strip() or f"Student{i + 1}"
        names.append(name)

        while True:
            try:
                score = float(input(f"Score for {name}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                print("Score must be between 0 and 100.")
            except ValueError:
                print("Invalid score. Enter a number.")

    return names, scores

def match_grade(score: float) -> str:
    if score >= 70: return "A"
    if score >= 60: return "B"
    if score >= 50: return "C"
    if score >= 40: return "D"
    return "F"

def compute_avg(scores: List[float]) -> float:
    return round(sum(scores) / len(scores), 2)

def generate_results_table(names: List[str], scores: List[float]) -> None:
    print("\n=== Student Results ===")
    print(f"{'Name':<15} {'Score':<10} {'Grade'}")
    print("-" * 30)

    for name, score in zip(names, scores):
        grade = match_grade(score)
        print(f"{name:<15} {score:<10.2f} {grade}")

    avg = compute_avg(scores)
    print(f"\nClass Average: {avg}")
    print(f"Rounded Up: {math.ceil(avg)}")
    print(f"Rounded Down: {math.floor(avg)}")

def main():
    print("Welcome to Grading System ")


    while True:
        names, scores = prompt_names_and_scores()
        generate_results_table(names, scores)
        if input("\nGrade another class? (yes/no): ").strip().lower() != "yes":
            print("Thank you for using the Python grading system!")
            break

if __name__ == "__main__":
    main()