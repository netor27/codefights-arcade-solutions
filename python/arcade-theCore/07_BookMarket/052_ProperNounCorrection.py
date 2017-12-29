def properNounCorrection(noun):
    '''
    Proper nouns always begin with a capital letter, followed by small letters.

    Correct a given proper noun so that it fits this statement.
    '''    
    return noun[:1].upper() + noun[1:].lower()

print(properNounCorrection("PaRiS"))