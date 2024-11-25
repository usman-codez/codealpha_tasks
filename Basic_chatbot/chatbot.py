import random

helo = ['hi','hello','hello there','good day']
bye = ['bye','good bye','have a good day','see you later']
howareyou = ['how are you','how are you doing','whats up']
name = ['whats your name','what is your name','do you have any name','What should i call you']
farm = ['i want to buy milk','what you offer','what i should buy','is anything specific']
open = ['when you guys open','time','specific hours','timing of farm']

print('-------------------------------------------\n')

while True:
    user = input('Ask anything: ').lower()
    if user in helo:
        bot_ans = ['Hi','Hi there','Hey whats up','How i can help you']
        print('Bot-ans:',random.choice(bot_ans),'\n')
    elif user in bye:
        bot_ans = ['Bye','See you again','Good day','Good day']
        print('Bot-ans:', random.choice(bot_ans), '\n')
    elif user in howareyou:
        bot_ans = ['Im good','Doing great thanks for asking','Im doing great']
        print('Bot-ans:', random.choice(bot_ans), '\n')
    elif user in name:
        bot_ans = ['Im minko bot','My name is minko bot','You can call me minko bot']
        print('Bot-ans:', random.choice(bot_ans), '\n')
    elif user in farm:
        bot_ans = ['Yeah,You can buy milk','Our milk is one of the best','Milk of our dairy farm is so pure']
        print('Bot-ans:', random.choice(bot_ans), '\n')
    elif user in open:
        bot_ans = ['We are open from 9am to 9pm','9am to 9pm','12 hours of day']
        print('Bot-ans:', random.choice(bot_ans), '\n')

    else:
        print('Bot-ans: Sorry I dont get that')