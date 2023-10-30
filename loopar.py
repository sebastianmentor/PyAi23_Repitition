# En loop är ett sätt att iterera!

# count = 0
# while count < 20:
#     print(count)
#     count += 1

# for i in range(20):
#     print(i)

# with open("my_file.txt",'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# l = [tal%29 for tal in range(100)]


# for tal in l:
#     print(tal%13 * '*')

var = None

while (inmatning := input('>>>')) != 'q':
    with open('add_new_lines.txt', 'a', encoding='utf-8') as f:
        f.write(inmatning + '\n' + len(inmatning)*'-'+ '\n')

