import os
import json
from TurnDictLower import turn_lower        # type: ignore # import turn_lower function

'''info = {
    "name": "py-shortcut", 
    "author": "Abhay Siddhartha",  
    "description": "Hi this is a tools like windows run command but, in this tool you create your own shorcuts.
    for example 'imagine you a work folder that open often, to open your work folder you locate it windows
    explorer every time' but here you can put file path of your 'work folder' and assign a key to it like "wf.
    now every time you open this tool and type 'wf' and 'press enter'. it will open you work folder directly.
    its much faster this way specially if you are a creator and you deal with multiple project/assets folder and files.
    to add your file/filder to the py-shortcut tool just use the :add_key command then type in the key then your
    file/folder path (use double forward slashes '//' instead of one backslash '' in the file path because python
    work with forward slashes). use help command to show all the useful commands.
    this tool store all the keys and path in a json file, if now json file present file the directory it will automatically
    create one for you. just the tools in a folder and put a shortcut of the main file to hte desktop.",
    }'''

# #  ____________ global variables and variables
global files, is_path_dict_empty, empty_dict_warnning

files = {}
# all_keys = files.keys()             # all the keys from dictionary
# key_count = len(all_keys)
is_path_dict_empty = False
empty_dict_warnning = '''
|    Warnning! - Path Dictionary is Empty!
|    Try adding some new keys to the Dictionary using ':add_key' command,
|    or Try 'help' Command.
'''

# _______________________________ importing the json dictionay which contains all the paths as a dictionary called "files"
def imp_json():
    global files, is_path_dict_empty, empty_dict_warnning

    dir_path = os.path.dirname(__file__)

    with open(os.path.join(dir_path, "•Dictionary•.json"), 'r') as f:
        
        try:
            files = json.loads(f.read())
            check_path_dict_empty()
            if is_path_dict_empty == True:
                print(empty_dict_warnning)
            return files
            
        except ValueError:
            print(empty_dict_warnning)
            is_path_dict_empty = True
            
            return  is_path_dict_empty 

# print(files)


#____________ printing some help messages 
def help():
    help_message = '''
|    :add_key = Add new Key
|    :all_keys = Show Dictionary
|    :clear = Clear Entire Dictionary
|    :keys = Show all Keys
|    :quit = Exit
|    :rm_key = Remove a Key
|    :sort = Sort Dictionary
|    :values = Show all Paths
    
    '''
    print(help_message)
    
    return None

def startup_check():
    if os.path.isfile("•Dictionary•.json") and os.access("•Dictionary•.json", os.R_OK):
        # checks if path dictionary exists
        print ("\nPath Dictionary Found and is readable")
    else:
        print ("\nEither Path Dictionary is missing or is not readable!")
        open('•Dictionary•.json', 'w').close()
        print("New Path Dictionary Created!")
        
    check_path_dict_empty()
        
        
    return None


# _________________ function to sort/refresh/save path dictionary
def sort_keys():
    
    global files, is_path_dict_empty, empty_dict_warnning
    
    with open(os.path.join(os.path.dirname(__file__), "•Dictionary•.json"), 'w') as f:            # saving files dictionary in path dictionary wiht sorting
        json.dump(files, f, indent = 4, sort_keys = True)
                    
    with open(os.path.join(os.path.dirname(__file__), "•Dictionary•.json"), 'r') as f:            # re opening newly saved path dictionary as files
        
        try:
            files = json.loads(f.read())
            
            check_path_dict_empty()
            if is_path_dict_empty == True:
                print(empty_dict_warnning)
            else:
                print("Dictionary Sorted")
                
            return files
            
        except ValueError:
            print(empty_dict_warnning)
            is_path_dict_empty = True
        
        return files
    
def check_path_dict_empty():
    
    global is_path_dict_empty
    
    with open(os.path.join(os.path.dirname(__file__), "•Dictionary•.json"), 'r') as f:
        
        try:
            temp = json.loads(f.read())
            
            if temp == {} or temp == None or temp == "":
                is_path_dict_empty = True
            else:
                is_path_dict_empty = False
                
            return 
            
        except ValueError:   
            is_path_dict_empty = True
        
        return is_path_dict_empty
    pass
    
def convert_slashes(path_string):
    """Convert all backslashes in a string to forward slashes."""
    return path_string.replace('\\', '//')    

def rm_key(key):
    global files
    if key in files.keys():
        files.pop(key)
        print("Key Removed!")
        sort_keys()
        return files
    else:
        print(F"The key you entered: '{key}' does not exixst!\nReturned to Home!")
        return None
    
def clear_dict():
    global files
    files.clear()
    print("\nPath Dictionary Cleared!\n")
    sort_keys()
    
    return None
    
# _____________ Function calls
startup_check()
imp_json()
turn_lower(files)               # turning all the keys in dictionary in lowercase 


while True:

    querry = input("enter the key: ",)        # ____ geiing querry input from the user
    querry = querry.lower()                    # ____ converting querry into lowercase
    


    if querry in files.keys():                   # checking if querry is in the keys. if it is, then open the assigned path
        if os.path.exists (files.get(querry)):          # checking if the path exist
            os.startfile(files.get(querry))
            print("It works")
            
            break                       # after opening the path break the loop
        
        else:      # if path does not exits print an error
            print("path: " + files.get(querry) + " does not exists")

        
        
    elif querry == ":add_key":
        new_item = {}
        new_key = ""
        new_path = ""
        
        new_key = input("Enter the new key\n example - 'work_folder'\n: ")
        input_path = input("Enter the value for your new key\n example - 'c://Users//Work Folder' \n: ")
        new_path = convert_slashes(input_path)

        new_item = {str(new_key):str(new_path)}
        files.update(new_item)
        
        with open(os.path.join(os.path.dirname(__file__), "•Dictionary•.json"), 'w') as f:
            json.dump(files, f, indent = 4, sort_keys = True)
            
        if is_path_dict_empty == True:
            is_path_dict_empty = False
        
        print("key added")
        
        continue
        
    elif querry == ":keys":         # if user want to print all the keys 
        
        if is_path_dict_empty == True or len(files.keys()) == 0:
            print("Path Dictionary is empty!")
        else:
            for x in files.keys():
                    print(x)    
    
    elif querry == ":values":         # if user want to print all the paths
        
        if is_path_dict_empty == True or len(files.values()) == 0:
            print("Path Dictionary is empty!")
        else:
            for x in files.values():
                    print(x)
        
    elif querry == ":all":
        
        if is_path_dict_empty == True or len(files) == 0:
            print("Path Dictionary is empty!")
        else:
            for x in files.items():              # if user want to print whole dictionary
                print(x)

    elif querry == ":quit":           # if user want to quit hte program
        exit()
        
    elif querry == "help":               # if user needs help
        help()
        
    elif querry == ":sort":
        
        if is_path_dict_empty == True or len(files) == 0:
            print("Path Dictionary is empty!")
        else:
            sort_keys()
    
    elif querry == ":rm_key":
        rm_key(input("Enter the key to remove: "))
    
    elif querry == ":clear":
        clear_dict()
    
    else:
        print(F"The key you entered '{querry}' does not exists")                   #show error for invalid input

## debug
# print("before\n", files, "\n___length is: ", len(files))   ## __________________________________ debug command