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
slots = []
i = 0
while i < n:
    if memory[i] == -1:
        length = 0
        start = i
        while i < n and memory[i] == -1:
            i += 1
            length += 1
        slots.append([start, length])
    else:
        i += 1

files = []
i = 0
while i < n:
    if memory[i] != -1:
        id = memory[i]
        length = 0
        start = i
        while i < n and memory[i] == id:
            i += 1
            length += 1
        files.append([start, length, id])
    else:
        i += 1

f = len(files) - 1
n_slots = len(slots)
while f >= 0:
    size = files[f][1]
    for i in range(n_slots):
        if slots[i][0] >= files[f][0]:
            break
        if slots[i][1] >= files[f][1]:
            for j in range(size):
                memory[files[f][0] + j] = -1
                memory[slots[i][0] + j] = files[f][2]
            slots[i][0] += size
            slots[i][1] -= size
            if slots[i][1] == 0:
                slots.pop(i)
            break
    f -= 1
    
result = 0
for i in range(n):
    if memory[i] == -1:
        continue
    result += i * memory[i]

print(result)