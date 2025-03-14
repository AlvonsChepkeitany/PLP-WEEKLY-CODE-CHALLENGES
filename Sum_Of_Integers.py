# Function to compute the sum of integers in a list
def sum_of_integers():
    # Accepting user input and converting it to a list of integers
    user_input = input("Enter a list of integers separated by spaces: ")
    
    # Converting the input string to a list of integers
    integer_list = [int(i) for i in user_input.split()]
    
    # Calculating the sum of the integers
    total_sum = sum(integer_list)
    
    # Displaying the result
    print(f"The sum of the integers in the list is: {total_sum}")

# Calling the function to run the program
sum_of_integers()
