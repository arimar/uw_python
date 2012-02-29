"""
From Brian Dorsey's Internet Programming in Python, Winter 2011
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
	return 'Main page'

@app.route('/id1')
def id1():
    for k,d in database.iteritems():
	if (k == 'id1'):
	    for keys,data in d.iteritems():
    		print url_for(keys,data)
    return 'id1'

@app.route('/id2')
def id2():
    for k,d in database.iteritems():
	if (k == 'id2'):
	    for keys,data in d.iteritems():
		print keys,data
    return 'id2'

@app.route('/id3')
def id3():
    for k,d in database.iteritems():
	if (k == 'id3'):
	    for keys,data in d.iteritems():
		print keys,data
    return 'id3'

@app.route('/id4')
def id4():
    for k,d in database.iteritems():
	if (k == 'id4'):
	    for keys,data in d.iteritems():
		print keys,data
    return 'id4'

if __name__ == '__main__':
	app.run()


class BookDB():
    def titles(self):
        titles = [dict(id=id, title=database[id]['title']) for id in database.keys()]
        return titles

    def title_info(self, id):
        return database[id]


# let's pretend we're getting this information from a database somewhere
database = {
    'id1' : {'title' : 'CherryPy Essentials: Rapid Python Web Application Development',
             'isbn' : '978-1904811848',
             'publisher' : 'Packt Publishing (March 31, 2007)',
             'author' : 'Sylvain Hellegouarch',
           },
    'id2' : {'title' : 'Python for Software Design: How to Think Like a Computer Scientist',
             'isbn' : '978-0521725965',
             'publisher' : 'Cambridge University Press; 1 edition (March 16, 2009)',
             'author' : 'Allen B. Downey',
           },
    'id3' : {'title' : 'Foundations of Python Network Programming',
             'isbn' : '978-1430230038',
             'publisher' : 'Apress; 2 edition (December 21, 2010)',
             'author' : 'John Goerzen',
           },
    'id4' : {'title' : 'Python Cookbook, Second Edition',
             'isbn' : '978-0-596-00797-3',
             'publisher' : 'O''Reilly Media',
             'author' : 'Alex Martelli, Anna Ravenscroft, David Ascher',
           },
    'id5' : {'title' : 'The Pragmatic Programmer: From Journeyman to Master',
             'isbn' : '978-0201616224',
             'publisher' : 'Addison-Wesley Professional (October 30, 1999)',
             'author' : 'Andrew Hunt, David Thomas',
           },
}


