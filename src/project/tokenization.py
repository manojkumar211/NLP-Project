import nltk
from data import content
from nltk.tokenize import sent_tokenize, word_tokenize


sent_token=sent_tokenize(content)

word_token=word_tokenize(content)

print('Sentence Tokenizer :',sent_token)
print("##"*30)
print('Word Tokenizer :',word_token)
print("##"*30)
