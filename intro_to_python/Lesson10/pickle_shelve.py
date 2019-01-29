import shelve

db_file = shelve.open('C:/Users/Alex/Desktop/letters.txt', 'c')
print ( list( db_file.keys( ) ) )


#db_file ['vowels'] = ['a', 'e', 'i', 'o', 'u']
#db_file ['end'] = ['x', 'y', 'z']
#db_file.close()

