import nltk
nltk.download()


my_file=open("C:/AI&ML Engineer/Projects/NLP/text.txt","r",encoding='utf8')

content=my_file.read()

my_file.close()

print("Text Content :",content)
print("##"*30)