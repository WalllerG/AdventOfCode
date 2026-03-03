import re
from Util.util import read_input

data = read_input(13, False)

for i in range(0,len(data),4):
    matchA = re.findall(r"(\d+), (\d+)",data[i])
    matchB = re.findall(r"(\d+), (\d+)",data[i+1])
    matchC = re.findall(r"(\d+), (\d+)",data[i+2])
    print(matchA[0],matchB[0],matchC[0])

