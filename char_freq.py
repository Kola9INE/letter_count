'''
- TASK: 
Record the frequency distribution of the English characters from a linguistic data (A PDF WAS USED HERE).

- APPROACH:
1. Read the PDF file into the program with the pypdf module.
2. Create a list of the english alphabets.
3. Extract text from the document.
4. Separate non-alphabets from alphabets.
5. Record the distribution of non-alphabets and alphabets as a pandas dataframe, then saved as a csv file.
6. Record the frequency of the alphabets as pandas dataframe, then save as csv file.
7. Report the five most frequent and five least frequent.

- REPORT:
Using the text 'Three Books of Occult Philosophy' by Henry Cornelius Aggripa. The following was discovered:
1. Non-chars amounted to a total of 13,396.
2. Chars amounted to a total of 401,393.
3. The 5 most frequent characters are 'e', 't', 'a', 'o', 'i' with a frequency of 49455, 37452, 32792, 29627 and 29181 respectively.
4. The 5 least frequent characters are 'z', 'q', 'j', 'x', 'k' with a frequency of 220, 280, 461, 823 and 2153 respectively.

- CONCLUSION:
We can rightly conclude that 'e' appeared the most in the text 'Three Books of Occult Philosophy' as oppposed to 'z' appearing the least in the document.
'''

import string
from pypdf import PdfReader
from pathlib import Path
from functools import reduce
import pandas as pd

text = PdfReader(Path(Path.cwd()/'read'/'Three Books of Occult Philosophy.pdf'))
print(f'This is a book of {len(text.pages)} pages.\nWe are goint to check the distribution of the English alphabets in the book.\n')

alphabets  = list(string.ascii_lowercase)

real = text.pages
texts = []
x = 0
while x < len(real):
    texts.append(real[x].extract_text())
    x+=1
doc = reduce(lambda x,y:x+y, texts)

chars= [i for i in doc.lower() if i in alphabets]
non_chars = [i for i in doc.lower() if i not in alphabets]
print(f'We have {len(non_chars)} characters that are non-alphabets and {len(chars)} characters that are alphabets.')

df = pd.DataFrame({'Chars':[len(chars)],
                   'Non_chars':[len(non_chars)]})
df.to_csv('info/char_or_not.csv')

tmp = {i:chars.count(i) for i in alphabets}
freq_df = pd.DataFrame({'Chars':list(tmp.keys()),
                        'Frequency':list(tmp.values())})
freq_df.to_csv('info/char_freq.csv')

print('TOP 5 MOST FREQUENT CHARS:')
print(freq_df.nlargest(5, 'Frequency').reset_index(drop=True))
print('\n\n')
print('LEAST FIVE FREQUENT CHARS:')
print(freq_df.nsmallest(5, 'Frequency').reset_index(drop=True))