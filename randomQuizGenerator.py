import random

#Quiz Data
maths = {'2 + 6': '8', '10 + 11': '21', '3 + 3': '6', '33 + 27': "60",
            '2 + 9': '11', '3 + 6': '9', '7 + 10': '17', '18 + 22': '40',
            '19 + 34': '53', '44 + 11': '55'}

#Quiz for loop (making a paper for each student)
for quizNo in range (10): #number of students
    #Question and answer files
    quizFile = open(f'mathsQuiz{quizNo + 1}.txt', 'w')
    answerFile = open(f'mathsQuizAnswers{quizNo + 1}.txt', 'w')
    #Paper heading
    quizFile.write('Name:\n\nDate:\n\n') #For user to fill
    quizFile.write(('' * 20) + f'Maths Quiz (Form {quizNo + 1})')
    quizFile.write('\n\n')
    #Suffle order of answers
    answer = list(maths.keys())
    random.shuffle(answer)
    
    for questionNo in range(10):
        #Finding the right and wrong answers
        correctAns = maths[answer[questionNo]]
        wrongAns = list(maths.values())
        del wrongAns[wrongAns.index(correctAns)]
        wrongAns = random.sample(wrongAns, 3)
        answerOptions = wrongAns + [correctAns]
        random.shuffle(answerOptions)
        #Write out the options
        quizFile.write(f'{questionNo + 1}. What is the answer to {answer[questionNo]}?\n')
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}. { answerOptions[i]}")
            quizFile.write('\n')
        #Write the answer key
        answerFile.write(f"{questionNo + 1}. {'ABCD'[answerOptions.index(correctAns)]}\n")
        
                            
