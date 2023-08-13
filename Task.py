'''write a program for a input of two strings X and Y, find the minimum number of steps required to convert X to Y. '''

# For find the minimum possibility for convert string x to y

def minimum_step(x, y):
    m, n = len(x), len(y)

    # creating 2D matrix, m for rows and n for columns
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            # check condition if 0
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] == i

            # if both character are same then copy them
            elif x[i -1] == y[j -1]:
                dp[i][j] = dp[i -1][j -1]

            # if the character are not same or zero then check the minimum possibility of insert, remove & replace
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j -1], dp[i -1][j -1])

    # this return minimum possibility for convert string
    return dp[m][n]

# Take input from user
x = input("Enter the first string: ") 
y = input("Enter the second string: ")

# print the result
result = minimum_step(x, y)
print("Minimum steps required: ",result)