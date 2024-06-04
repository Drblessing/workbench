import time


# Python 2
# Task: Calculate the sum of squares from 1 to a large number
# def sum_of_squares(n):
#     total = long(0)
#     for i in range(1, n + 1):
#         total = total + (long(i) * long(i))
#     return total


# Python 3
def sum_of_squares(n):
    total = 0
    for i in range(1, n + 1):
        total = total + (i * i)
    return total


# Number of iterations (this should take around a minute to complete)
iterations = 10**8

# Start the timer
start_time = time.time()

# Perform the task
result = sum_of_squares(iterations)

# End the timer
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Write the result and elapsed time to a log file
log_file = open("speed_test_log.txt", "a")
log_file.write("Task completed.\n")
log_file.write("Sum of squares result: %d\n" % result)
log_file.write("Time taken: %.2f seconds\n" % elapsed_time)
log_file.write(
    "Python version: %s\n"
    % (".".join(map(str, [x for x in list(__import__("sys").version_info)[:3]])))
)
log_file.write("-" * 40 + "\n")
log_file.close()

# Print the result and elapsed time to the console
print("Task completed.")
print("Sum of squares result:", result)
print("Time taken: %.2f seconds" % elapsed_time)
