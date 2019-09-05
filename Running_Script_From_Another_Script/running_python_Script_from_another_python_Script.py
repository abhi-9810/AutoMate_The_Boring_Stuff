import os
import sys
for filename in os.listdir(os.getcwd()):
    try:
        if filename=="c.py":
            continue
        if filename.endswith('.py'):
                temp="python "+str(filename)
                os.system(temp)
                os.system('\x03')
                #sys.exit()
    except:
            print("ex")
            pass
                
