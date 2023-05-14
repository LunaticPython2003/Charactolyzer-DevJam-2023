import afinn
import nltk
import string
import re

# Define emotional score thresholds
rude_threshold = -5
satisfied_threshold = 2
unsatisfied_threshold = -2
angry_threshold = -5
sad_threshold = -3
happy_threshold = 4

with open('test.txt', 'r') as file:
    text = file.read()

# Define a regular expression to match the different parts of the text
pattern = re.compile(r'(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}) - (.+?): (.+)')

# Find all matches of the regular expression in the text
matches = pattern.findall(text)
text = ""
# Loop over each match and extract the features
for date, time, name, body in matches:
    # Convert the text to the correct character encoding
    print(f'Date: {date}')
    print(f'Time: {time}')
    print(f'Name: {name}')
    print(f'Body: {body}')
    text = body


text = ''.join([char for char in text if char in string.printable])
text = text.lower()
words = nltk.word_tokenize(text)
stop_words = set(nltk.corpus.stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

afinn = afinn.Afinn()
score = afinn.score(text)
print(score)


if score <= rude_threshold:
    emotion = 'rude'
elif score >= happy_threshold:
    emotion = 'happy'
elif score >= satisfied_threshold:
    emotion = 'satisfied'
elif score <= unsatisfied_threshold:
    emotion = 'unsatisfied'
elif score <= angry_threshold:
    emotion = 'angry'
elif score <= sad_threshold:
    emotion = 'sad'

print(f'The emotion of the text is {emotion}.')
