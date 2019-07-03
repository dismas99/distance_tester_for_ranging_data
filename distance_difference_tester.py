from dismas import check_min_and_max
from dismas import print_min_max_range


my_list = []
with open('ranging_data.txt') as ranging_data:
    for line in ranging_data:
        value = line.split(",")
        my_list.append(value)

Tag1_distances = []
Tag2_distances = []
Tag3_distances = []
Tag4_distances = []
 
for each_line in my_list:
    if int(each_line[5]) > 0:
        Tag1_distances.append(each_line[5])
    if int(each_line[7]) > 0:
        Tag2_distances.append(each_line[7])
    if int(each_line[9]) > 0:
        Tag3_distances.append(each_line[9])
    if int(each_line[11]) > 0:
        Tag4_distances.append(each_line[11])
        

print("\tTAG1\n")
Tag1_values = check_min_and_max(Tag1_distances)
print_min_max_range(Tag1_values)

print("\tTAG2\n")
Tag2_values = check_min_and_max(Tag2_distances)
print_min_max_range(Tag2_values)

print("\tTA3\n")
Tag3_values = check_min_and_max(Tag3_distances)
print_min_max_range(Tag3_values)

print("\tTAG4\n")
Tag4_values = check_min_and_max(Tag4_distances)
print_min_max_range(Tag4_values)
