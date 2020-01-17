import urllib

def read_txt():
    file = open(r'C:/Users/raigo/Documents/Python_course/movie_quotes.txt')
    content = file.read()
    #print (content)
    file.close()
    check(content)

def check(text):
    connection = urllib.urlopen ("http://www.wdylike.appspot.com/?q=" + text)
    output = connection.read()
    #print(output)
    if output == "true":
        print ("Palabrota")
    else:
        print ("We're fine!")


read_txt()
