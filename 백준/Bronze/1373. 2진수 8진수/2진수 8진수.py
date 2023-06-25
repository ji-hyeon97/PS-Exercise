import sys

data = sys.stdin.readline().rstrip()
value = "0b"+data
intValue = int(value,2)

print(oct(intValue).replace("0o",""))