
def check_min_and_max(tag_distance):
    list_val =[]
    min_max_range = []
    for vall in tag_distance:
        list_val.append(int(vall))
    list_val.sort()
    if (list_val):
        minimum = list_val[0]
        maximum = list_val[-1]
        the_range = maximum - minimum
        min_max_range.append(minimum)
        min_max_range.append(maximum)
        min_max_range.append(the_range)
    return min_max_range

def print_min_max_range(list_of_values):
    if (list_of_values):
        print("the minimum value is %d \n\n the maximum vale is %d \n\n and the range is %d \n\n" %(list_of_values[0],list_of_values[1],list_of_values[2]))
        if list_of_values[2] <= 15:
            print("\t The distance fluctuation is within accpetable limit\n\n")
        else: 
            print("\t Too much fluctuation, Not Accepted!!!\n\n")
