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

6. read in the r or z , makes you know what matrix it is 

"""
import random
# class MatrixError(Exception):
#     pass

class Matrix:



    def __init__(self,values,rows,cols):
        #makes them private : .__variable_name
        self.__values = values
        self.__rows = rows
        self.__cols = cols


    def __add__(self, other):

        if len(self.__values) != len(other.__values) or len(self.__values[0]) != len(other.__values[0]):
            # raise MatrixError("Trying to add Matrices of different dimensions")
            print("Trying to add Matrices of different dimensions")
            return None


        result = [[1 for x in range(self.__cols)] for y in range(self.__rows)]
        for i in range(len(self.__values)):
            # iterate through columns
            for j in range(len(self.__values[0])):
                result[i][j] = int(self.__values[i][j]) + int(other.__values[i][j])

        return Matrix(result, len(result), len(result[0]))







    def __mul__(self, other):

        if(len(other.__values[0]) == len(self.__values)):
            print("Matrices cannot be multiplied")
            return None

        matrix_container = [[0 for cols in range(len(other.__values[0]))] for rows in range(len(self.__values))]

        # explicit for loops
        for i in range(len(self.__values)):
            for j in range(len(other.__values[0])):
                for k in range(len(other.__values)):
                    # resulted matrix
                    matrix_container[i][j] += int(self.__values[i][k]) * int(other.__values[k][j])

        return Matrix(matrix_container,len(matrix_container), len(matrix_container[0]))






    def get_value(self, rows, cols):
        return self.__values[rows][cols]




    #should it only get the 2d matrix?
    def get_values(self):
        return self.__values




    def set_dimensions(self,rows,cols):
        if rows < 0:
            rows = 2
        if cols < 0:
            cols = 2

        self.__rows = rows
        self.__cols = cols




    def get_dimensions(self):
        return [self.__rows,self.__cols]




    def set_values(self,matrix_values):
        if len(matrix_values) == 0:
            w, h = 2, 2;
            matrix_values= [[0 for x in range(w)] for y in range(h)]

        self.__values = matrix_values



    def transpose_str(self):
        current_values = self.get_values()
        result = [[1 for rows in range(self.__rows)] for cols in range(self.__cols)]

        for i in range(len(current_values)):
            # iterate through columns
            for j in range(len(current_values[0])):
                result[j][i] = current_values[i][j]
        temp_Matrix = Matrix(result, self.__cols, self.__rows)

        return temp_Matrix.ToString()


    def transpose(self):

        #load array with 1s with the transposed dimensions
        result = [[1 for rows in range(self.__rows)] for cols in range(self.__cols)]

        #iterate through orginial and load transposed array.
        for i in range(len(self.__values)):
            # iterate through columns
            for j in range(len(self.__values[0])):
                result[j][i] = self.__values[i][j]

        #set_values of the transposed array into the original matrix object.
        self.set_values(result)
        self.set_dimensions(self.__cols, self.__rows)



    def isSymmetric(self):
        #created instnace of matrix which is a copy of the original.
        transposed_matrix = Matrix(self.get_values(),self.__rows,self.__cols)

        #transpose the matrix
        transposed_matrix.transpose()

        #check to see if matrix is equal to transposed.
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__values[i][j] != transposed_matrix.__values[i][j]:
                    return False
        return True






    #This prints a 2d matrix
    def ToString(self):
        str_matrix = ""
        temp = ""
        for i in range(self.__rows):
          for j in range(self.__cols):

            temp = str(self.__values[i][j])

            str_matrix += temp + " "

            if i == len(self.__values) - 1 and j == len(self.__values[i]) - 1:
                return str_matrix

            if j == len(self.__values[i]) - 1:
              str_matrix += "\n"

        return str_matrix








class ZeroOneMatrix(Matrix):
    def __init__(self,values,rows,cols):
        for r in range(len(values)):
            for c in range(len(values[0])):
                if int(values[r][c]) > 1 or int(values[r][c]) < 0:
                    values[r][c] = random.randrange(0,2)

        self.__values = values
        self.__rows = rows
        self.__cols = cols
        super().__init__(values,rows,cols)
        #figure out what happend


    def __add__(self, other):
        if len(self.__values) != len(other.__values) or len(self.__values[0]) != len(other.__values[0]):
            # raise MatrixError("Trying to add Matrices of different dimensions")
            print("Trying to join Matrices of different dimensions")
            return None

        result = [[1 for cols in range(self.__cols)] for row in range(self.__rows)]
        for i in range(len(self.__values)):
            # iterate through columns
            for j in range(len(self.__values[0])):
                result[i][j] = int(self.__values[i][j]) | int(other.__values[i][j])

        return ZeroOneMatrix(result, len(result), len(result[0]))



    def __pow__(self, other):
        if len(self.__values) != len(other.__values) or len(self.__values[0]) != len(other.__values[0]):
            # raise MatrixError("Trying to add Matrices of different dimensions")
            print("Trying to meet Matrices of different dimensions")
            return None

        result = [[1 for cols in range(self.__cols)] for rows in range(self.__rows)]
        for i in range(len(self.__values)):
            # iterate through columns
            for j in range(len(self.__values[0])):
                result[i][j] = int(self.__values[i][j]) & int(other.__values[i][j])

        return ZeroOneMatrix(result, len(result), len(result[0]))





    










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
# arr1 = read_input_files()
# print(arr1)
# print(arr1[3])

#arr1[n] = acessing a whole array
#arr[n][n] = a value within the array [[n]]
#arr[n][n][n] = for these [[[]]]



# ['2', '3'], [['2', '3', '4'], ['1', '5', '2']]

# ['2', '3'], [['1', '1', '1'], ['3', '4', '5']]

# [[4,1,9], [6,2,8], [7,3,5]]
# [[2,9], [5,2], [1,0]]
#['Z'], ['2', '2'], [['1', '0'], ['0', '1']], ['2', '2'], [['1', '1'], ['1', '0']]

matrix1 = Matrix([['2', '3', '4'], ['1', '5', '2'],['1', '5', '2']], 2 ,3)
matrix2 = Matrix([['1', '1', '1'], ['3', '4', '5']], 2, 3)

matrix3 = Matrix([[4,1,9], [6,2,8], [7,3,5]],3,3)
matrix4 = Matrix([[2,9], [5,2], [1,0]],3,2)


zmatrix1 = ZeroOneMatrix([['1', '0'], ['0', '1']],2,2)
zmatrix2 = ZeroOneMatrix([['1', '1'], ['1', '0']],2,2)





# print(zmatrix1.ToString())
# print("^")
# print(zmatrix2.ToString())
# print()
# zmatrix3 = zmatrix1 ** zmatrix2
# print(zmatrix3.ToString())
# print("\n\n")
#
#
# print(zmatrix1.ToString())
# print("v")
# print(zmatrix2.ToString())
#
# zmatrix3 = zmatrix1 + zmatrix2
# print("\n")
# print(zmatrix3.ToString())



# matrix3 = matrix1 * matrix2
# 
# 
# 
# 
# print(matrix3)

# matrix5 = matrix3 * matrix4
#
# print(matrix5.ToString())



#
#
# matrix1_str = matrix1.print_matrix()
# matrix2_str = matrix2.print_matrix()
#
# summation = matrix1_str +"\n\n"+"+"+"\n\n"+matrix2_str
#
# print(summation)









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