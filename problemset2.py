#problem2
def first_last(list:list[int],number:int):
    count_of_target=list.count(number)
    first_occ=0
    second_occ=0

    if count_of_target==0:
        return "The number is not in the list"
    elif count_of_target==1:
        first_occ=list.index(number)
        second_occ=list.index(number)
    else:
        first_occ=list.index(number)

        rest_list=list.copy()[first_occ:]
        rest_list.reverse()
        for i in range(len(rest_list)):
            if(rest_list[i]==number):
                second_occ=len(rest_list)+first_occ-i
                break
        
    return f"The first occurence is at {first_occ} and the last occurence is at {second_occ}"

#problem4
def binary_search(list:list[int],number:int):
    low=0
    high=len(list)-1

    while low<=high:
        mid=low+high-low//2

        if list[mid]==number:
            return f"The integer is in location: {mid}"
        elif list[mid]>number:
            low=mid+1
        elif list[mid]<number:
            high=mid-1

    return "The number is not in the list."

#problem5
def bubble_sort(list:list[int]):
    finished=False

    while not finished:
        swap=False
        for i in range(len(list)-1):
            if list[i]>list[i+1]:
                val=list[i]
                list[i]=list[i+1]
                list[i+1]=val
                swap=True

        if not swap:
            finished=True

    return list

# Problem 8 (2 points): This program needs to take in an integer n and then use the cashier’s algorithm to
# find the change for n cents using dollars, quarters, dimes, nickels and pennies.
# Conditions:
# 1
# (a) Put a comment line in your file designating where problem8 is.
# (b) You must name the function cashiers(amount).
# (c) It must return output of the form ’a dollars, i quarters, j dimes, k nickels, m pennies’.
# Note: This will print all currencies even if the number of them is zero. For example, an input of 25 will
# output ’0 dollars, 1 quarters, 0 dimes, 0 nickels, 0 pennies’. There are better ways to print this, but for
# consistency of output the above method has been chosen.

#problem
def cashiers(amount):
        return None