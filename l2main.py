# while something:
        # response = input('How are you')
        # if response equals to quit, then we end loop
        # perform sentiment analysis

import random
from textblob import TextBlob
#import openai

Postive = ["That's great to hear! Is there anything I can assist you with today?", "Glad to know you're doing well!", "Awesome! If you have any questions or concerns, feel free to let me know.", "Wonderful! Is there anything specific you would like to talk about or discuss?", "Fantastic! Let me know if there is anything I can do for you."]
Negative = ["I'm sorry to hear that. Is there anything I can do to help you feel better?", "I'm sorry to hear that you are not doing well. Would you like to talk about what's been bothering you?", "I'm sorry to hear that. If you need someone to listen or support you.","'im sorry to hear that. If there's anything you'd like to talk about or if you need any assistance, I'm here for you."]
Normal = ["Good to hear that you're alright! Is there anything you would like to discuss or ask me about?", "Glad to know you're doing okay! Let me know if there's anything I can do to help make your day better.", "Alright is better than not alright, right? If there's anything that you need help with, just let me know.", "Great to hear that you're doing alright! Is there anything specific on your mind that you'd like to chat about?", "Sounds good to me! If you ever need any assistance or support from me, don't hesitate to reach out."]


    

while True:
    user_input = input('How are you? (type quit to quit)')
    if user_input.lower() == 'quit':
        print("Thanks you, see you next time")
        break
    else:
        response_after_sentiment_analysis = TextBlob(user_input)
        score = response_after_sentiment_analysis.sentiment.polarity
        if score > 0:
            print(random.choice(Postive))
        elif score == 0:
            print(random.choice(Normal))
        else: 
            print(random.choice(Negative))
    
        
