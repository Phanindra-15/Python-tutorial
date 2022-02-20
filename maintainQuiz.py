

import pickle
from question import Question 

while True:
    print('1. Create a new quiz file')
    print('2. Add questions to an existing quiz file')
    print('3. Exit')
    
    choice = input('Enter your choice : ')

    if choice!='1' and choice !='2':
        break

    with open('quizTopics.txt', 'r') as file:
        topics = [topic.strip() for topic in file.readlines()]
       
    if choice == '1':
        topic = input('Enter the new topic : ')
        if topic in topics:
            print("This topic is already present, choose option2 to add questions to the existing file")
            continue
        with open('quizTopics.txt', 'a') as file:
            file.write(f'{topic}\n')
        questions_list = []  
    else: 
        print(f'\nAvailable topics : {topics}')
        topic = input('Enter the topic in which you want to add questions : ')
        if topic not in topics:
            print('This topic not included still, choose option 1 to create a new quiz file')
            continue
                
        filename = topic.lower().replace(' ','') + '.pck' 
        with open(filename, 'rb') as file:
            questions_list = pickle.load(file)

        print(f'This topic has {len(questions_list)} questions\n')
        for question in questions_list:
            print(f' - {question.text}\n')
        
    #Enter questions in questions_list
    while True:
        question = Question()
        question.enter_details()
        questions_list.append(question)
        response = input('Want to enter another question(y/n) :')
        if response == 'n':
            break

    #write question_list to the file
    filename = topic.lower().replace(' ','') + '.pck'
    with open(filename, 'wb') as file:
        pickle.dump(questions_list,file)
        