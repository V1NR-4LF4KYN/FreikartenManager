# file for manipulating/editing data_james and data_anna

import sys, json

opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]


with open("data_anna.json", "r") as f_a: # open  annas json file
data_anna = json.load(f_a) # read it
    

with open("data_james.json", "r") as f_a: # open  james json file
    data_james = json.load(f_a) # read it

# manipulating the folge, if needed or lets say as orderered
if "-a" in opts:
    data_anna.folge += 1
    
elif "-j" in opts:
    data_james.folge += 1    



# conditions for adding other rewards for certain values of folge
if 