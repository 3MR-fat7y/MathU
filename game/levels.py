import math
import random

def math_level_measurement():
    print("Welcome to the Math Level Measurement Program!")
    print("-----solve five questions for this test-------")
    exit() if input("press Enter to begen or 'x' to exit").lower() == 'x' else None

    equations = [
        {"Equation": "(5 + 3) * 6 / 2", "_format": "(5 + 3) × 6 ÷ 2"},
        {"Equation": "9 + (5 / 3) * 2**3", "_format": "9 + 5 ÷ 3 × 2³"},
        {"Equation": "math.sqrt(25) + 7 * 3", "_format": "√25 + 7 × 3"},
        {"Equation": "(10 - 2) * (8 / 4)", "_format": "(10 - 2) × (8 ÷ 4)"},
        {"Equation": "2**4 - 5 * 3", "_format": "2⁴ - 5 × 3"},
        {"Equation": "9 * 7 - 7", "_format": "9 × 7 - 7"},
        {"Equation": "10 / 5 * 2", "_format": "10 ÷ 5 × 2"},
        {"Equation": "15 + 2 * 6", "_format": "15 + 2 × 6"},
        {"Equation": "(4**2 + 3) / 5", "_format": "(4² + 3) ÷ 5"},
        {"Equation": "math.sin(30) * 8", "_format": "sin(30°) × 8"},
        {"Equation": "math.floor(10.5) - 3", "_format": "floor(10.5) - 3"},
        {"Equation": "math.log(100, 5) + 2", "_format": "log₅(100) + 2"},
        {"Equation": "(12 / 2) + 4 * 3", "_format": "12 ÷ 2 + 4 × 3"},
        {"Equation": "math.exp(2) - 5", "_format": "exp(2) - 5"},
        {"Equation": "math.factorial(4) / 2", "_format": "4! ÷ 2"},
        {"Equation": "3**3 - 2", "_format": "3³ - 2"},
        {"Equation": "math.ceil(9.4) * 2", "_format": "ceil(9.4) × 2"},
        {"Equation": "math.cos(45) * 12", "_format": "cos(45°) × 12"},
        {"Equation": "math.sqrt(144) + 10", "_format": "√144 + 10"},
        {"Equation": "math.3log(e**3) * 5", "_format": "logₑ(e³) × 5"}
    ]

    user_answers = []
    
    for i , equation in enumerate(random.choices(equations,k=6), start=1):
        user_input = input(f"Question [{i}]: {equation['_format']} = ")

        try:
            result = eval(equation['Equation'])
            user_answer = float(user_input)
            user_answers.append((user_answer, result))
            
        except (ValueError, SyntaxError):
            print("Invalid input. Please enter a valid number.")
            user_answers.append((None, None))

    print("\nResults:")
    correct_count = 0

    for i, (user_answer, result) in enumerate(user_answers, start=1):
        if user_answer is not None:
            print(f"Question [{i}]: {result:.2f}  (Your answer: {user_answer:.2f})")
            if math.isclose(user_answer, result, abs_tol=1e-2):
                print(" - Correct")
                correct_count += 1
            else:
                print(" - Incorrect")

    total_questions = len(user_answers)
    score = (correct_count / total_questions) * 100 if total_questions > 0 else 0
    print(f"\nYour score is: {score:.2f} out of 100")

if __name__ == "__main__":
    math_level_measurement()



