# sum the numbers: given a list of numbers, print their sum

list_of_numbers = [-1, 2, 3, 4, 5]

'''sum_of_list = sum(list_of_numbers)
print(sum_of_list)


# smallest number:  given a list of numbers, print the smallest of the numbers
smallest_num = min(list_of_numbers)
print(smallest_num)


# even numbers: given a list of numbers, print each number in that list that is even

for i in list_of_numbers:

    if i % 2 == 0:
        print(i)
    else:
        pass

# positive numbers: given a list of numbers, print each number in the list that is > 0

for i in list_of_numbers:

    if i > 0:
        print(i)
    else:
        pass

# positive numbers 2: given a list of numbers, create a new list which contains every number in the given list which is positive

positive_numbers = []

for i in list_of_numbers:

    if i > 0:
        positive_numbers.append(i)
    else:
        pass

print(positive_numbers)


# multiply a list: given a list of numbers and a single factor, create a new list consisting of each of the numbers in the first list multiplied by the factor. Print out the new list.

multiply_list = []
factor = 2

for i in list_of_numbers:
    multiply_list.append(i * factor)
else:
    pass

print(multiply_list)


# multiply vectors: given two lists of numbers of the same length, create a new list by multiplying pairs of numbers in corresponding positions in the two lists

list_one = [2, 5, 10]
list_two = [1, 4, 12]
combined_list = []

for i in range(len(list_one)):

    combined_list.append(list_one[i] * list_two[i])

print(combined_list)
'''

'''# Matrix Addition: given two two-dimensional lists of numbers of the size 2x2, calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding matrices


matrix_list_one = [
    [1, 3],
    [2, 4]
]

matrix_list_two = [
    [5, 2],
    [1, 0]
]

sum_first_matrix = []
sum_second_matrix = []

sum_matrix_list = []

for i in range(len(matrix_list_one)):

    for j in range(len(matrix_list_one[i])):

        if i == 0:
            sum_first_matrix.append(
                matrix_list_one[i][j] + matrix_list_two[i][j])
        else:
            sum_second_matrix.append(
                matrix_list_one[i][j] + matrix_list_two[i][j])

    if i == 0:
        sum_matrix_list.append(sum_first_matrix)
    else:
        sum_matrix_list.append(sum_second_matrix)


print(sum_matrix_list)'''

# Matrix Addition II: Extend the previous solution for a pair of matrices of any size (as long as they have the same size)

matrix_one = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

matrix_two = [
    [3, 2, 1],
    [3, 2, 1],
    [3, 2, 1],
    [3, 2, 1, 10]
]

for i in range(len(matrix_one)):

    if len(matrix_one[i]) == len(matrix_two[i]):
        print("The matrices have the same length")
    else:
        print(
            "The matrices should be equal. It'll still work though for equal sized arrays.")

list_storage = []  # Where we are storing the individual lists

for x in range(len(matrix_one)):
    x = []
    list_storage.append(x)

for i in range(len(matrix_one)):

    for j in range(len(matrix_one[i])):

        list_storage[i].append(matrix_one[i][j] + matrix_two[i][j])

print(list_storage)
