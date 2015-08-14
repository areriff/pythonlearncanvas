# coding=utf-8
story = '''
Look, I guarantee there`ll be {} times. I guarantee that at some {}, {} or both of us is gonna want
to get out of this {}. But I also guarantee that if I don`t ask you to be {}, I`ll {} it for the
rest of my {}, because I know, in my {}, you`re the {} one for me.
'''


def main( ):
    number = input( 'Enter a number (e.g. 1, 9: ' )
    verbs = input( 'Enter a verb (e.g. sleep, eat: ' )
    bodyPart = input( 'Enter a body part (e.g. knee, head: ' )

    adjectives = [ ]
    adjectives.append( input( 'Enter an adjective (e.g. big, smelly: ' ) )
    adjectives.append( input( 'Enter the second adjective (e.g. big, smelly: ' ) )
    adjectives.append( input( 'Enter the third adjective (e.g. big, smelly: ' ) )

    nouns = [ ]
    nouns.append( input( 'Enter a noun (e.g. box, window: ' ) )
    nouns.append( input( 'Enter the second noun (e.g. box, window: ' ) )
    nouns.append( input( 'Enter the third noun (e.g. box, window: ' ) )

    mad_lib = story.format(
        adjectives[ 0 ],
        nouns[ 0 ],
        number,
        nouns[ 1 ],
        adjectives[ 1 ],
        verbs,
        nouns[ 2 ],
        bodyPart,
        adjectives[ 2 ]
    )
    print( mad_lib )


main( )
