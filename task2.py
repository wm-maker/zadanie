import json
file_name="data.json"
# Load the data back from the file

def print_library(lib):
    print("Library context")
    for book in lib:
        print("book: ", book)

def add_book(lib):
    print("add new book in format: name author genre")
    try:
        name, author, genre = map(str, input().split())
        lib.append({'name':name, 'author':author, 'genre':genre, 'status':'not read'})
    except ValueError:
        print("wrong values")

def mark_book_read(lib, book_name):
    print("mark book with name %s as read" % book_name)
    for it in lib:
        if it['name'] == book_name:
            it['status'] = 'read'
            print("book with name %s was marked successfully" % book_name)
            return
    print("book with name %s is not in the library" % book_name)

try:
    with open(file_name, 'r') as file:
        library = json.load(file)
except:
    print("Unable to load file %s, set some default library books" % file_name)
    library=[]
    # library = [ 
    #     {
    #     'name': 'kniga 1',
    #     'author': 'J.R.Tolkien',
    #     'genre': "fantasy",
    #     'status': "not read"
    #     'favorite': "no"
    #     },
    #     {
    #     'name': 'kniga 2',
    #     'author': 'author 2',
    #     'genre': "thriller",
    #     'status': "not read"
    #     'favorite': "no"
    #     }
    # ]
#add_book(library)        
print_library(library)

print("what book to mark as read? Enter  the name: ")
mark_book_read(library, input())
print_library(library)



# Save the data to a text file
with open(file_name, 'w') as file:
    json.dump(library, file, indent=2) 

