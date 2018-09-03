# import os
# import io
# from pandas import DataFrame
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import train_test_split
#
# def readFiles(path):
#     for root, dirnames, filenames in os.walk(path):
#         for filename in filenames:
#             path = os.path.join(root, filename)
#
#             inBody = False
#             lines = []
#             f = io.open(path, 'r', encoding='latin1')
#             for line in f:
#                 if inBody:
#                     lines.append(line)
#                 elif line == '\n':
#                     inBody = True
#             f.close()
#             message = '\n'.join(lines)
#             yield path, message
#
#
# def dataFrameFromDirectory(path, classification):
#     rows = []
#     index = []
#     for filename, message in readFiles(path):
#         rows.append({'message': message, 'class': classification})
#         index.append(filename)
#
#     return DataFrame(rows, index=index)
#
# train_data = DataFrame({'message': [], 'class': []})
# test_data = DataFrame({'message': [], 'class': []})
#
# spam_train, spam_test = train_test_split(dataFrameFromDirectory('data_files/emails/spam', 'spam'))
# ham_train, ham_test = train_test_split(dataFrameFromDirectory('data_files/emails/ham', 'ham'))
#
# train_data = train_data.append(spam_train, 'spam')
# train_data = train_data.append(ham_train, 'ham')
# print('train_data count: ', train_data.count())
#
# test_data = test_data.append(spam_test, 'spam')
# test_data = test_data.append(ham_test, 'ham')
# # print('test_data count: ', test_data.count())
# # print('test_data: ', test_data.head())
# # split up each message into list of words and give it to MultinomialNB classifier.
# vectorizer = CountVectorizer()
# counts = vectorizer.fit_transform(train_data['message'].values)
#
# # print(counts)
# classifier = MultinomialNB()
# targets = train_data['class'].values
# classifier.fit(counts, targets)
#
# # print(classifier)
#
# # examples = ['Win million dollars now!', 'Hi, how are you?']
# # example_counts = vectorizer.transform(examples)
# # print(example_counts)
# test_counts = vectorizer.transform(test_data['message'].values)
# # print(test_counts)
# predictions = classifier.predict(test_counts)
# print(predictions)
#
# #Measure accuracy of classifier on test data
# print(classifier.score(spam_test, ham_test, sample_weight=None))



import os
import io
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split


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

train, test = train_test_split(data, test_size=0.33)
# print(data.head())


# split up each message into list of words and give it to MultinomialNB classifier.
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(train['message'].values)

# print(counts)
classifier = MultinomialNB()
targets = train['class'].values
classifier.fit(counts, targets)

# print(classifier)

# examples = ['Win million dollars now!', 'Hi, how are you?']
test_counts = vectorizer.transform(test['message'].values)
# print(example_counts)
predictions = classifier.predict(test_counts)
print(predictions)

# #Measure accuracy of classifier on test data
# print(classifier.score(test, sample_weight=None))
