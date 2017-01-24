
# coding: utf-8

# In[22]:

new_fmale_chars = open('C:\\Ross\\female_chars_output.txt','r')
new_string = ''
for row in new_fmale_chars:
    row = row.strip()
    row = row.split(' ')
    if row.index(max(row)) == 0:
        next_char = 'a'
    elif row.index(max(row)) == 1:
        next_char = 'b'
    elif row.index(max(row)) == 2:
        next_char = 'c'
    elif row.index(max(row)) == 3:
        next_char = 'd'
    elif row.index(max(row)) == 4:
        next_char = 'e'
    elif row.index(max(row)) == 5:
        next_char = 'f'
    elif row.index(max(row)) == 6:
        next_char = 'g'
    elif row.index(max(row)) == 7:
        next_char = 'h'
    elif row.index(max(row)) == 8:
        next_char = 'i'
    elif row.index(max(row)) == 9:
        next_char = 'j'
    elif row.index(max(row)) == 10:
        next_char = 'k'
    elif row.index(max(row)) == 11:
        next_char = 'l'
    elif row.index(max(row)) == 12:
        next_char = 'm'
    elif row.index(max(row)) == 13:
        next_char = 'n'
    elif row.index(max(row)) == 14:
        next_char = 'o'
    elif row.index(max(row)) == 15:
        next_char = 'o'
    elif row.index(max(row)) == 16:
        next_char = 'q'
    elif row.index(max(row)) == 17:
        next_char = 'r'
    elif row.index(max(row)) == 18:
        next_char = 's'
    elif row.index(max(row)) == 19:
        next_char = 't'
    elif row.index(max(row)) == 20:
        next_char = 'u'
    elif row.index(max(row)) == 21:
        next_char = 'v'
    elif row.index(max(row)) == 22:
        next_char = 'w'
    elif row.index(max(row)) == 23:
        next_char = 'x'
    elif row.index(max(row)) == 24:
        next_char = 'y'
    elif row.index(max(row)) == 25:
        next_char = 'z'
    elif row.index(max(row)) == 26:
        next_char = ' '
    elif row.index(max(row)) == 27:
        next_char = '\n'
    new_string = new_string + next_char
print new_string
new_fmale_chars.close()


# In[ ]:



