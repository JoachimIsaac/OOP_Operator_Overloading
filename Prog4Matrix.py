"""
info for class , remember to put it !
"""



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
    results =[]


    for row in range(len(array)):
        #if the length of the array at positon row is 2 and the length
        #of the array behind it is 1 then we enter the if statement.
        #The case is: When we hit the postion of the first dimension
        if len(array[row]) == 2 and len(array[row - 1]) == 1:

            #we get the number of rows in the dimensions array.
            number_of_rows = int(array[row][0])

            #we append the array with the number of sets of matrixes we have to read through.
            results.append(array[row - 2])

            #we append the character which says what we should do to a matrix.
            results.append(array[row - 1])

            #this appends the dimensions of the very first matrix.
            if row == 2 and len(array[row - 1]) == 1 and len(array[row-2]) == 1:
                results.append(array[row])

            #This is where we store the values of the matrix in a 2d array basedof the row
            #we read in.
            for postion in range(1,number_of_rows + 1):

                temp_arr.append(array[row + postion])

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
                for postion in range(1, number_of_rows + 1):
                    temp_arr.append(array[row + postion])

            #And we append those parts to the results array.
            results.append(temp_arr)

            #we step temp_arr to be an empty array again
            temp_arr = []

#we return an array with all the results formated well within an array.
    return results











#test to see how it reads it.
arr1 = read_input_files()

print(arr1)













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