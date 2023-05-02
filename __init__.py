from math_game import add

def game():
    score = 0
    while True:
        print('======== Menu ========\n1. Add\n2. Subtract\n3. Multiply')
        operation = int(input('Choose an operation:\n'))
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))
        answer = int(input('Enter your answer: \n'))
        if operation == 1:
            result = add(num_1, num_2)
        elif operation == 2:
            result = num_1 - num_2
        elif operation == 3:
            result = num_1 * num_2
        else:
            print('Invalid operation!')
            continue
        
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
            break
        
    print(f'======== Game Over ========\nYour score is {score}\nKeep going!')

game()
