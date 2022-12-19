# Question 1: Write a function to print "Hello_USERNAME"
# def hello_name(user_name):
#     print("What's Up!!??!! " + user_name.title() + "? ((:")


# hello_name('jimmy choo')


def hello_name(user_name):
    """Create a function that allows a user to input a username to output Hello_(user_name)"""
    user_name = input('Enter Username: ')
    print("hello_" + user_name + "!")
    return


def greeting(user_name):
    return print("hello_"+user_name.upper())

# greeting("Ryan")


# Question 2: Print first odd numbers between 1 and 100

# def first_odds():
#     '''Displays odd numbers 1-100
#     anythign that exists in here will be
#     part of the docstring

#     '''
#     for x in range(1, 101):

#         if x % 2 != 0:
#             print(x)

# first_odds()


# def first_odds():
#     for number in range(1, 101):
#         if number % 2 == 1:
#             print(number)


# def first_odds():
#     """Create a function that prints out odd numbers but returns nothing"""
#     for value in range(1, 100, 2):
#         print(value)
#     return


# first_odds()

# def odd_numbers():
#     numbers = list(range(0, 101))
#     print(numbers)
#     for number in numbers:
#         if number % 2 != 0:
#             print(number)

# odd_numbers()

def odd_numbers2():
    odd_numbers = []
    for odd in range(1, 100, 2):
        # print(odd)
        odd_numbers.append(odd)

    print(odd_numbers)


odd_numbers2()

# Question 3 Write a function that returns the max number in a given list

# def max_num_in_list(a_list):
#     return max(a_list)


# def max_num_in_list(a_list):
#    return print(max(a_list))
# #test cases
# list = [1, 2, 3, 4]
# list2 = [6, 88, 44, 104, 1]
# print(max_num_in_list(list))
# print(max_num_in_list(list2))


def max_num_in_list(a_list):
    """Pick the biggest number out of a given list"""
    max = a_list[0]
    # max number to first item in the list
    for x in a_list:
        if x > max:
            max = x
    return max


print(max_num_in_list([1, 2, 3, -10, 5]))


# Question 4 - Write a function that returns true if a year is a leap year
# or false if it is not
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False


def is_leap_year(a_year):
    '''Checks if given year is a leap year'''
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    elif (a_year % 400 == 0):
        return True
    else:
        return False


def is_leap_year(a_year):
    if(a_year % 4 == 0):
        if(a_year % 100 != 0 or a_year % 400 == 0):
            return True
    else:
        if(a_year % 4 > 0):
            return False


# print(is_leap_year(2022))


# Question 5: Write a function to check if all numbers in a list are consecutive
def is_consecutive(a_list):
    # store the first number in the list
    previous_num = a_list[0]
    # copy of a_list excluding the first number in a_list
    new_list = a_list[1:]

    for number in new_list:
        # check if the current number is the consecutive
        # number from the previous number
        if number-previous_num != 1:
            return False
        # if current number is consecutive, current
        # number now becomes the previous number
        else:
            previous_num = number

    return True




def is_consecutive(a_list):
    a_list.sort()
    for numbers in range(1, len(a_list)):
        if a_list[numbers] != a_list[numbers-1] + 1:
            return False
    return True





def is_consecutive(a_list):
    '''Checks if all given numbers are in consecutive order'''
    if sorted(a_list) == list(range((min(a_list)), (max(a_list) + 1))):
        return True
    else:
        return False


print(is_consecutive([1, 2, 3, 4, 5]))


def is_consecutive(a_list):
    """Write a function to confirm if numbers in a list are consecutive or not"""
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))


a_list = [2, 1, 3, 4, 5]

print(is_consecutive(a_list))
print(type(is_consecutive(a_list)))
