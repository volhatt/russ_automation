#should be imported modules
# datetime module to retrieve day and time
from datetime import datetime
import os
import sys


# functions:
# functions returns current time 
def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time

# finction returns file opened for writing  (in current directory, in some folder?)
def getLog1():
    #check dir existing, if not it creates dir 'logs' in curr directory

    if not os.path.exists('logs'):
            os.mkdir('logs')
    try:
        #file = open('./logs/testrun'+getCurTime()+'.log', 'a')
        log_file = open('logs\\testrun'+getCurTime()+'.log', 'a')
        return log_file
    except:
        return -1 

# writes entry into the log with time of entry and prints the same message on the screen
def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. example: [Oct 25 01:52:33.000001] TC1 - Passed
    print(log)
    print(message)
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print(log_message)
    # writes message to a log file
    log.write(log_message + "\n")

def getLog(log):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
    ##logs = "logs"
    ##log_dir = os.path.join(os.getcwd(), "logs")

    log_dir = os.path.join(os.getcwd(), log)
    
    
    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, "rfaRunner_" + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1
    
def getLocalEnv(properties):
    """
    Returns dictionary from properties file
    """
    # check if file is empty?
    try:
        with open(properties) as f:
            #dictionary comprehension
            dicT = dict([line.split('=') for line in f])
        return dicT
    except (OSError, IOError):
        return -1


def getCleanString(string):
    """ remove new line char in strings from files and from cmd
the same with leading spaces and space of end of the line """
    return string.rstrip()



##############################################
# rfaRunner.py

## take arguments from cmd

#really
### argv = sys.argv

#for test
argv = ["rfaRunner.py", "--testrun=42"]
if len(argv) != 2:
    print("something wrong here ")
    sys.exit('the arguments should be like \"--testrun=[0-10000]\"')

file_name = argv[0]
#file_name = getCleanString(argv[0])
print("File Name Is : ", file_name)


#trid = int(getCleanString(argv[0])((argv[1].split('='))[1]))
trid = int((argv[1].split('='))[1])
print("this is trid : ", trid)    


localEnv = getLocalEnv('local.properties')
## check, delete later
for i in localEnv:
    print (i + ' : ' + localEnv[i])
    
#test = getLocalEnv('test')
if localEnv == -1:
    sys.exit("Unable to get property file")


print("THIS IS LOCAL DIR ", localEnv['log_dir'])
# take  local dir from properties file 
log_dir = getCleanString(localEnv['log_dir'])

if log_dir == '':
    print("No value in log_dir")
    sys.exit("No value in log_dir")


#direct_for_test = os.path.join(os.getcwd(), log_dir)
#print("direct_for_test " , direct_for_test)
#print(os.path.isdir(direct_for_test))

log = getLog(log_dir)
if log == -1:
    sys.exit("Unable to create log file")

message = "It is working, right?"

# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
qaPrint(log, "Me like what me see")

# close the log file if it open
if not log.closed:
    log.close()



