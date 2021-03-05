import nltk
import re
import numpy as numpy
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

f_positive = open("good_news.txt","r", encoding="utf8")
positive_news_data = f_positive.read()
f_positive.close()

f_negative = open("bad_news.txt","r", encoding="utf8")
negative_news_data = f_negative.read()
f_negative.close()

lemmatizer = nltk.stem.WordNetLemmatizer()
remove_punctuation = dict((ord(punctuation), None) for punctuation in string.punctuation)

# lists of good bad words

# check__possibility__functions

def check_prob_positive(user_input,sentence_list,article_words):
	chatbot_response = ''
	sentence_list.append(user_input)
	word_vectors = TfidfVectorizer(tokenizer=RemovePunctuations, stop_words='english')
	vectorized_words = word_vectors.fit_transform(sentence_list)
	similarity_values = cosine_similarity(vectorized_words[-1],vectorized_words)
	similar_sentence_number = similarity_values.argsort()[0][-2]
	similar_vectors = similarity_values.flatten()
	similar_vectors.sort()
	matched_vectors = similar_vectors[-2]
	if(matched_vectors==0):
		return 0
	else:
		return matched_vectors
def check_prob_negative(user_input,sentence_list,article_words):
	chatbot_response = ''
	sentence_list.append(user_input)
	word_vectors = TfidfVectorizer(tokenizer=RemovePunctuations, stop_words='english')
	vectorized_words = word_vectors.fit_transform(sentence_list)
	similarity_values = cosine_similarity(vectorized_words[-1],vectorized_words)
	similar_sentence_number = similarity_values.argsort()[0][-2]
	similar_vectors = similarity_values.flatten()
	similar_vectors.sort()
	matched_vectors = similar_vectors[-2]
	if(matched_vectors==0):
		return 0
	else:
		return matched_vectors

def LemmatizeWords(words):
	return [lemmatizer.lemmatize(word) for word in words]
def RemovePunctuations(text):
	return LemmatizeWords(nltk.word_tokenize(text.lower().translate(remove_punctuation)))
def thinking(question):
	question = question.lower()

	sentence_list_positive = nltk.sent_tokenize(positive_news_data)
	article_words_positive = nltk.word_tokenize(positive_news_data)

	sentence_list_negative = nltk.sent_tokenize(negative_news_data)
	article_words_negative = nltk.word_tokenize(negative_news_data)
	
	positive_prob = check_prob_positive(question, sentence_list_positive,article_words_positive)
	negative_prob = check_prob_negative(question, sentence_list_negative,article_words_negative)

	if(negative_prob>positive_prob):
		return "It seems to be bad news."
	elif(negative_prob==positive_prob):
		return "Either Neautral news"
	else:
		return "That must be a good news."
	# return "+ve: "+str(positive_prob)+"  ; -ve: "+str(negative_prob)
