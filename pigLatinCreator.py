#pigLatinCreator.py
#translates sentences into Pig Latin
#douglas mckenney

def main():
    print("**Igpay Atinlay Eneratorgay 0005ay**")
    sentence = input("\nPlease enter an English sentence: ")
    print()

    words = (sentence.lower()).split()
    entencesay = []

    for word in words:
        ordway = [(latinize(word))]
        entencesay = entencesay + ordway

    entencesay = ' '.join(entencesay)
    entencesay = stripPunctuation(entencesay)
    
    print(entencesay.capitalize() + '.')

def latinize(word):
    vowels = 'aeiou'
    if word[0] in vowels:
        return (word + 'way')
    else:
        return (word[1:] + word[0] + 'ay')

def stripPunctuation(sentence):
    #had this as stripPeriod(); not sure how useful additions are
    sentence = sentence.replace('.', '')
    sentence = sentence.replace('!', '')
    sentence = sentence.replace('?', '')

        
    return sentence

main()
