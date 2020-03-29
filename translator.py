from chomsky import convert_grammar, read_grammar
from cyk import parse

translation_key = {

'and': 'y','but': 'pero', 'or': 'o', 
'a': 'uno', 'an': 'un', 'this': 'esto', 'the': 'el',
'from': 'desde', 'to': 'a', 'over': 'encima', 'down': 'abajo', 'in': 'en',
'me': 'yo', 'I': 'yo', 'we': 'Nosotros', 'you': 'tú', 'they': 'ellos', 'it': 'eso',
'us': 'nosotros', 'he': 'él',
'fast': 'rápido', 'hot': 'caliente', 'magnificent': 'magnífico', 'aesthetic': 'estético',
'dirty': 'sucio',
'drove': 'condujo', 'drank': 'bebió', 'jumped': 'saltó', 'ran': 'corrió', 'fought': 'luchó',
'Argentina': 'Argentina', 'Pakistan': 'Pakistán', 'Arham': 'Arham', 'street': 'calle', 
'tea': 'té', 'laptop': 'ordenador portátil', 'mountains': 'montañas', 'Himalayas': 'Himalaya',
'bike': 'Bicicleta', 'lake': 'Lago'
}


def translate(grammar_file_path: str, string: str, translation_key: dict) -> str:
    '''    
    The function translates the English sentence that we parse into Spanish.
    The translation is done word by word by mapping English words to Spanish equals.
    The translation is stored in the dictionary: translation_key. 
    
    param: (1) the grammar file path that defines grammar
           (2) the sentence that we are testing for recognizability and translating
           (3) the word by word translation key

    return: the translation or the error message
    '''
    
    trans = []

    if parse(grammar_file_path, string) != True:
        print("Sorry the String is not recognized")
    else:
        trans = []
        string = string.split()
        for i in range(len(string)):
            trans.append(translation_key[string[i]])

        print('Translation:', '{}'.format(' '.join("{}".format(i) for i in trans)))

sentence = ['I and Arham drove the bike down the dirty street',
    'I jumped over the aesthetic mountains down the magnificent Himalayas lake',
    'I drank the Argentina', 
    'laptop drank the hot tea',
    'I drank the tea',
    'I drank the coffee',
    'Argetina and America are neighbours',
]

for i in sentence:
    print(i,':')
    translate('./english_grammar.txt', i, translation_key)
    print('')


