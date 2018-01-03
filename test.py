import re
pattern = '\w\dpython\w'
string = 'abcdfphp345pythony_py'
result = re.search(pattern,string)
print(result)