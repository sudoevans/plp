#Multiple choice game

# 1 question and choices, then we collect the correct answers based on comparison wirh the user input.__annotations__
# we need to have a list of the choices and the questions and another dictionary with questions and correct answers.

"""
1. How do we print to the console in python?
a. print
b. std.println
c. cout
d. stringwrite.write
"""
questions={
    1:"How do we print to the console in python?",
    2:"What is the best programming language for AI and ML"
}
choices={
    1:{

        "a":'print',
        "b":"std.println",
        "c":"cout",
        "d":"stringwrite.write"
    },

    2:{

        "a":'VBA',
        "b":"Fortan",
        "c":"Assembly",
        "d":"Python"
    },
    
}

answers={
    1:'a',
    2:'b',
    3:'d'
}

# print(answers[1])

# print(questions[1])
# query=input()

# def answer_checker(n,choice):
#     if questions[n]:
#         if choice[n]==answers[n]:
#             True
#         else:
#             False

for i in range(1,len(questions)):
        count_correct=0
        print(f'{questions[i]}')
        for j in range(1,3):
            print(choices[1])
            choice=input("What is your choice?: ")
            # result=answer_checker(i,choice)
            result= True if choice==answers[i] else False
            if result==True:
                print('Correct!')
                count_correct+=1
            else:
                 print("You missed it, try next time :(")
        i+=1
    


    

