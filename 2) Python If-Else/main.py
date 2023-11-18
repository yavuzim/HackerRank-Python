import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2==1:
        message = "Weird"
    elif n>1 and n<6:
        message = "Not Weird"
    elif n>5 and n<21:
        message = "Weird"
    else:
        message = "Not Weird"
    print(message)