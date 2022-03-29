# Name: Collin Krooneman
# Date: 27-3-2022
# Name program: Medaille_counter.py
# This program takes a corpus with twitter tweets and filters threw these
# tweets for the word medaille and its synonyms in the dutch language.

import gzip
import json
import sys

def individual_count(argv):
    '''takes a hour of tweets and looks for the 
    word medaille and it's synoyms and will return
    a dictionary for every hour worth of tweets'''
    Medaille_dict = {'medaille': 0, 'versierselen': 0, 'gedenkpenning': 0, 'eremetaal': 0,
                    'insigne': 0, 'ereteken': 0, 'erepenning': 0, 'distinctief': 0,
                    'onderscheiding': 0, 'plak': 0}
    with gzip.open(argv[2], 'rt' ) as infile:
        for line in infile:
            tweet = json.loads(line)
            tweet_text = tweet["text"]
            for item in Medaille_dict.keys():
                if item in tweet_text:
                    Medaille_dict[item] = Medaille_dict[item] + 1
    print(Medaille_dict)

def Total_count(argv):
    '''Takes the output file with dictionaries from
    the individual_count function and makes one total 
    dictionary'''
    Total_Medaille_dict = {'medaille': 0, 'versierselen': 0, 'gedenkpenning': 0, 'eremetaal': 0,
                    'insigne': 0, 'ereteken': 0, 'erepenning': 0, 'distinctief': 0,
                    'onderscheiding': 0, 'plak': 0}
    Total_tweets = 0
    with open(argv[2], "r") as infile:
        for line in infile:
            if line[0] == '{':
                Total_tweets += 1
            individual_dict = json.loads(line)
            for word in Total_Medaille_dict.keys():
                Total_Medaille_dict[word] = Total_Medaille_dict[word] + individual_dict[word]
    print("Dictionary:", Total_Medaille_dict)

def main(argv):
    if len(argv) != 3:
        print("Usage: python3 Medaille_counter.py [0/1] [file]")
        exit(-1)
    if argv[1] == str(0):
        individual_count(argv)
    elif argv[1] == str(1):
        Total_count(argv)
    else:
        print("Usage: python3 Medaille_counter.py [0/1] [file]")
        exit(-1) 

        
if __name__=="__main__":
    main(sys.argv)