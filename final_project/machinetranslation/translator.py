from deep_translator import MyMemoryTranslator

def english_to_french(englishtext):
    """Function printing python version."""
    frenchtext = MyMemoryTranslator(source = 'english', target = 'french').translate(englishtext)
    return frenchtext

def french_to_english(frenchtext):
    """Function printing python version."""
    englishtext = MyMemoryTranslator(source = 'french', target = 'english').translate(frenchtext)
    return englishtext
