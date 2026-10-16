expression = input()

n1 = int(expression[0])
op = expression [1]
n2 = int(expression [2])

result = 0

if op == '+':
  result = n1 + n2
elif op == '-':
  result = n1 - n2
elif op == '/':
   result = n1 / n2
elif op == '*' or 'x':
    result = n1 * n2
else:
  result = 'Invalid'

print(f"={result}")
