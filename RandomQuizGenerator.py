#! python3
# Project: Random Quiz Generator (Country-Capital_Quiz
# Creates quizzes with questions and answers in random order, along with the answer key.

import random
import sys

# The quiz data. Keys are states and values are their capitals.
country_capitals = {
    'Afghanistan': 'Kabul',
    'Albania': 'Tirana',
    'Algeria': 'Algiers',
    'Andorra': 'Andorra la Vella',
    'Angola': 'Luanda',
    'Argentina': 'Buenos Aires',
    'Armenia': 'Yerevan',
    'Australia': 'Canberra',
    'Austria': 'Vienna',
    'Belgium': 'Brussels',
    'Brazil': 'Brasília',
    'Canada': 'Ottawa',
    'China': 'Beijing',
    'Colombia': 'Bogotá',
    'Czech Republic': 'Prague',
    'Denmark': 'Copenhagen',
    'Egypt': 'Cairo',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Greece': 'Athens',
    'Hungary': 'Budapest',
    'India': 'New Delhi',
    'Indonesia': 'Jakarta',
    'Iran': 'Tehran',
    'Iraq': 'Baghdad',
    'Ireland': 'Dublin',
    'Italy': 'Rome',
    'Japan': 'Tokyo',
    'Kenya': 'Nairobi',
    'Mexico': 'Mexico City',
    'Netherlands': 'Amsterdam',
    'Nigeria': 'Abuja',
    'Norway': 'Oslo',
    'Pakistan': 'Islamabad',
    'Peru': 'Lima',
    'Philippines': 'Manila',
    'Poland': 'Warsaw',
    'Portugal': 'Lisbon',
    'Russia': 'Moscow',
    'Saudi Arabia': 'Riyadh',
    'South Africa': 'Pretoria',
    'South Korea': 'Seoul',
    'Spain': 'Madrid',
    'Sweden': 'Stockholm',
    'Switzerland': 'Bern',
    'Turkey': 'Ankara',
    'United Kingdom': 'London',
    'United States': 'Washington, D.C.',
    'Venezuela': 'Caracas',
    'Vietnam': 'Hanoi',
}

# Generate 25 Quiz Files
for quizNum in range(25):
    # Create the quiz and answer key files
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'Country Capital Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Shuffle the order of the countries.
    countries = list(country_capitals.keys())
    random.shuffle(countries)

    # Loop through all the 50 countries, making a question for each.
    for questionNum in range(50):

        # Get right and wrong answers.
        correctAnswers = country_capitals[countries[questionNum]]
        wrongAnswers = list(country_capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswers]
        random.shuffle(answerOptions)

        # Write the question and the answer options to the quiz file.
        quizFile.write('%s. What is the capital of %s?\n' % (questionNum + 1, countries[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        # Write the answer to a file.
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswers)]))

    quizFile.close()
    answerKeyFile.close()

# while True:
#     print('Type \"Exit\" to exit.')
#     response = input().capitalize()
#     if response == 'Exit':
#         sys.exit()
#     print(f'You typed {response}.')
