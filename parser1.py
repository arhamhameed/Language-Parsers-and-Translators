from cyk import parse

'''
The array sentence contains the test sentenses that our machine recognizes or not.
Recognizable sentences:
    'I and Arham drove the bike down the dirty street'
    'I jumped over the aesthetic mountains down the magnificent Himalayas lake'
    'I drank the Argentina'
    'laptop drank the hot tea'
    'I drank the tea'

Non Recognizable Sentences:
    'I drank the coffee',
    'Argetina and America are neighbours',
'''

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
    parse('./english_grammar.txt', i)
    print('')
