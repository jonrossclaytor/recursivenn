
# coding: utf-8

# In[57]:

import random


outfile = open('C:\\Ross\\male_output.txt','w')


# generate a random sample of 10 names from this list
names_list = []
mnames = open('C:\\Ross\\mnames.txt','r')
for name in mnames:
    names_list.append(name)

random.shuffle(names_list)

names_list = names_list[:10]

character_input = []
for name in names_list:
    name = name.lower()
    for char in name:
        onehot = [0] * 28 # 26 letters plus space and new line
        if char == 'a':
            onehot[0] = 1
        elif char == 'b':
            onehot[1] = 1
        elif char == 'c':
            onehot[2]= 1
        elif char == 'd':
            onehot[3] = 1
        elif char == 'e':
            onehot[4] = 1
        elif char == 'f':
            onehot[5] = 1
        elif char == 'g':
            onehot[6] = 1
        elif char == 'h':
            onehot[7] = 1
        elif char == 'i':
            onehot[8] = 1
        elif char == 'j':
            onehot[9] = 1
        elif char == 'k':
            onehot[10] = 1
        elif char == 'l':
            onehot[11] = 1
        elif char == 'm':
            onehot[12] = 1
        elif char == 'n':
            onehot[13] = 1
        elif char == 'o':
            onehot[14] = 1
        elif char == 'p':
            onehot[15] = 1
        elif char == 'q':
            onehot[16] = 1
        elif char == 'r':
            onehot[17] = 1
        elif char == 's':
            onehot[18] = 1
        elif char == 't':
            onehot[19] = 1
        elif char == 'u':
            onehot[20] = 1
        elif char == 'v':
            onehot[21] = 1
        elif char == 'w':
            onehot[22] = 1
        elif char == 'x':
            onehot[23] = 1
        elif char == 'y':
            onehot[24] = 1
        elif char == 'y':
            onehot[25] = 1
        elif char == ' ':
            onehot[26] = 1
        elif char == '\n':
            onehot[27] = 1
        
        matlab_arr_output = '['
        for item in onehot:
            matlab_arr_output = matlab_arr_output + str(item) + ' '
        matlab_arr_output = matlab_arr_output.strip() + ']'
        character_input.append(matlab_arr_output)

# write the output for matlab
outfile.write('inputs_cell = cell(1,' + str(len(character_input)-1) + ');\n')
for i in range(0,len(character_input) - 1):
    outfile.write('inputs_cell{' + str(i+1) + '} = ' + character_input[i] + ';\n')
    
print

outfile.write('\ntargets_cell = cell(1,' + str(len(character_input)-1) + ');\n')
for i in range(1,len(character_input)):
    outfile.write('targets_cell{' + str(i) + '} = ' + character_input[i] + ';\n')

outfile.close()


# In[ ]:



