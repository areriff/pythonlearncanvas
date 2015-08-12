import operator

import requests
from bs4 import BeautifulSoup


# How to make word counter

def start( url ):
    word_list = [ ]
    source_code = requests.get( url ).text
    soup = BeautifulSoup( source_code, 'html.parser' )
    for post_text in soup.find_all( 'h2', { 'class': 'list_title truncate' } ):
        content = post_text.string
        words = content.lower( ).split( )
        for each_word in words:
            print( each_word )
            word_list.append( each_word )
    clean_up_list( word_list )


def clean_up_list( word_list ):
    clean_up_list = [ ]
    for word in word_list:
        symbols = '~!@#$%^&*()_+`1234567890-=[]{};\'\\:\"|,./<>?'
        for i in range( 0, len( symbols ) ):
            word = word.replace( symbols[ i ], '' )
        if len( word ) > 0:
            clean_up_list.append( word )
    create_dictionary( clean_up_list )


def create_dictionary( clean_up_list ):
    word_count = { }
    for word in clean_up_list:
        if word in word_count:
            word_count[ word ] += 1
        else:
            word_count[ word ] = 1
    for key, value in sorted( word_count.items( ), key=operator.itemgetter( 1 ) ):
        print( key, value )


start( 'http://www.mudah.my/Kedah/for-sale' )
