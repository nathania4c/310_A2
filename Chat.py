import PersonOrLocation, random, General

global branch
branch=''
def Chat(words): #type is person or place
    branch = PersonOrLocation.determineBranch(words.split())
    keywords = PersonOrLocation.PersonOrLocation(words)
    if(len(keywords[0]) == 0) and (len(keywords[1]) == 0):
        return


    for person in keywords[0]:
        sentence = input(General.response(branch,'person'))
        Chat(sentence)
    for place in keywords[1]:
        sentence = input(General.response(branch,'place'))
        Chat(sentence)

def setBranch(b):
    global branch
    branch = b

def getBranch():
    return branch