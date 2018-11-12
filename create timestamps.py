with open('time.txt') as f:
    time_file = list(f);

f.close()

move = {}
for i in range(time_file.__len__()):
    data = time_file[i].split()
    move[data[0]] = [ data[j].split(':') for j in range(1, data.__len__())]

for i in move.keys():
    print(i)
    for j in move[i]:
        print('https://www.youtube.com/watch?v=MhLrqVQCZ7Q&feature=youtu.be&t=' + j[0] + 'm' + j[1] + 's')
    print('')

#print(move)

