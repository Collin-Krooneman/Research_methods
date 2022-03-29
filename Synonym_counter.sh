#!/bin/bash

# Runs the pyhton script Medaille_counter.py for the tweets in February.
# Will give a final dictionary in output.txt were all occurrences of the
# words are added.
echo 'Olympics 2022 februari:' > output.txt
find corpus/02/ -type f -print |\
xargs -n 1 python3 Medaille_counter.py 0 > IC_output.txt
tr \' \" < IC_output.txt > IC_output2.txt
python3 Medaille_counter.py 1 IC_output2.txt >> output.txt

# Runs the pyhton script Medaille_counter.py for the tweets in August.
# Will give a final dictionary in output.txt were all occurrences of the
# words are added.
echo '16 days in august 2021:' >> output.txt
find corpus/08/ -type f -print |\
xargs -n 1 python3 Medaille_counter.py 0 > IC_output3.txt
tr \' \" < IC_output3.txt > IC_output4.txt
python3 Medaille_counter.py 1 IC_output4.txt >> output.txt

