import time
givenseconds = 27500
temp = time.gmtime(givenseconds)                          # converting given time in seconds to hours and minutes
resultantTime = time.strftime("%H:%M:%S", temp)
print("Converting given time in seconds", givenseconds,   # printing the given time in seconds to hours and minutes
      "=", resultantTime)

# Below is the Output :

Converting given time in seconds 27500 = 07:38:20
