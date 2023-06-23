import random
import nltk
from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.corpus import names
from bgnames import boys, girls
import tkinter as tk


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


# Define a function to handle button click events
def predict_gender():
    name = name_entry.get().lower().strip()

    # Predict the gender of the name using the trained classifier
    features = gender_features(name)
    prob_male = classifier.prob_classify(features).prob('male')
    prob_female = classifier.prob_classify(features).prob('female')

    # Update the output label with the predicted gender and probabilities
    prediction_label.config(text=f'{name.capitalize()} is a {"boy" if prob_male > prob_female else "girl"} name ({prob_male*100:.0f}% boy, {prob_female*100:.0f}% girl)')


# Create the main window
root = tk.Tk()
root.title('Name Gender Classifier')

# Make the window non-resizable
root.resizable(False, False)

# Add a label and entry box for the name input
name_label = tk.Label(root, text='Enter a name:')
name_label.pack(side=tk.LEFT)
name_entry = tk.Entry(root)
name_entry.pack(side=tk.LEFT)

# Add a button to predict the gender of the name
predict_button = tk.Button(root, text='Predict', command=predict_gender)
predict_button.pack(side=tk.LEFT)

# Add a label to display the predicted gender and probabilities
prediction_label = tk.Label(root, text='')
prediction_label.pack()

# Start the main event loop
root.mainloop()
