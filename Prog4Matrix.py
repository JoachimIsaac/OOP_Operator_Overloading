"""
info for class , remember to put it !
"""



# Reads in the input files and splits them into subarrays.
def read_input_files():
    input_list = []
    file_name = input("Please enter the input file name.\n")
    counter = 0
    tracker = []
    temp_arr = []

    #Handles both the opening and closing of the file
    #when reading in values.
    with open(file_name,'r') as read_file:

        for line in read_file:
            array = line.split()
            tracker.append(len(array))

            if len(array) == 2 and tracker[counter - 1] == 1:
                    temp_arr[row_number] = array

            input_list.append(line.split())
            counter = counter + 1
        return input_list



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