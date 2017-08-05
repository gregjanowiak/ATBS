#! /usr/bin/env python3
import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
   'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
   'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# create quiz and answer key files
for quizNum in range(35): # for loop to create 35 quiz txt files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w') # open file objects in write mode
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # write the header for the quiz and format appropriately
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # shuffle the order of the states
    states = list(capitals.keys()) # set states as a list of the keys from capitals
    random.shuffle(states) # shuffle with the random module

    # loop through all states, make question for each
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]] # set correctAnswer as the value in capitals by the questionNum index for states in the current loop
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)] # remove the correctAnswer by finding the index in wrongAnswers using the index method
        wrongAnswers = random.sample(wrongAnswers, 3) # pick three random wrong answers
        answerOptions = wrongAnswers + [correctAnswer] # append all answers together in a list
        random.shuffle(answerOptions) # shuffle the list of answers

        # write the question and answer options to the quiz file
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum])) # ask for the capital of a state, using questionNum as the index value
        for i in range(4): # loop 4 times to go through ABCD and answerOptions defined in last loop
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i])) # i makes the statement go through each option one by one per loop
            quizFile.write('\n')

        # write the answer key file
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnswer)])) # write ABCD option that corresponds to the correctAnswer, using correctAnswer as the index value
    quizFile.close()
    answerKeyFile.close() # close the files with the top-level for loop, otherwise you'll get a ValueError
