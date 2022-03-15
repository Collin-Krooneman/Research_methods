#!/bin/bash
#
# Description: generates the total amount of occurences
#              of the word "de" in any given text file. 
#
# Usage: ./Find_word_de.sh <FILE>

# argument is the file, check if we got it. 
TEXT=$1
if [ -z "$TEXT" ]
then
    echo "specify a file!"
    exit
fi
# Filter the text on the word "de", taking into account capital letters,
# printing these on a seperate line, counting each line.
cat $TEXT | grep -wio 'de' | wc -l
# Filter the text on the word "de", without taking into account capital letters,
# printing these on a seperate line, counting each line.
cat $TEXT | grep -wo 'de' | wc -l
