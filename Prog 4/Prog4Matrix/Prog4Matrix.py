"""
 for class , remember to put it !
info
"""







"""
{
Matrix(class): 
list[][]
int rows 
int columns 
}

1. parameterized constructor --> Matrix = new matrix(list,row,column)
2. Matrix : operator --> *, + . 
3. matrix1 + matrix 2 four things with then we changing them. reinitialize each loop. (MATRIX 1 =  new matrix(...) and for 2 )  
4. 

(google search) 
transpose 
for row loop: 
    for cloumn loop(row + 1, array[]): 
        [row][column] = [column][row]
    
    
isSymmetric () vs. if, else 

5. !!!!! --> set_matrix_values(values,row,columns) (idea) ---> ? what would be the get? do we need ? get_matrix_values()==> [[[1,2,3,4], [24,4,5,5]]],[row,columns]]
"""

class Matrix:

    def __init__(self,values,rows,cols):
        self.values = values
        self.rows = rows
        self.cols = cols


    #This prints a 2d matrix
    def print_matrix (self):
        str_matrix = ""
        temp = ""
        for i in range(self.rows):
          for j in range(self.cols):

            temp = str(self.values[i][j])

            str_matrix += temp + " "

            if i == len(self.values) - 1 and j == len(self.values[i]) - 1:
                return str_matrix

            if j == len(self.values[i]) - 1:
              str_matrix += "\n"

        return str_matrix






# Reads in the input files and splits them into subarrays.
def read_input_files():
    input_list = []
    file_name = input("Please enter the input file name.\n")

    #Handles both the opening and closing of the file
    #when reading in values.
    with open(file_name,'r') as read_file:
        for line in read_file:
            input_list.append(line.split())

        return transform_input_into_2darrays(input_list)


def transform_input_into_2darrays(array):
    temp_arr = []
    number_of_rows = 0
    results = []

    for row in range(2, len(array)):
        #if the length of the array at positon row is 2 and the length
        #of the array behind it is 1 then we enter the if statement.
        #The case is: When we hit the postion of the first dimension
        if len(array[row]) == 2 and len(array[row - 1]) == 1:

            if row < 3:
                #we get the number of rows in the dimensions array.
                number_of_rows = int(array[row][0])

                #we append the array with the number of sets of matrixes we have to read through.
                if row - 2 == 0:
                    array[row-2][0] = int(array[row-2][0])
                    results.append(array[row - 2])
                else:
                    results.append(array[row - 2])



                #we append the character which says what we should do to a matrix.
                results.append(array[row - 1])


            #if row has already gone through the starting items.
            if row > 3:
                number_of_rows = int(array[row][0])

                # we append the array with the number of sets of matrixes we have to read through.
                results.append(array[row - 1])
                results.append(array[row])

                # # we append the character which says what we should do to a matrix.
                # results.append(array[row - 1])

            #this appends the dimensions of the very first matrix.
            if len(array[row]) == 2 and len(array[row - 1]) == 1 and len(array[row - 2]) == 1:
                results.append(array[row])

            #This is where we store the values of the matrix in a 2d array basedof the row
            #we read in.
            for position in range(1,number_of_rows + 1):


                temp_arr.append(array[row + position])

            #we append the array in temp array.
            results.append(temp_arr)

            # we make temp array empty.
            temp_arr = []

            #we add on the number of rows we went through + 1  so that we start on the very next dimension.
            row += number_of_rows + 1

            # if we get a dimension we fall in to this if statement.
            if len(array[row]) == 2:
                #we imediatly append the dimensions.
                results.append(array[row])

                #then we append the parts to make up the twod matix
                for position in range(1, number_of_rows + 1):
                    temp_arr.append(array[row + position])

            #And we append those parts to the results array.
            results.append(temp_arr)

            #we step temp_arr to be an empty array again
            temp_arr = []

#we return an array with all the results formated well within an array.
    return results











# test to see how it reads it.
arr1 = read_input_files()
print(arr1)
print(arr1[3])

#arr1[n] = acessing a whole array
#arr[n][n] = a value within the array [[n]]
#arr[n][n][n] = for these [[[]]]



# ['2', '3'], [['2', '3', '4'], ['1', '5', '2']]

# ['2', '3'], [['1', '1', '1'], ['3', '4', '5']]

# matrix1 = Matrix([['2', '3', '4'], ['1', '5', '2']], 2 ,3)
# matrix2 = Matrix([['1', '1', '1'], ['3', '4', '5']], 2, 3)
#
# matrix1_str = matrix1.print_matrix()
# matrix2_str = matrix2.print_matrix()
#
# summation = matrix1_str +"\n\n"+"+"+"\n\n"+matrix2_str
#
# print(summation)

#
# matrix3 = matrix + matrix2
#
# print(matrix1.values)
# print(matrix1.rows)
# print(matrix1.cols)





#This prints a 2d matrix
# def print_matrix(matrix):
#     str_matrix = ""
#     temp = ""
#     for i in range(len(matrix)):
#       for j in range(len(matrix[0])):
#
#         temp = str(matrix[i][j])
#
#         str_matrix +=  temp + " "
#
#         if j == len(matrix[i]) - 1:
#           str_matrix += "\n"
#     print(str_matrix)