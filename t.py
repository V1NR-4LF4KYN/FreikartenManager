import sys

# getting all users specifications
opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

if "-r" in opts:
    print('reset')
    
elif "-j" in opts:
    print('james')
    

elif "-a" in opts:
    print('anna')

elif "-az" in opts:
    print('anna zero')
