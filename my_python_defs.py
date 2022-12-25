

def input_list_v1(list_lenth):
    list_inernal = []
    for i in range(list_lenth):
        list_inernal.append(int(input(f"Enter {i} number of {list_lenth} in list: ")))
    return list_inernal


