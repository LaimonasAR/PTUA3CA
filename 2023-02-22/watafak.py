import logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')



def move_to_end_fu(my_list: list, numb: int) -> list:
    to_be_order = my_list.copy()
    logging.info(f"function move_to_end received my_list {my_list}, and number {numb}")
    my_order = make_order_list_fu(to_be_order=to_be_order, numb=numb)
    logging.info(f"function make_order_list returned {my_order}")
    #my_list_ordered = [my_list[k] for k in my_order]
    my_list_ordered = sorted(zip(my_list, my_order), key=lambda x: x[1])
    my_list_ordered = [item[0] for item in my_list_ordered]
    return my_list_ordered


def make_order_list_fu(to_be_order: list, numb:int) ->list:
    logging.info(f"function make_order_list received list to be changed to order list {to_be_order} and number to move to end {numb}")
    i=0
    j=0
    for item in to_be_order:

        if item == numb:
            to_be_order[i] = (len(to_be_order) -i -1)
            j+=1
        else:
            to_be_order[i] = i - j
        i+=1
    logging.info(f"Make_order_list creates this list {to_be_order}")
    return to_be_order


list= [1,1,2,5,9]


result_list = move_to_end_fu(list, numb= 1)
print(result_list)