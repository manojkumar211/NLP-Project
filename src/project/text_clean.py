import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from tokenization import sent_token, word_token

ps=PorterStemmer()

wl=WordNetLemmatizer()

corpus=[]

for i in range(len(sent_token)):

    punct=re.sub('[^a-zA-Z0-9]'," ",sent_token[i])
    punct_low=punct.lower()
    punct_split=punct_low.split()
    word_token=[wl.lemmatize(word) for word in punct_split if word not in (stopwords.words('english'))]
    word_join=' '.join(word_token)
    corpus.append(word_join)

print("Printing Corpus :",corpus)
print("##"*30)
