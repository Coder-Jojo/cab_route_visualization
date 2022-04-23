import math


#for each patch we'll run csp
dict_of_sizes = {'House':2*2, 'Indus':5*5, 'Building':3*3, 'Tree' : 1*1, 'Ground':4*4, 'Airport':7*7, 'Railway':6*6}
# tot_num_industries = 0
# tot_num_houses = 0
def Diff(li1, li2):
    return list(set(li1) - set(li2)) + list(set(li2) - set(li1))

def find_square_of_this_size(assigned, n):
    #Return list of coordinates forming the given length of square
    to_ret = []
    assigned.sort()
    len = math.sqrt(n)
    least_i = assigned[0][0]
    least_j = assigned[0][1]
    for i in assigned:
        if(i[0]<len+least_i and i[1]<len+least_j):
            to_ret.append(i)
    return to_ret

def big_ones_square(arr):
    R = len(arr) 
    C = len(arr[0])
 
    S = []
    for i in range(R):
      temp = []
      for j in range(C):
        if i==0 or j==0:
          temp += arr[i][j],
        else:
          temp += 0,
      S += temp,
    # here we have set the first row and first column of S same as input matrix, other entries are set to 0
 
    # Update other entries
    for i in range(1, R):
        for j in range(1, C):
            if (arr[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                            S[i-1][j-1]) + 1
            else:
                S[i][j] = 0
     
    # Find the maximum entry and
    # indices of maximum entry in S[][]
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j
    
    x = []

    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            x.append((i,j))

    return x

def find_big_square(list_unassigned):
    #finding the biggest square, return list of coordinates
    temp = []
    list_unassigned.sort()
    least_i = list_unassigned[0][0]
    least_j = list_unassigned[0][1]
    for i in list_unassigned:
        temp.append((i[0]-least_i , i[1] - least_j))

    temp.sort()
    start_i = temp[0][0]
    start_j = temp[0][1]
    temp.sort(key = lambda a: a[1]) 
    end_i = temp[-1][0]
    end_j = temp[-1][1]
    rows = end_i - start_i + 1
    cols = end_j - start_j + 1

    arr=[] #to perform function of finding biggest 1 squares
    for i in range(rows):
        col = []
        for j in range(cols):
            if((i,j) in temp):
                col.append(1)
            else:
                col.append(0)
        arr.append(col)
    
    temp_indices_of_square = big_ones_square(arr)
    final_to_ret = []

    for i in temp_indices_of_square:
        final_to_ret.append((i[0]+least_i, i[1]+least_j))

    return final_to_ret



def is_consistent(assigned_coordinates, assigned_object,tot_num_houses, tot_num_industries,domain, tot_airports, tot_num_railways):
    if((assigned_object=='House' or assigned_object == 'Building') and tot_num_industries>0):   #House or ground away
        return False
    if(assigned_object=='Indus' and tot_num_houses<5*(tot_num_industries+1)): #minimum number of houses per industry
        return False
    if(len(assigned_coordinates) < dict_of_sizes[assigned_object]): #Size of plot and object
        return False
    if(assigned_object not in domain):  #Checking Domain updated during forward checking
        return False
    if(assigned_object == 'Airport' and tot_airports>0):
      return False
    if(assigned_object == 'Railway' and tot_num_railways>0):
      return False
    if(tot_num_houses>0 and assigned_object == 'Indus'):
        return False
    return True

def inferences(assigned_object,domain_left):
    if(assigned_object == 'Indus'):
        return True
        

def backtracking(unassigned_coordinates, domain_left, assignment,tot_num_houses, tot_num_industries, tot_num_airports, tot_num_railways):
    
    if(len(unassigned_coordinates) == 0): #all assigned
        
        return assignment
    to_be_assigned = find_big_square(unassigned_coordinates)
    unassigned_coordinates = Diff(unassigned_coordinates , to_be_assigned)
    
    for j in range(len(domain_left)):
        flag = 0
        flag1 = 0
        flag2 = 0
        i = domain_left[j]
        if (len(to_be_assigned) > dict_of_sizes[i]):
            x = find_square_of_this_size(to_be_assigned, dict_of_sizes[i])
            unassigned_coordinates = unassigned_coordinates + Diff(to_be_assigned , x)
            to_be_assigned = x
        if is_consistent(to_be_assigned, i, tot_num_houses, tot_num_industries, domain_left, tot_num_airports, tot_num_railways):
            if(i == 'House'):
                tot_num_houses += 1
                flag1 = 1
            if(i == 'Indus'):
                tot_num_industries += 1
                flag2 = 1
            if( i == 'Airport'):
              tot_num_airports += 1
            if( i == 'Railway'):
                tot_num_railways += 1
            

            if(inferences(i, domain_left)):
                domain_left= Diff(domain_left,  ['House','Ground']) #Removing from domain
                flag=1
            temp2 = [to_be_assigned,i]
            
            assignment.append(temp2) #assignment is the form of list of list, where the last index in the list inside list is the object assigned
            
            result = backtracking(unassigned_coordinates, domain_left, assignment, tot_num_houses, tot_num_industries, tot_num_airports, tot_num_railways)   #recursive call
            
            
            if(len(result)>0):
                return result
            else:
              assignment = []
        
        if(flag):
            domain_left.append('House')
            domain_left.append('Ground')
        if(flag2):
            tot_num_industries-=1
        if(flag1):
            tot_num_houses-=1

    return [] #return  empty list on failure
            

        

