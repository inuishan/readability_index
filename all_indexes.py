#!/usr/bin/env python
# -*- coding: utf-8 -*-


from os import listdir
from os.path import isfile, join
import math

PATH = './corpus/'



def ARI_hindi():
	# characters, words, sentences
	onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
	dic = {}
	ari = {}
	for filename in onlyfiles:
		with file(PATH+filename) as f:
			s = f.read()
    		sentences = s.split("।")
    		sentences = len(sentences)
    		words_list = s.split(" ")
    		tot_words = len(words_list)
    		tot_chars = sum(map(len, words_list))
    		dic[filename] = (sentences,tot_words,tot_chars)
    		ARI = (4.71*float(tot_chars)/float(tot_words))+0.5*(float(tot_words)/float(sentences)) - 21.43
    		ari[filename] = ARI
	return dic,ari

def Colemon_Lieu():
	# characters, words, sentences
	onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
	dic = {}
	ari = {}
	for filename in onlyfiles:
		with file(PATH+filename) as f:
			s = f.read()
    		sentences = s.split("।")
    		sentences = len(sentences)
    		words_list = s.split(" ")
    		tot_words = len(words_list)
    		tot_chars = sum(map(len, words_list))
    		hun_words = float(tot_words)/100
    		L = float(tot_chars)/hun_words
    		S = float(sentences)/hun_words
    		dic[filename] = (L,S)
    		CL = 0.0588*L - 0.296*S - 15.8
    		ari[filename] = CL
	return dic,ari	

vowelsTemp = ['ँ', 'ं', 'ः', '़', 'ा', 'ि', 'ी', 'ु', 'ू', 'ृ', 'ॄ', 'ॢ' ,'े', 'ै', 'ो', 'ौ']
vowels2Temp = ['अ','आ','इ','ई','उ','ऊ','ए','ऐ','ओ','औ']
vowels = [i.decode('utf-8') for i in vowelsTemp]
vowels2 = [i.decode('utf-8') for i in vowels2Temp]
def fleschReadingEase():

	onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
	dic = {}
	ari = {}
	for filename in onlyfiles:
		tot_syllables = 0
		with file(PATH+filename) as f:
			s = f.read()
    		sentences = s.split("।")
    		sentences = len(sentences)
    		words_list = s.split(" ")
    		for word in words_list:
    			word = word.decode('utf-8')
    			for i in range(len(word)):
    				if word[i] not in vowels and word[i] not in vowels2:
    					if (i+1)<len(word) and (word[i+1] in vowels or word[i+1] in vowels2):
    						tot_syllables+=1 

    		tot_words = len(words_list)
    		tot_chars = sum(map(len, words_list))
    		FRE = 206.835 - 1.015*float(tot_words)/float(sentences) - (84.6*float(tot_syllables)/float(tot_words))
    		dic[filename] = (tot_syllables)
    		ari[filename] = FRE
	return dic,ari	

def fleschKincaidReadingEase():

	onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
	dic = {}
	ari = {}
	for filename in onlyfiles:
		tot_syllables = 0
		with file(PATH+filename) as f:
			s = f.read()
    		sentences = s.split("।")
    		sentences = len(sentences)
    		words_list = s.split(" ")
    		for word in words_list:
    			word = word.decode('utf-8')
    			for i in range(len(word)):
    				if word[i] not in vowels and word[i] not in vowels2:
    					if (i+1)<len(word) and (word[i+1] in vowels or word[i+1] in vowels2):
    						tot_syllables+=1 

    		tot_words = len(words_list)
    		tot_chars = sum(map(len, words_list))
    		FRE = 0.39*float(tot_words)/float(sentences) + (11.8*float(tot_syllables)/float(tot_words)) - 15.59
    		dic[filename] = (tot_syllables)
    		ari[filename] = FRE
	return dic,ari		
def SMOG():

	onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
	dic = {}
	ari = {}
	for filename in onlyfiles:
		with file(PATH+filename) as f:
			polysyll = 0
			s = f.read()
    		sentences = s.split("।")
    		sentences = len(sentences)
    		words_list = s.split(" ")
    		for word in words_list:
				tot_syllables = 0
				word = word.decode('utf-8')
				for i in range(len(word)):
					if word[i] not in vowels and word[i] not in vowels2:
						if (i+1)<len(word) and (word[i+1] in vowels or word[i+1] in vowels2):
							tot_syllables+=1
				if(tot_syllables>=3):
					polysyll+=1			

    		tot_words = len(words_list)
    		tot_chars = sum(map(len, words_list))
    		grade = 1.0430*math.sqrt(polysyll*30/sentences)+3.1291
    		dic[filename] = (polysyll)
    		ari[filename] = grade
	return dic,ari	
def linsearWrite():
	onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
	dic = {}
	ari = {}
	for filename in onlyfiles:
		with file(PATH+filename) as f:
			polysyll = 0
			s = f.read()
    		sentences = s.split("।")
    		sentences = len(sentences)
    		words_list = s.split(" ")
    		for word in words_list:
				tot_syllables = 0
				word = word.decode('utf-8')
				for i in range(len(word)):
					if word[i] not in vowels and word[i] not in vowels2:
						if (i+1)<len(word) and (word[i+1] in vowels or word[i+1] in vowels2):
							tot_syllables+=1
				if(tot_syllables>=3):
					polysyll+=1			

    		tot_words = len(words_list)
    		tot_chars = sum(map(len, words_list))
    		easy_words = tot_words - polysyll
    		raw_index = easy_words + 3*polysyll
    		if raw_index>20:
    			grade = raw_index/2
    		else: grade = (raw_index-2)/2
    		dic[filename] = (polysyll)
    		ari[filename] = grade
	return dic,ari	


def LIX():
	onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
	dic = {}
	ari = {}
	for filename in onlyfiles:
		with file(PATH+filename) as f:
			long_words = 0
			polysyll = 0
			s = f.read()
    		sentences = s.split("।")
    		sentences = len(sentences)
    		words_list = s.split(" ")
    		for word in words_list:
				length = len(word)
				if length>6:
					long_words+=1

    		tot_words = len(words_list)
    		tot_chars = sum(map(len, words_list))
    		grade = (tot_words/sentences)+(long_words*100)/tot_words
    		dic[filename] = (polysyll)
    		ari[filename] = grade
	return dic,ari



def GunningFog():

	onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
	dic = {}
	ari = {}
	for filename in onlyfiles:
		with file(PATH+filename) as f:
			polysyll = 0
			s = f.read()
    		sentences = s.split("।")
    		sentences = len(sentences)
    		words_list = s.split(" ")
    		for word in words_list:
				tot_syllables = 0
				word = word.decode('utf-8')
				for i in range(len(word)):
					if word[i] not in vowels and word[i] not in vowels2:
						if (i+1)<len(word) and (word[i+1] in vowels or word[i+1] in vowels2):
							tot_syllables+=1
				if(tot_syllables>=3):
					polysyll+=1			

    		tot_words = len(words_list)
    		tot_chars = sum(map(len, words_list))
    		grade = 0.4*(float(tot_words)/float(sentences)+100*float(polysyll)/float(tot_words))
    		dic[filename] = (polysyll)
    		ari[filename] = grade
	return dic,ari		

if __name__ == '__main__':
	x,y = GunningFog()	
	print x
	print y

