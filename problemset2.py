#problem2
def first_last(list:list[int],number:int):
    count_of_target=list.count(number)
    first_occ=0
    second_occ=0

    if count_of_target==0:
        return "The number is not in the list."
    elif count_of_target==1:
        first_occ=list.index(number)
        second_occ=list.index(number)
    else:
        first_occ=list.index(number)

        rest_list=list.copy()[first_occ:]
        rest_list.reverse()
        for i in range(len(rest_list)):
            if(rest_list[i]==number):
                second_occ=len(rest_list)+first_occ-i-1
                break
        
    return f"The first occurrence is at {first_occ} and the last occurrence is at {second_occ}."

#problem4
def binary_search(list:list[int],number:int):
    low=0
    high=len(list)-1

    while low<high:
        mid=low+(high-low)//2
        print(high)
        print(mid)
        print(low)
        print(list[mid])

        if list[mid]==number:
            return f"The integer is in location: {mid}"
        elif list[mid]>=number:
            low=mid-1
        elif list[mid]<number:
            high=mid+1

    return "The number is not in the list."

print(binary_search([1,1,4,5,2,6,8],4))

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

#problem8
def cashiers(amount:int):
    dollars=amount//100
    amount=amount%100
    quarters=amount//25
    amount=amount%25
    dimes=amount//10
    amount=amount%10
    nickels=amount//5
    amount=amount%5
    pennies=amount
    return f"{dollars} dollars, {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies"

#column checker
def column_checker(matrix:list[list[int]],col_num:int,target_num:int):
    for row in matrix:
        if target_num == row[col_num]:
            return True

    return False

#grid checker
def grid_checker(matrix:list[list[int]],col_num:int,row_num:int,target_num:int):
    grid_list=[]
    for i in range(len(matrix)):
        if i//3==row_num//3:
            for j in range(len(matrix)):
                if j//3==col_num//3:
                    grid_list.append(matrix[i][j])

    return target_num in grid_list