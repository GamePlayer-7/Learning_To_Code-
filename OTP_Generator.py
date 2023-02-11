import math, random

corpus= "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
generate_OTP = "" 
size=5
length = len(corpus) 
for i in range(size) : 
  generate_OTP+= corpus[math.floor(random.random() * length)] 
print(generate_OTP)
