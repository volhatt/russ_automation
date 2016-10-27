#should be imported modules
# datetime module to retrieve day and time
#import datetime
import os
import time

# functions:
# functions returns current time 
def getCurTime():
    return time.strftime("%Y%m%d_%H%M%S")

# finction returns file opened for writing  (in current directory, in some folder?)
def getLog():
    #check dir existing, if not it creates dir 'logs' in curr directory

    if not os.path.exists('logs'):
            os.mkdir('logs')
    try:
        #file = open('./logs/testrun'+getCurTime()+'.log', 'a')
        log_file = open('logs/testrun'+getCurTime()+'.log', 'a')
        return log_file
    except IOError:
        return -1 

# writes entry into the log with time of entry and prints the same message on the screen
def qaPrint(log, entry):
    #create message to be writed 
    message = getCurTime() + ' ' + entry
    print message
    log.write(message)
    log.close
    
#test how it works
entry = 'this is test entry passed'
log = getLog()
qaPrint(log, entry)