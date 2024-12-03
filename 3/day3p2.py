import re

def get_value(text: str) -> int:
    closing_idx =  text.find(')')
    if closing_idx == -1:
        return 0
    text = text[4:closing_idx]
    if re.fullmatch(r'\d{1,3},\d{1,3}', text):
        nums = [int(x) for x in text.split(',')]
        return nums[0] * nums[1]
    return 0

input = open('input2.txt').read().strip()

enabled = True
result = 0
for i in range(len(input)):
    if input[i:].startswith('do()'):
        enabled = True
    elif input[i:].startswith('don\'t()'):
        enabled = False
    elif input[i:].startswith('mul('):
        if enabled == True:
            result += get_value(input[i:])

print(result)