from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'home/home.html')



def even_odd_game(request):
    if request.method == 'GET':
        return render(request, 'game/even_odd_game.html')
    
    elif request.method == 'POST':
        user_input = request.POST.get('user_input', '').lower()
        try:
            if user_input == 'x':
                return JsonResponse("Exiting the program. Thank you!", safe=False)
            else:
                user_input = int(user_input)
                if user_input % 2 == 0:
                    return JsonResponse(f"Your number [{user_input}] is even", safe=False)
                else:
                    return JsonResponse(f"Your number [{user_input}] is odd", safe=False)
        except ValueError:
            return JsonResponse({'Ops':"Invalid input. Please enter a valid number or 'x' to exit."})
    else:
        return HttpResponse("Invalid request method.")

    
def multiplication_game(request):
    if request.method == 'GET':
        return render(request, 'game/multiplication_game.html')
    elif request.method == 'POST':
        user_input1 = request.POST.get('first_number', '')
        user_input2 = request.POST.get('second_number', '')

        try:
            a = int(user_input1)
            b = int(user_input2)

            def game(a, b):
                result = ""
                for num in range(a, b + 1):
                    result += f"----------------------------------<br>"
                    result += f"The Multiplication table for {num}<br>"
                    for i in range(1, 13):
                        result += f"[{num} x {i}] = {num * i}<br>"
                return result

            return JsonResponse({"result": game(a, b)})
        
        except ValueError:
            return JsonResponse({"result": "Invalid input. Please enter valid numbers."})
    
    else:
        return JsonResponse({"result": "Invalid request method."})

def summation_game(request):
    if request.method == 'GET':
        return render(request, 'game/summation.html')
    elif request.method == 'POST':
        num_input = request.POST.get('num_input', '').lower()

        try:
            if num_input == 'x':
                return JsonResponse({"result": "Exiting the program. Thank you!"})
            else:
                num = int(num_input)
                numbers = []

                for x in range(num):
                    while True:
                        user_num = input(f"Enter number [{x + 1}] ('x' to exit): ")
                        if user_num.lower() == "x":
                            return JsonResponse({"result": "Exiting the program. Thank you!"})
                        try:
                            user_num = int(user_num)
                            numbers.append(user_num)
                            break
                        except ValueError:
                            return JsonResponse({"result": "Invalid input. Please enter a valid number or 'x' to exit."})

                number_sum = sum(numbers)
                average = number_sum / num

                result = {
                    "numbers": numbers,
                    "sum": number_sum,
                    "average": average
                }

                return JsonResponse({"result": result})
        except ValueError:
            return JsonResponse({"result": "Invalid input. Please enter a valid number or 'x' to exit."})
    else:
        return JsonResponse({"result": "Invalid request method."})
    


import math
import random

def math_level(request):
    if request.method == 'POST':
        return render(request, 'math_level_result.html', process_math_level())
    return render(request, 'game/math_level.html')

def process_math_level():
    print("Welcome to the Math Level Measurement Program!")
    print("-----solve five questions for this test-------")

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

    for i, equation in enumerate(random.choices(equations, k=6), start=1):
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

    return {'user_answers': user_answers, 'score': score}
