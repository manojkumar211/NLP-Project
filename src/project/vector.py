import nltk
from text_clean import corpus
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

cv=TfidfVectorizer()
bow=cv.fit_transform(corpus).toarray()

tf=TfidfVectorizer()
tfid=tf.fit_transform(corpus).toarray()

print("Count Vector Matrix :",bow)
print("##"*30)
print("TF-IDF Vector Matrix :",tfid)
