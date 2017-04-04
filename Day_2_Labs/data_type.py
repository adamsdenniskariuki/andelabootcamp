# function to test the data types

def data_type(arg):
  
  if (isinstance(arg, basestring)):
    return len(arg)
  
  elif(isinstance(arg, type(None))):
    return "no value"
    
  elif(arg == True or arg == False):
    return arg
  
  elif(isinstance(arg, int)):
    
    if(arg < 100):
      return "less than 100"
    elif(arg == 100):
      return "equal to 100"
    else:
      return "more than 100"
  
  elif(isinstance(arg, list)):
    
    if(len(arg) >= 3):
      return arg[2]
    else:
      return None

print data_type('andela')