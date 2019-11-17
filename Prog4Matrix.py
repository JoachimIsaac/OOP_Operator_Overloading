"""
 for class , remember to put it !
info
"""







import random


class Matrix:



    def __init__(self,values,rows,cols):
        #makes them private : .__variable_name
        self.__values = values
        self.__rows = rows
        self.__cols = cols


    def __add__(self, other):

        if len(self.__values) != len(other.__values) or len(self.__values[0]) != len(other.__values[0]):
            # raise MatrixError("Trying to add Matrices of different dimensions")
            outfile.write("Trying to add Matrices of different dimensions"+"\n\n")
            return None


        result = [[1 for x in range(self.__cols)] for y in range(self.__rows)]
        for i in range(len(self.__values)):
            # iterate through columns
            for j in range(len(self.__values[0])):
                result[i][j] = int(self.__values[i][j]) + int(other.__values[i][j])

        return Matrix(result, len(result), len(result[0]))




    def __mul__(self, other):

        if(len(other.__values) != len(self.__values[0])):
            outfile.write("Matrices cannot be multiplied"+"\n\n")
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
                    return "is not Symmetric"+"\n"
        return "is Symmetric"+"\n"






    #This  outfile.writes a 2d matrix
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
            outfile.write("Trying to join Matrices of different dimensions"+"\n\n")
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
            outfile.write("Trying to meet Matrices of different dimensions"+"\n\n")
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


#Reads in input file name and returns a file object.
def open_output_file():
    outfile = input("Please enter output file name: \n")
    file = open(outfile,'w')
    return file






# test to see how it reads it.
input_values = read_input_files()
outfile = open_output_file()








# while iterations < input_values[0][0]:

for position in range(1,len(input_values)):
    if len(input_values[position]) == 1:
        if input_values[position][0] == 'R':
            matrix1 = Matrix(input_values[position + 2],int(input_values[position + 1][0]),int(input_values[position + 1][1]))
            position = position + 3
            matrix2 = Matrix(input_values[position + 1],int(input_values[position][0]),int(input_values[position][1]))

            outfile.write("Multiplication:" + "\n\n" + matrix1.ToString()+ "\n" + "*" + "\n" + matrix2.ToString()+"\n\n")
            matrix3 = matrix1 * matrix2
            if matrix3 != None:
                outfile.write("=  " +"\n"+ matrix3.ToString()+"\n\n\n")

            outfile.write("Summation:" + "\n\n" + matrix1.ToString() + "\n" + "+" + "\n" + matrix2.ToString() + "\n\n")
            matrix3 = matrix1 + matrix2
            if matrix3 != None:
                outfile.write("=  " + "\n" + matrix3.ToString() + "\n\n")

            outfile.write("\n"+ "Transpose:"+"\n\n")
            outfile.write("Matrix1:" + "\n" + matrix1.ToString()+"\n\n")
            outfile.write("Transposed:" + "\n" + matrix1.transpose_str()+"\n\n")
            outfile.write("Matrix2:" + "\n" + matrix2.ToString() + "\n\n")
            outfile.write("Transposed:" + "\n" + matrix2.transpose_str()+"\n\n\n")

            outfile.write("Symmetry:"+"\n\n")
            outfile.write("Matrix1:" + "\n" + matrix1.ToString() + "\n\n" + matrix1.isSymmetric()+"\n\n")
            outfile.write("Matrix2:" + "\n" + matrix2.ToString() + "\n\n" + matrix2.isSymmetric()+"\n\n")

        elif input_values[position][0] == 'Z':
            zmatrix1 = ZeroOneMatrix(input_values[position + 2], int(input_values[position + 1][0]),
                             int(input_values[position + 1][1]))
            position = position + 3
            zmatrix2 = ZeroOneMatrix(input_values[position + 1], int(input_values[position][0]), int(input_values[position][1]))

            outfile.write("Join:" + "\n\n" + zmatrix1.ToString() + "\n" + "v" + "\n" + zmatrix2.ToString() + "\n\n")
            zmatrix3 = zmatrix1 + zmatrix2
            if zmatrix3 != None:
                 outfile.write("=  " + "\n" + zmatrix3.ToString() + "\n\n\n")

            outfile.write("Meet:" + "\n\n" + zmatrix1.ToString() + "\n" + "∧" + "\n" + zmatrix2.ToString() + "\n\n")
            zmatrix3 = zmatrix1 ** zmatrix2
            if zmatrix3 != None:
                 outfile.write("=  " + "\n" + zmatrix3.ToString() + "\n\n")

            outfile.write("\n" + "Transpose:" + "\n\n")
            outfile.write("Matrix1:" + "\n" + zmatrix1.ToString() + "\n\n")
            outfile.write("Transposed:" + "\n" + zmatrix1.transpose_str() + "\n\n")
            outfile.write("Matrix2:" + "\n" + zmatrix2.ToString() + "\n\n")
            outfile.write("Transposed:" + "\n" + zmatrix2.transpose_str() + "\n\n\n")

            outfile.write("Symmetry:" + "\n\n")
            outfile.write("Matrix1:" + "\n" + zmatrix1.ToString() + "\n\n" + zmatrix1.isSymmetric() + "\n\n")
            outfile.write("Matrix2:" + "\n" + zmatrix2.ToString() + "\n\n" + zmatrix2.isSymmetric() + "\n\n")

outfile.close()
















#  outfile.write(arr1[3])

#arr1[n] = acessing a whole array
#arr[n][n] = a value within the array [[n]]
#arr[n][n][n] = for these [[[]]]



# ['2', '3'], [['2', '3', '4'], ['1', '5', '2']]

# ['2', '3'], [['1', '1', '1'], ['3', '4', '5']]

# [[4,1,9], [6,2,8], [7,3,5]]
# [[2,9], [5,2], [1,0]]
#['Z'], ['2', '2'], [['1', '0'], ['0', '1']], ['2', '2'], [['1', '1'], ['1', '0']]

# matrix1 = Matrix([['2', '3', '4'], ['1', '5', '2'],['1', '5', '2']], 2 ,3)
# matrix2 = Matrix([['1', '1', '1'], ['3', '4', '5']], 2, 3)
#
# matrix3 = Matrix([[4,1,9], [6,2,8], [7,3,5]],3,3)
# matrix4 = Matrix([[2,9], [5,2], [1,0]],3,2)
#
#
# zmatrix1 = ZeroOneMatrix([['1', '0'], ['0', '1']],2,2)
# zmatrix2 = ZeroOneMatrix([['1', '1'], ['1', '0']],2,2)






#  outfile.write(zmatrix1.ToString())
#  outfile.write("^")
#  outfile.write(zmatrix2.ToString())
#  outfile.write()
# zmatrix3 = zmatrix1 ** zmatrix2
#  outfile.write(zmatrix3.ToString())
#  outfile.write("\n\n")
#
#
#  outfile.write(zmatrix1.ToString())
#  outfile.write("v")
#  outfile.write(zmatrix2.ToString())
#
# zmatrix3 = zmatrix1 + zmatrix2
#  outfile.write("\n")
#  outfile.write(zmatrix3.ToString())



# matrix3 = matrix1 * matrix2
# 
# 
# 
# 
#  outfile.write(matrix3)

# matrix5 = matrix3 * matrix4
#
#  outfile.write(matrix5.ToString())



#
#
# matrix1_str = matrix1. outfile.write_matrix()
# matrix2_str = matrix2. outfile.write_matrix()
#
# summation = matrix1_str +"\n\n"+"+"+"\n\n"+matrix2_str
#
#  outfile.write(summation)









#This  outfile.writes a 2d matrix
# def  outfile.write_matrix(matrix):
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
#      outfile.write(str_matrix)