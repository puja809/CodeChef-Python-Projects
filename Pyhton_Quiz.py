import time
import random

"""Function to return question/answers:"""
def ques_ans():
    return [{"question": "Which keyword is used to define a function in Python?",
         "options": ["A) func", "B) define", "C) def", "D) function"], "answer": "C"},

        {"question": "What is the output of print(2 ** 3) in Python?",
         "options": ["A) 6", "B) 8", "C) 9", "D) 10"], "answer": "B"},

        {"question": "Which data type is mutable in Python?",
         "options": ["A) Tuple", "B) String", "C) List", "D) Integer"], "answer": "C"},

        {"question": "Which of the following is used to take input from the user?",
         "options": ["A) input()", "B) print()", "C) scan()", "D) read()"], "answer": "A"},

        {"question": "What will be the output of len('Python')?",
         "options": ["A) 5", "B) 6", "C) 7", "D) Error"], "answer": "B"}]

"""Function for CountDown:"""
def countdown_timer():
    for i in range(10,0,-1):
        print(f'\rTime left: {i} seconds',end='')
        time.sleep(1)
    print("\nTime's up!")


"""Function to get user answer and check if its correct or not:"""
def get_check_answer(user_choice,answer):
    opt=['A','B','C','D']
    if user_choice in opt and user_choice==answer:
        if user_choice==answer:
            return 1
        else:
            return 0

"""Score Update Function:"""

def update_score(score,result):
    if result==1:
        score+=1

    return score


"""Quiz Begins"""
def play_quiz():
    score=0
    ques = ques_ans()
    random.shuffle(ques)
    for i in range(len(ques)):
        print('\n=======================')
        print(f'Question {i + 1}: {ques[i]['question']}')
        for j in ques[i]['options']:
            print(j)
        countdown_timer()
        answer=ques[i]['answer']
        user_choice = input('Enter Your answer: ').upper().strip()
        result=get_check_answer(user_choice, answer)
        if result == 1:
            print('Correct Answer!')
            score=update_score(score, result)
            print(f'Your Score is {score}')
        elif result==0:
            print('Wrong Answer')
            print(f'Your Score is {score}')
        else:
            print('Invalid choice!!')

    print('\nThanks for playing the quiz!!')
    print(f'Your final score is: {score}')



if __name__=='__main__':
    play_quiz()

