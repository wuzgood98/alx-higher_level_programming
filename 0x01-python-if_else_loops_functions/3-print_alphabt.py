#!/usr/bin/python3
for alphabet in range(26):
    if (alphabet == 4) or (alphabet == 16):
        continue
    print("{}".format(chr(alphabet + 97)), end="")
