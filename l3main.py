import random
from difflib import get_close_matches

def find_best_match(user_question: str, questions: list[str]) -> str | None:
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


question_responses = {
    'greetings': {
        'patterns': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'whats up?', 'howdy', 'greetings', 'nice to see you', 'hey there', 'yo', 'whats up', 'hiya', 'hey man', 'sup'],
        'responses': ['Hello!', 'Hi there!', 'Hey!', 'Morning!', 'Good afternoon!', 'Good evening!', 'Not much!', 'Howdy!', 'Greetings!', 'Great to see you!', 'Hello to you too', 'Yo!', 'Hey, whats going on?', 'Hi, how are you?', 'Hey, good to see you!', 'Hi! How have you been?', 'Hello there!', 'Hey buddy!', 'Whats new?', 'Hows it going?', 'Nice to meet you!', 'Pleased to meet you!', "What have you been up to?", "How's your day going?", "Good to see you, how've you been?" ]
    },
    'farewell': {
        'patterns': ['bye!', 'see you', 'goodbye', 'take care', 'farewell', 'catch you later', 'later', 'have a good one', 'see you later', 'bye for now', 'so long', 'talk to you later', 'take care of yourself', 'until we meet again'],
        'responses': ['Bye!', 'Goodbye!', 'See you!', 'Take care!', 'Farewell!', 'Catch you later!', 'Later!', 'Have a nice day!', 'Goodbye and take care!', 'Until next time!', 'Take it easy!', 'Peace out!', 'See ya!', 'Have a good one!', 'Ill see you later!', 'Bye for now!', 'So long!', 'Talk to you later!', 'Take care of yourself!', 'Until we meet again!', "Goodnight!", "Sleep well!", "Farewell, friend!", "See you soon!" ]
    },
    'jokes': {
        'patterns': ['tell me a joke', 'say something funny', 'make me laugh', 'give me a chuckle', 'whats a good joke?'],
        'responses': ['Why did the tomato turn red? Because it saw the salad dressing!', 'Why dont scientists trust atoms? Because they make up everything!', 'Why do cows have hooves instead of feet? Because they lactose.', 'Why did the chicken cross the playground? To get to the other slide!', 'Why couldnt the bicycle stand up by itself? Because it was two-tired!', 'What do you call fake spaghetti? An impasta!', 'Why dont oysters share their pearls? Because theyre shellfish!', 'Why did the math book look sad? Because it had too many problems.', 'How does a penguin build its house? Igloos it together.']
    },
    'favorite_color': {
        'patterns': ['what is your favorite color?', 'do you like any colors?', 'what color do you like?', 'which color do you prefer?', 'any favorite color?', 'is there any color you like?', 'do you have a color preference?', 'what is your preferred color?', 'what color do you think is the best?', 'what color is the prettiest?', 'what color makes you happy?'],
        'responses': ['I am a machine learning model, so I do not have the ability to like or dislike colors.', 'As an AI language model, I do not have the capability to possess preferences or emotions, including a favorite color.', 'I dont have a favorite color, but I think all colors are beautiful in their own way.', 'There is no particular color that I prefer.', 'Colors are subjective and vary from person to person.', 'Which color do you like best?']
    },
    'weather': {
        'patterns': ['what is the weather like today?', 'what will be the temperature today?', 'is it going to rain today?', 'do I need an umbrella today?', 'will it be sunny today?', 'what is the forecast for tomorrow?', 'what is the weather like in [city]?', 'what is the temperature in [city]?'],
        'responses': ['To get the weather information, please provide me with your location or the city name.', 'Please specify the location or city name to get the weather information.', 'Sure, I can help you with the weather information. Could you please provide me with your location or the city name?', 'Let me check the weather forecast for you. Please tell me the location or city name.']
    }
}



while True:
    user_input = input("You: ")
    if user_input == "quit":
        break
    question = find_best_match(user_input.lower(), sum(question_responses.values(), []))
    response = ''
    if question:
        for intent, data in question_responses.items():
            if question in data['patterns']:
                response = random.choice(data['responses'])
                break
    if response == '':
        print("Sorry, I didn't understand your question. Could you please rephrase it?")
    else:
        print("Bot:", response)
