''' При запуске сформируется файл append.txt
в который запишутся все файлы из списка file_name
в порядке возрастания количества строк '''
file_name = ['1.txt', '2.txt', '3.txt']
line_dict = {}
line = []
for file in file_name:
    if line_dict.get(sum(1 for line in open(file))) is None:
        line_dict[sum(1 for line in open(file))] = [file]
        line.append(sum(1 for line in open(file)))
    else:
        line_dict[sum(1 for line in open(file))] += [file]
        line.append(sum(1 for line in open(file)))

line_set = set(line)
line = list(line_set)
line.sort()
file_open = 'append.txt'
with open(file_open, 'w') as f:
    for li in line:
        for l_file in line_dict[li]:
            with open(l_file) as file:
                data = file.read()
            f.write(str(l_file) + '\n')
            f.write(str(li) + '\n')
            f.write(data)
            f.write('\n\n')
            f.flush()
