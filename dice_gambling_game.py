
def sum_rolls(roll):
    """ This method takes a list and return sum of the list under conditions """
    factor =1
    dice_sum =0
    for i in range(len(roll)):
        dice_sum += factor*roll[i]
        if roll[i] ==1:
            factor =0
        elif roll[i] ==6:
            factor= 2
        else:
            factor =1
    return dice_sum


if __name__ == "__main__":
    
    litst =[1,2,3]
    print(sum_rolls(litst))
    
