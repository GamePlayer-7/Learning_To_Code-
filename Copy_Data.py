
filename1 = input("Enter the first file name = ")

filename2 = input("Enter the second file name = ")

file1 = open(filename1, "r")

filedata1 = file1.read()

file1.close()

file2 = open(filename2, "a")                          

file2.write(filedata1)                                # Append the contents of the first file using the write() function.

file2.close()
