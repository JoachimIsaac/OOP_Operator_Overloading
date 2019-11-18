"""
Names: Joachim Isaac & Micah-Lyn Scotland
Course: CS 2433-101, Fall 19, Dr. Stringfellow.

Purpose: To implement overloaded operators in Python;
to implement several copy constructors and a toString
method in Python. Also to extend the class. To perform
software development with others.

What we learned:
--> you cannot have both a default constructor
    and a parameterized constructor in a python class.

---> self.__variable_name (makes the member data private)

---> def __add__(self, other) makes you overload '+' operator.

"""

import random


class Matrix:

    # Matrix class parameterized constructor
    def __init__(self, values, rows, cols):
        # If matrix dimension/s exceed 10
        # create default matrix of 2x2 and all values
        # are equal to 1
        if len(values) > 10 or len(values[0]) > 10:
            self.__values = [[1 for x in range(2)] for y in range(2)]
            self.__rows = 2
            self.__cols = 2
        else:
            # Private member data.
            self.__values = values
            self.__rows = rows
            self.__cols = cols



    # Logic for '+' operator
    # '+' operator adds two regular Matrices together.
    def __add__(self, other):

        # If you try to add Matrices that have different dimensions. Print
        # "Trying to add Matrices of different dimensions" and make the
        # operator return null.
        if len(self.__values) != len(other.__values) or len(self.__values[0]) != len(other.__values[0]):
            outfile.write("Trying to add Matrices of different dimensions" + "\n\n")
            return None

        # Creates a 2d array with the correct dimensions
        # to load the sums of matrix1 and matrix2.
        result = [[1 for x in range(self.__cols)] for y in range(self.__rows)]

        # Loads the sums into the result.
        for i in range(len(self.__values)):
            for j in range(len(self.__values[0])):
                result[i][j] = int(self.__values[i][j]) + int(other.__values[i][j])

        # Returns a matrix with the right dimensions and
        # the values that were calculated after adding up
        # matrix1 and matrix2.
        return Matrix(result, len(result), len(result[0]))



    # Logic for '*' operator
    # '*' operator multiples two regular Matrices together.
    def __mul__(self, other):

        # If you try to multiply two matrices where the column of the first
        # matrix and the row of the second matrix is different. We print
        # "Matrices cannot be multiplied" and make the
        # operator return null.
        if (len(other.__values) != len(self.__values[0])):
            outfile.write("Matrices cannot be multiplied" + "\n\n")
            return None


        # Creates a 2d array with the correct dimensions
        # to load the products of matrix1 and matrix2.
        result = [[0 for cols in range(len(other.__values[0]))] for rows in range(len(self.__values))]

        # Loads the sums into the result.
        for i in range(len(self.__values)):
            for j in range(len(other.__values[0])):
                for k in range(len(other.__values)):
                    result[i][j] += int(self.__values[i][k]) * int(other.__values[k][j])

        # Returns a matrix with the right dimensions and
        # the values that were calculated, after computing
        # the product of matrix1 and matrix2.
        return Matrix(result, len(result), len(result[0]))



    # Gets a specific value from a matrix.
    def get_value(self, rows, cols):
        return self.__values[rows][cols]



    # Gets the 2d array that contains
    # all the values of a matrix.
    def get_values(self):
        return self.__values



    # Sets the dimensions of a matrix.
    def set_dimensions(self, rows, cols):
        self.__rows = rows
        self.__cols = cols



    # Returns an array of the Dimensions that a
    # matrix has.
    def get_dimensions(self):
        return [self.__rows, self.__cols]



    # Sets the values of a matrix.
    def set_values(self, matrix_values):
        if len(matrix_values) == 0:
            w, h = 2, 2;
            matrix_values = [[0 for x in range(w)] for y in range(h)]
        # If matrix dimension/s exceed 10
        # create default matrix of 2x2 and all values
        # are equal to 1
        elif len(matrix_values) > 10 or len(matrix_values[0]) > 10:
            matrix_values = [[1 for x in range(2)] for y in range(2)]
            self.__rows = 2
            self.__cols = 2
        else:
            self.__values = matrix_values



    # Transposes a matrix Not in-place (does not change the original matrix)
    # and then it returns a string of the transposed matrix.
    def transpose_str(self):
        current_values = self.get_values()

        #temporary 2D array to store values.
        result = [[1 for rows in range(self.__rows)] for cols in range(self.__cols)]

        # Transposes the values into the temporary 2D array
        for i in range(len(current_values)):
            for j in range(len(current_values[0])):
                result[j][i] = current_values[i][j]

        temp_Matrix = Matrix(result, self.__cols, self.__rows)

        return temp_Matrix.ToString()



    # Transposes the current Matrix
    # and changes the matrix values completely.
    def transpose(self):
        #temporary 2dlist to store transposed results.
        result = [[1 for rows in range(self.__rows)] for cols in range(self.__cols)]

        # iterate through original and load result array.
        for i in range(len(self.__values)):
            for j in range(len(self.__values[0])):
                result[j][i] = self.__values[i][j]

        # set_values of the transposed array into the original matrix object.
        self.set_values(result)
        self.set_dimensions(self.__cols, self.__rows)



    # Checks whether a matrix is symmetric or not, this is done Not in-place
    # without affecting the original matrix values.
    def isSymmetric(self):
        # Created instance of matrix which is a copy of the original.
        transposed_matrix = Matrix(self.get_values(), self.__rows, self.__cols)

        # Transpose the matrix
        transposed_matrix.transpose()

        # Check whether matrix is equal to transposed or not.
        for i in range(self.__rows):
            for j in range(self.__cols):
                if self.__values[i][j] != transposed_matrix.__values[i][j]:
                    return "is not Symmetric" + "\n"
        return "is Symmetric" + "\n"



    # Changes matrix values into a string format
    # and returns it.
    def ToString(self):
        str_matrix = ""
        temp = ""

        # Iterate through each value.
        for i in range(self.__rows):
            for j in range(self.__cols):

                # Loads value in temp.
                temp = str(self.__values[i][j])

                # Adds value into str_matrix with a space.
                str_matrix += temp + " "

                # When at the end of the 2D Array return the string.
                if i == len(self.__values) - 1 and j == len(self.__values[i]) - 1:
                    return str_matrix

                # If at the end of a column add "\n"
                # to the string, to go to the next line.
                if j == len(self.__values[i]) - 1:
                    str_matrix += "\n"

        return str_matrix



# Child class ZeroOneMatrix extends parent class Matrix.
class ZeroOneMatrix(Matrix):

    # Class parameterized constructor
    def __init__(self, values, rows, cols):
        # Checks all values in the 2d list if they are not 1 or 0, it changes
        # them randomly into a 1 or 0. This prevents the user from
        # inputting invalid values.
        for r in range(len(values)):
            for c in range(len(values[0])):
                if int(values[r][c]) > 1 or int(values[r][c]) < 0:
                    values[r][c] = random.randrange(0, 2)

        # Declare same private variables as in Parent class.
        self.__values = values
        self.__rows = rows
        self.__cols = cols

        # Calls Parent class to execute methods that were inherited.
        super().__init__(values, rows, cols)




    # Logic for '+' operator
    # '+' operator joins two ZeroOneMatrices together.
    def __add__(self, other):

        # If you try to join Matrices that have different dimensions. Print
        # "Trying to join Matrices of different dimensions" and make the
        # operator return null.
        if len(self.__values) != len(other.__values) or len(self.__values[0]) != len(other.__values[0]):
            outfile.write("Trying to join Matrices of different dimensions" + "\n\n")
            return None

        # Creates a 2d Array with the correct dimensions
        # to load the result of matrix1 join matrix2.
        result = [[1 for cols in range(self.__cols)] for row in range(self.__rows)]

        # Loads the results into the result array.
        for i in range(len(self.__values)):
            for j in range(len(self.__values[0])):
                result[i][j] = int(self.__values[i][j]) | int(other.__values[i][j])

        # Returns a matrix with the right dimensions and
        # the values that were calculated after computing
        # the join of Matrix1 and Matrix2.
        return ZeroOneMatrix(result, len(result), len(result[0]))



    # Logic for '**' operator
    # '**' operator meets two ZeroOneMatrices together.
    def __pow__(self, other):
        # If you try to  meet Matrices that have different dimensions. Print
        # "Trying to meet Matrices of different dimensions" and make the
        # operator return null.
        if len(self.__values) != len(other.__values) or len(self.__values[0]) != len(other.__values[0]):
            outfile.write("Trying to meet Matrices of different dimensions" + "\n\n")
            return None

        # Creates a 2D array with the correct dimensions
        # to load the result of matrix1 meet matrix2.
        result = [[1 for cols in range(self.__cols)] for rows in range(self.__rows)]

        # Loads the results into the result list.
        for i in range(len(self.__values)):
            for j in range(len(self.__values[0])):
                result[i][j] = int(self.__values[i][j]) & int(other.__values[i][j])

        # Returns a matrix with the right dimensions and
        # the values that were calculated after computing
        # the meet of matrix1 and matrix2.
        return ZeroOneMatrix(result, len(result), len(result[0]))



# Reads in the input files and splits them into subarrays.
def read_input_files():
    input_list = []
    file_name = input("Please enter the input file name.\n")

    # Handles both the opening and closing of the file
    # when reading in values.
    with open(file_name, 'r') as read_file:
        for line in read_file:
            input_list.append(line.split())

        return transform_input_into_2Darrays(input_list)



# Transforms input into 2D arrays.
def transform_input_into_2Darrays(array):
    temp_arr = []
    number_of_rows = 0
    results = []
    iterations = array[0][0]


    if iterations == '0':
        return results


    for row in range(2, len(array)):
        # If the length of the array at position 'row' is 2 and the length
        # of the array behind it is 1 then we enter the if statement.
        if len(array[row]) == 2 and len(array[row - 1]) == 1:

            if row < 3:
                # Gets the number of rows in the dimensions array.
                number_of_rows = int(array[row][0])

                # Gets the number of sets of matrices we have to read through.
                if row - 2 == 0:
                    array[row - 2][0] = int(array[row - 2][0])
                    results.append(array[row - 2])

                    # If it is not the first value, don't type cast it
                    # into an int.
                else:
                    results.append(array[row - 2])

                # Appends the character which says what we should do to a matrix.
                # ('R' or 'Z')
                results.append(array[row - 1])

            # If row has already gone through the starting items:
            # i.e ( [4] , [R] , [2,2] , [[1,2],[5,4]] , [[6,2],[5,6]])
            if row > 3:
                number_of_rows = int(array[row][0])

                # Appends the dimensions
                results.append(array[row - 1])
                # Appends the character which says what type of matrix it is.
                results.append(array[row])



            # This appends the dimensions of the very first matrix
            # in the input file.
            if len(array[row]) == 2 and len(array[row - 1]) == 1 and len(array[row - 2]) == 1:
                results.append(array[row])

            # This stores the values of the matrix
            # in a 2d array based of the row read in.
            for position in range(1, number_of_rows + 1):
                temp_arr.append(array[row + position])

            # Appends the temporary array in the results array.
            results.append(temp_arr)

            # Make temp array empty.
            temp_arr = []

            # Adds on the number of rows traversed + 1,
            # so that it starts at the very next dimension.
            row += number_of_rows + 1


            # If a dimension if found.
            if len(array[row]) == 2:
                # Immediately append the dimensions.
                results.append(array[row])

                # Then it appends the values of a matrix
                # into temp array, creating a 2d array
                for position in range(1, number_of_rows + 1):
                    temp_arr.append(array[row + position])

            # And appends the 2D array of values to the results array.
            results.append(temp_arr)

            # Sets temp_arr to be an empty array
            temp_arr = []

    # Returns array with all the input.
    return results



# Reads in input file name and returns a file object.
def open_output_file():
    outfile = input("Please enter output file name: \n")
    file = open(outfile, 'w')
    return file



# Print all the results in a nice format.
def print_results(input_values, outfile):

    if len(input_values) == 0:
        return outfile.write("The number of sets is Zero, nothing to read.")

    # If input_values has values, iterate over input_values and
    # read in a limit of (N(sets) * 5) + 1 to print the
    # number of sets.
    for position in range(1, (input_values[0][0] * 5) + 1):
        # If subarray of length 1 is found,
        # enter the if statement. This will be
        # a character of 'R' or 'Z'.
        if len(input_values[position]) == 1:
            if input_values[position][0] == 'R' or input_values[position][0] == 'r':
                matrix1 = Matrix(input_values[position + 2], int(input_values[position + 1][0]),
                                 int(input_values[position + 1][1]))
                position = position + 3
                matrix2 = Matrix(input_values[position + 1], int(input_values[position][0]),
                                 int(input_values[position][1]))

                outfile.write(
                    "Multiplication:" + "\n\n" + matrix1.ToString() + "\n" + "*" + "\n" + matrix2.ToString() + "\n\n")
                matrix3 = matrix1 * matrix2
                if matrix3 != None:
                    outfile.write("=  " + "\n" + matrix3.ToString() + "\n\n\n")

                outfile.write(
                    "Summation:" + "\n\n" + matrix1.ToString() + "\n" + "+" + "\n" + matrix2.ToString() + "\n\n")
                matrix3 = matrix1 + matrix2
                if matrix3 != None:
                    outfile.write("=  " + "\n" + matrix3.ToString() + "\n\n")

                outfile.write("\n" + "Transpose:" + "\n\n")
                outfile.write("Matrix1:" + "\n" + matrix1.ToString() + "\n\n")
                outfile.write("Transposed:" + "\n" + matrix1.transpose_str() + "\n\n")
                outfile.write("Matrix2:" + "\n" + matrix2.ToString() + "\n\n")
                outfile.write("Transposed:" + "\n" + matrix2.transpose_str() + "\n\n\n")

                outfile.write("Symmetry:" + "\n\n")
                outfile.write("Matrix1:" + "\n" + matrix1.ToString() + "\n\n" + matrix1.isSymmetric() + "\n\n")
                outfile.write("Matrix2:" + "\n" + matrix2.ToString() + "\n\n" + matrix2.isSymmetric() + "\n\n")
                #Seperator
                outfile.write("##########################################################"+"\n\n\n")


            elif input_values[position][0] == 'Z' or input_values[position][0] == 'z':
                zmatrix1 = ZeroOneMatrix(input_values[position + 2], int(input_values[position + 1][0]),
                                         int(input_values[position + 1][1]))
                position = position + 3
                zmatrix2 = ZeroOneMatrix(input_values[position + 1], int(input_values[position][0]),
                                         int(input_values[position][1]))

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
                # Seperator
                outfile.write("##########################################################" + "\n\n\n")
    #Closes file
    outfile.close()



input_values = read_input_files()
outfile = open_output_file()
print_results(input_values, outfile)




