import nltk 
import re
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
nltk.download('punkt_tab')
nltk.download('stopwords')

def summarize(text,size):
    text=re.sub(r'\s+',' ',text) #this removes spaces in text
    text=re.sub(r'\[[0-9*\]]',' ',text) #removes number references

    sentences = sent_tokenize(text)
    totsentence = len(sentences) #to get len for summary length
    words = word_tokenize(text) # We tokenised sentece and words

    useless = set(stopwords.words('english'))# removes usless words like is or etc

    word_frequencies = {} #couting word freq for imp words
    for word in words:
        if word not in useless and word.isalpha():
            word_frequencies[word] = word_frequencies.get(word,0) + 1
    
    sentence_score = {} #sentence score for imp key words
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                sentence_score[sent]=sentence_score.get(sent,0) + word_frequencies[word]

    if size==1:
        numb=max(1,totsentence//7)
    elif size==2:
        numb=max(2,totsentence//3)
    else:
        numb=max(3,totsentence//8) #here we set how much we want summary in size

    summary_sentences=heapq.nlargest(numb,sentence_score,key=sentence_score.get)
    summary = ' '.join(summary_sentences)

    return summary
