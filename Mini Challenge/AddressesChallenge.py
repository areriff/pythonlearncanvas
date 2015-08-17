# coding=utf-8
import sqlite3


def main( ):
    db = sqlite3.connect( 'test.db' )  # Create the database file
    db.execute( 'drop table if exists test' )  # Create a new table if it didn't already exist
    db.execute( 'create table test (t1 text, i1 int)' )  # To populate the table
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('one', 1) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('two', 2) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('three', 3) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('four', 4) )
    db.commit( )
    cursor = db.execute(
        'select * from test order by t1' )  # select all data according to order from the entry, and sorted by t1 field
    for row in cursor:
        print( row )


def main2( ):
    db = sqlite3.connect( 'test.db' )  # Create the database file
    db.execute( 'drop table if exists test' )  # Create a new table if it didn't already exist
    db.execute( 'create table test (t1 text, i1 int)' )  # To populate the table
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('one', 1) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('two', 2) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('three', 3) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('four', 4) )
    db.commit( )
    cursor = db.execute(
        'select i1, t1 from test order by i1' )  # change the order to display i1 first in the 1st colum then t1, after that sorted by i1 field
    for row in cursor:
        print( row )


def main3( ):
    db = sqlite3.connect( 'test.db' )  # Create the database file
    db.row_factory = sqlite3.Row  # row_factory allow to specify how rows will be return return from the cursor. It will create row object instead of tuples.
    db.execute( 'drop table if exists test' )  # Create a new table if it didn't already exist
    db.execute( 'create table test (t1 text, i1 int)' )  # To populate the table
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('one', 1) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('two', 2) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('three', 3) )
    db.execute( 'insert into test (t1, i1) values (?, ?)', ('four', 4) )
    db.commit( )
    cursor = db.execute(
        'select i1, t1 from test order by i1' )  # change the order to display i1 first in the 1st colum then t1, after that sorted by i1 field
    for row in cursor:
        print( dict( row ) )  # Will display dictionary object
        print( dict( row[ 't1' ], row[ 'i1' ] ) )  # To get all the data


main( )
print( '' )
main2( )
