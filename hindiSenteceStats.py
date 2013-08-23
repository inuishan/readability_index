#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy
import sys
import os
import pickle
import simplejson
	

def sentenceLengthStats(corpus):
	files = []
	for (dirpath, dirname, filenames) in os.walk(corpus):
	    files.append([dirpath,filenames])

	totalDocs = 0
	lengths = []
	for direc in files:
		for afile in direc[1]:
			docPath = direc[0]+'/'+afile;
			totalDocs += 1
			print(docPath)
			f = open(direc[0]+'/'+afile,'r')
			sentences = f.read().strip().split('।')
			sentences = [sentence for sentence in sentences if sentence != '']
			lengths += [len(sentence.split()) for sentence in sentences]
			f.close()
	totalWords = sum(lengths)
	totalSentences = len(lengths)
	avgLength = float(totalWords)/totalSentences
	temp = 0
	for val in lengths:
		temp += math.pow((avgLength - val),2)
	standardDeviation = math.sqrt(float(temp)/totalSentences)

	median = numpy.median(numpy.asarray(lengths))
	maxLength = max(lengths)
	minLength = min(lengths)

	sentenceLengthResult = [avgLength, standardDeviation, median, minLength, maxLength, totalSentences, totalWords, totalDocs]

	
	print('\n\n--------------------------SentenceLengthResult-------------------------------')
	sys.stdout.flush()

	print('Corpus : ' + corpus + '\nTotal Docs : ' + str(totalDocs))
	print("-------------Sentence Length Stats----------------")
	print('Average Sentence Length : ' + str(sentenceLengthResult[0]) + '\nStandard Deviation : ' + str(sentenceLengthResult[1]) + '\nMedian : ' + str(sentenceLengthResult[2]) + '\nMin Sentence Length : ' + str(sentenceLengthResult[3]) + '\nMax Sentence Length : ' + str(sentenceLengthResult[4]) + '\nTotal Sentences : ' + str(sentenceLengthResult[5]) + '\nTotal Words : ' + str(sentenceLengthResult[6]))
	sys.stdout.flush()

	f = open('sentenceStatsProgData_pickle_' + str(corpus.split('/')[-3:]),'w')
	pickle.dump({'sentenceLengthResult_': sentenceLengthResult, 'lengths': lengths}, f)
	f.close()


	f = open('sentenceStatsProgData_json' + str(corpus.split('/')[-3:]),'w')
	simplejson.dump({'sentenceLengthResult': sentenceLengthResult, 'lengths': lengths}, f)
	f.close()



def sentenceLengthStarts_mine(corpus):
	files = []
	for (dirpath, dirname, filenames) in os.walk(corpus):
	    files.append([dirpath,filenames])

	totalDocs = 0
	lengths = []
	for direc in files:
		for afile in direc[1]:
			docPath = direc[0]+'/'+afile;
			totalDocs += 1
			print(docPath)
			f = open(direc[0]+'/'+afile,'r')
			sentences = f.read().strip().split('।')
			sentences = [sentence for sentence in sentences if sentence != '']
			lengths += [len(sentence.split()) for sentence in sentences]
			f.close()
	totalWords = sum(lengths)
	totalSentences = len(lengths)


#sentenceLengthStats('../test/hindi')
sentenceLengthStats_mine('../../../../DATA/Fire/AD_Hoc/Hindi/hi.docs.2011/Clean')