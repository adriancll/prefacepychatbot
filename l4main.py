import random
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.corpus import names
from bgnames import boys, girls



# Define a function to extract features from a given name
def gender_features(name):
    return {'last_letter': name[-1]}

# Extract features from the names and label them as male or female
labeled_names = ([(name, 'male') for name in boys] + [(name, 'female') for name in girls])
random.shuffle(labeled_names)

# Split the labeled names dataset into training and testing sets
split_ratio = 0.8 # 80% training data and 20% testing data
split_index = int(len(labeled_names) * split_ratio)
train_names = labeled_names[:split_index]
test_names = labeled_names[split_index:]

# Use the training set to train a Naive Bayes classifier
train_set = [(gender_features(name), gender) for (name, gender) in train_names]
classifier = NaiveBayesClassifier.train(train_set)

# Evaluate the accuracy of the classifier using the testing set
test_set = [(gender_features(name), gender) for (name, gender) in test_names]
print('Accuracy:', accuracy(classifier, test_set))

# Wait for user input and predict the gender of the name using the trained classifier
while True:
    name = input('Enter a name: ').lower().strip()
    if name == 'exit':
        break
    features = gender_features(name)
    prob_male = classifier.prob_classify(features).prob('male')
    prob_female = classifier.prob_classify(features).prob('female')
    print(f'{name.capitalize()} is a {"boy" if prob_male > prob_female else "girl"} name ({prob_male*100:.0f}% boy, {prob_female*100:.0f}% girl)')
