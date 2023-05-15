from afinn import Afinn
import nltk
import string
import re
import streamlit as st

def predict(names, index = 0, score = 0):
    if index == len(names):
        return score/len(names)
    text = names[index]
    text = ''.join([char for char in text if char in string.printable])
    text = text.lower()
    words = nltk.word_tokenize(text)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]

    afinn = Afinn()
    score += afinn.score(text)
    print(score)
    return predict(names, index+1, score)

rude_threshold = -5
satisfied_threshold = 2
unsatisfied_threshold = -2
angry_threshold = -5
sad_threshold = -3
happy_threshold = 4

def character(score):
    if score == 0:
        emotion = 'neutral'
    elif score == 1:
        emotion = 'polite'
    elif score <= rude_threshold:
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
    return emotion

def main():
    with open('uploads/test.txt', 'r') as file:
        text = file.read()

    pattern = re.compile(r'(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}) - (.+?): (.+)')

    matches = pattern.findall(text)
    analyze = dict()
    for date, time, name, body in matches:
        print(f'Date: {date}')
        print(f'Time: {time}')
        print(f'Name: {name}')
        print(f'Body: {body}')
        if name not in analyze:
            analyze[name] = [body]
        else:
            analyze[name].append(body)

    print(analyze)
    scores = dict()
    prediction = dict()
    for i in analyze.keys():
        temp = analyze[i]
        scores[i] = predict(temp)
        prediction[i] = character(int(scores[i]))
    st.write('The individual scores are - ')
    st.write(scores)
    return prediction