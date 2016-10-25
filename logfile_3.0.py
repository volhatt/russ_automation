#should be imported modules
# datetime module to retrieve day and time
import datetime

def main():


    # functions:


    # functions returns current time in format we need it (month/day/year ?)
    def getCurTime():
        return (' {:%Y-%b-%d %H-%M-%S}'.format(datetime.datetime.now()))


    # finction returns file opened for writing  (in current directory, in some folder?)
    def getLog():
        #part of file name 
        #fileName = 'testrun'
        # should it be 'log' extention?
        file = open('C:\\test\\testrun'+getCurTime()+'.txt', 'a')
        
        return file
    
    
    


    # writes entry into the log with time of entry and print the same message on the screen
    def qaPrint(log, entry):
        #create message to be writed 
        message = getCurTime()+' '+entry
        print(message)
        log.write(message)


    entry = 'this is test entry passed'
    log = getLog()
    qaPrint(log, entry)







    # test how it works

if __name__ == "__main__":
    main()


