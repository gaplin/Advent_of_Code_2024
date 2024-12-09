text = open('input2.txt').read().strip()

text = [int(x) for x in text]

id = 0
n = len(text)
memory = []
for i in range(n):
    if i % 2 == 0:
        for _ in range(text[i]):
            memory.append(id)
        id += 1
    else:
        for _ in range(text[i]):
            memory.append(-1)

n = len(memory)
r = n - 1
for l in range(n):
    if memory[l] == -1:
        while r >= 0 and memory[r] == -1:
            r -= 1
        if r <= l:
            break
        memory[l] = memory[r]
        memory[r] = -1

result = 0
for i in range(n):
    if memory[i] == -1:
        break
    result += i * memory[i]

print(result)