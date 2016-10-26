#should be imported modules
# datetime module to retrieve day and time
#import datetime
import os
import time

# functions:
# functions returns current time in format we need it (month/day/year ?)
"""
def getCurTime():
    return (' {:%Y-%b-%d %H-%M-%S}'.format(datetime.datetime.now()))
"""
def getCurTime():
    return time.strftime("%Y%m%d_%H%M%S")

# finction returns file opened for writing  (in current directory, in some folder?)
def getLog():
    #check if folder already exists, it not create folder
    #in current dir
    #may be it will be one more function
    #everything for windows and python 3 for now

    
    if not os.path.exists('logs'):
            os.mkdir('logs')
    try:
        file = open('./logs/testrun'+getCurTime()+'.log', 'a')
        return file
    except:
        return -1 


# writes entry into the log with time of entry and print the same message on the screen
def qaPrint(log, entry):
    #create message to be writed 
    message = getCurTime()+' '+entry
    print message
    log.write(message)
    log.close
    
#test how it works
entry = 'this is test entry passed'
log = getLog()
qaPrint(log, entry)