import os
import io
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)

            inBody = False
            lines = []
            f = io.open(path, 'r', encoding='latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
            f.close()
            message = '\n'.join(lines)
            yield path, message


def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class': classification})
        index.append(filename)

    return DataFrame(rows, index=index)


data = DataFrame({'message': [], 'class': []})

data = data.append(dataFrameFromDirectory('data_files/emails/spam', 'spam'))
data = data.append(dataFrameFromDirectory('data_files/emails/ham', 'ham'))

# print(data.head())


# split up each message into list of words and give it to MultinomialNB classifier.
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

print(counts)
classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)

# print(classifier)

examples = ['Win million dollars now!', 'Hi, how are you?']
example_counts = vectorizer.transform(examples)
print(example_counts)
predictions = classifier.predict(example_counts)
print(predictions)

