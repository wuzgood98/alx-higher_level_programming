#!/usr/bin/python3
for num in range(90):
    if (num % 10) > int(num / 10):
        if num == 89:
            print("{}".format(num))
        else:
            print("{:02}".format(num), end=", ")
