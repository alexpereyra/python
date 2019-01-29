import shelve

db_file = shelve.open('letters.txt', 'c')
db_file ['vowels'] = ['a', 'e', 'i', 'o', 'u']
db_file ['end'] = ['x', 'y', 'z']
db_file.close()
db_file.sync()


db_file = shelve.open('letters.txt', 'c')
print ( list( db_file.keys( ) ) )
