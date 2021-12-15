class Helper:
    def check_user_input(val,datalist):
        '''' 
        Input : 
            (str) vaL: user input value
            (list) datalist: the list we need to search for user input
            
        OutPut: 
            True if the value exist in the list
            False if the value not exist.
        Print: print error message if the value not exist in the list.
        '''
        try:
            # Convert it into integer
            stringVal = str(val).lower()
            ValueExist= datalist.index(stringVal)
            return True
        except ValueError:
            print("Data input is incorrect!")
            return False
    
    def convertSeconds(seconds):
        '''
        INPUT: the number of seconds
        OUTPUT: 
        (str) string format for the hours:minutes:seconds
        '''
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60

        return "%d:%02d:%02d" % (hour, minutes, seconds)