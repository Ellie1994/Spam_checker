import re
from spellchecker import SpellChecker

text_check = input('Paste your text here (for latin letters only!)\n: ')

pattern = r"[А-Яа-я]"

URLpattern = "(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?"

def detector():
    if re.findall(pattern, text_check):
        print("WARNING! The text contains characters of the cyrillic alphabet. It might be spam!")
    
    if re.findall(URLpattern, text_check):
        print("WARNING! The text contains URLs. Check the links. There might be spam!")
    
    else:
        print("first level spam-check was done successfully")
    
spell = SpellChecker()    
def spam_spellcheck():

    misspelled = spell.unknown(text_check.split())
    for counter, word in enumerate(misspelled, 1):
    
        print(counter, "detected: misspelled word --> " + word)
    
detector()
spam_spellcheck()
