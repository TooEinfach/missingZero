"""
Script to add zero to front of a id as text
"""
with open('testingStuff.txt', 'r') as out_file:
    new_list = []
    final_list = []
    for line in out_file:
        new_line = line.strip('\n')
        for i in new_line:
            new_list.append(i)
        final_list.append(new_list)
        new_list = []
    for i in final_list:
        if len(i) < 10 and len(i) > 0:
            i.insert(0, '0')
            # print(i)

with open('newfile.txt', 'w') as new_file:
    for i in final_list:
        for j in i:  # Write line to new file.
            new_file.write(j)
        new_file.write('\n')
# print(final_list)
        