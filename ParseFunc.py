from cyk import parse

'''
The array function contains the test functions that our machine recognizes or not.
Recognizable functions:
    f ( x ) = x * 5
    f ( x , z ) = sin ( x * z )
    f ( x , z ) = ( x + z ) / 2 

Non Recognizable functions:
    x + y + z
    f ( a ) = a / 2
    g ( x ) = f ( z )
'''

function = ['f ( x ) = x * 5',
    'f ( x , z ) = sin ( x * z )',
    'f ( x , z ) = ( x + z ) / 2', 
    'x + y + z',
    'f ( a ) = a / 2',
    'g ( x ) = f ( z )',
]

for i in function:
    print(i,':')
    parse('./function_grammar.txt', i)
    print('')
