import imp
input_data = input()
input_data = 'print(' + input_data + ')'
f = open('temp.py', 'w')
f.write(input_data)  # python will convert \n to os.linesep
f.close()
#imp.reload(temp) 
import temp

  
  
  