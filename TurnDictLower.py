
# ------------------------------a function that takes keys from input dictionary and turn then into lowercase, returns the new modified diuctionary as result---------------------------
def turn_lower(dict = {}):
    
    global  ley_list, temp_keylist, value_list, garbage_list                   # making used variable into global for future usecase.

    key_list = []                            # a new fresh list for keys
    temp_keylist = dict.keys()        # taking all the keys from input dictionary NOTE: this list doesn't support all the functionality of traditional list.
    key_list = [i.lower() for i in temp_keylist]  # so, we need to transfer all the keys into the new list that we just created above. and we can turn the keys in lowercase here.
    
    value_list = []                        # a new fresh list for values
    temp_valuelist = dict.values()   #  taking values from the input dictionary NOTE: this list doesn't support all the functionality of traditional list.
    for x in temp_valuelist:                        # so, transfer all the values into a new list that we just created.
        value_list.append(x)
    
    garbage_list = []                          # a list for all the keys who weren't lowercase.
    
    for x in temp_keylist:                    # puting the keys who werrn't lowercase into that garbage list.
        if x != x.lower():
            garbage_list.append(x)            

    # files.clear()
    
    for key in key_list:                          # appending all the lowercase keys with their values into the input dictionary.
        for value in value_list:
            # files.update({str(key): str(value)})
            dict[key] = value
            value_list.remove(value)               # removing used value for the loop
            break 
        
    #print("+__garbage keys needs to be popped__+\n", garbage_list)          #________debug command
    
    for x in garbage_list:                   # removing all the garbage/uppercase keys from the input dictionary
        dict.pop(str(x))
        # print(x, "popped")   #_______________________________________________debug command

    
    return dict, key_list, temp_keylist        # returning the final result with some useful data
    


# turn_lower(files)           #________________________________________________debug command
# print("\n after\n", files, "\n___length is: ", len(files))             #____________________denug command
