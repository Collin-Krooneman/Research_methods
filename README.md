# Final research project

The provided shell script implements the python script medaille_counter.py. The end result will be the file output.txt that will contain two dictionaries. 

The script uses Twitter data that is retrieved from the Karora server.

# Data collection
You will be able to get the twitter tweets while using: scp -r s4890396@karora.let.rug.nl:/net/corpora/twitter2/Tweets/2022/02 . This command will get you the twitter tweets from February 2022.

scp -r s4890396@karora.let.rug.nl:/net/corpora/twitter2/Tweets/2021/08 . This command will give you the twitter tweets from August 2021.

The twitter tweets will be put in the directory you have opened in linux. 
# Usage 

To run the shell script you first need to grant permission with: chmod +x Synonym_counter.sh in linux.

In the directory containing the shell script you will need to make a directory called corpus. In corpus you need to put your acquired twitter tweets. This can be achieved by going first to the directory corpus and then downloading your twitter tweets. Or you download your tweets and then put them in your corpus directory.

The shell script used in the repository is run in Ubuntu 20.04 on Windows.

# Placement

You will need to put the python script and the shell script in the same directory. In this directory needs to be a directory called corpus that contains both files with twitter tweets.

# Running the program

The run the shell script use ./Synonym_counter.sh

You will get four different IC_output.txt files and one output.txt file. The output.txt file is the file that contains the dictionaries with the end results. 


