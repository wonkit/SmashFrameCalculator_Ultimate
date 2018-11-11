# import sys
#
# class Logger(object):
#     def __init__(self):
#         self.terminal = sys.stdout
#         self.log = open("logfile.txt", "w")
#
#     def write(self, message):
#         self.terminal.write(message)
#         self.log.write(message)
#
#     def flush(self):
#         #this flush method is needed for python 3 compatibility.
#         #this handles the flush command by doing nothing.
#         #you might want to specify some extra behavior here.
#         pass
#
# sys.stdout = Logger()

########################################################################

with open('frame_data.txt') as f:
    source_file = list(f);

f.close()

import math
import re

def listToMs(mylist):
    return int(mylist[2]) * 10 + int(mylist[1]) * 1000 + int(mylist[0]) * 60000

def getDeltaTime(time1, time2):
    timeStart = re.split(r'[:|.]', time1)
    timeEnd = re.split(r'[:|.]', time2)

    timeStartMilli = listToMs(timeStart)
    timeEndMilli = listToMs(timeEnd)

    return timeStartMilli - timeEndMilli

def printComparison(new, old):
    MarginOfError = 1
    withinMoE = False

    difference = new - old

    text = "("

    if (math.fabs(difference) <= MarginOfError):
        withinMoE = True

    if (difference < 0):
        text += f'{difference * -1} frames FASTER than Smash 4'
        if (withinMoE):
            text+= f' **but is within the margin of error of {MarginOfError} frames)**'
        else:
            text += ' and is likely buffed)'
    elif (difference > 0):
        text += f'{difference} frames SLOWER than Smash 4'
        if (withinMoE):
            text += f' **but is within the margin of error of {MarginOfError} frames)**'
        else:
            text += ' and is likely nerfed)'
    else:
        text += f'likely unchanged)'
    return text

move = {}

import os
import errno



def longScript(move_name, move_start, move_start_image, move_hit, move_hit_image, move_end, move_end_image, original_hit, original_faf, aerial_flag, notes):
    filename = f"{os.getcwd()}/moves/{move_name}.txt"

    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    f = open(filename, "w+")


    f.write("---------------------------------")
    f.write(f"\n**{move_name}**")
    f.write("\n---------------------------------")
    f.write(f"\n\nThe first frame where {move_name} starts is at {move_start}\n")
    f.write(move_start_image)
    f.write(f"\n\nThe first frame where {move_name} has a hitbox is at {move_hit}\n")
    f.write(move_hit_image)
    f.write(f"\n\nThe first frame where {move_name} can be acted out of is at {move_end}\n")
    f.write(move_end_image)
    f.write(f"\n\n\nAs a recap:\nStartingFrame: **{move_start}**"
            f"\nHitboxFrame: **{move_hit}**"
            f"\nVisiblyActingFrame: **{move_end}**")

    f.write(f"\n\n*__Hit Frame__*")
    f.write(f"\n\nMath Time: ")
    f.write(f"\n```"
            f"StartingFrame - HitboxFrame")

    newHit = getDeltaTime(move_start, move_hit)
    newHitFrame = newHit / 16.67

    newFAF = getDeltaTime(move_start, move_end)
    newFAFFrame = newFAF / 16.67


    f.write(f"\n{move_start} - {move_hit} = {newHit} ms"
            f"\n1 frame = 16.67 ms"
            f"\n{newHit} ms / 16.67 ms = {newHitFrame} => {math.ceil(newHitFrame)} frames")
    f.write(f"```")

    f.write(f"\n\n*__First Active Frame__*")
    f.write(f"\n\nMath Time: ")
    f.write(f"\n```"
            f"StartingFrame - VisiblyActingFrame")

    f.write(f"\n{move_start} - {move_end} = {newFAF} ms"
            f"\n1 frame = 16.67 ms"
            f"\n{newHit} ms / 16.67 ms = {newFAFFrame} => {math.ceil(newFAFFrame)} frames")
    f.write(f"```")

    f.write("\n\n__In total with conservative estimates:__")
    f.write(f"\nFirst hitbox comes out on about **Frame {math.ceil(newHitFrame)}** "
            f"{printComparison(math.ceil(newHitFrame), original_hit)}")
    f.write(f"\nFAF is about **Frame {math.ceil(newFAFFrame)}** "
            f"{printComparison(math.ceil(newFAFFrame), original_faf)}")
    f.write(f"{notes}\n")

    f.close()

def shortScript(move_name, move_start, move_start_image, move_hit, move_hit_image, move_end, move_end_image, original_hit, original_faf, aerial_flag, notes, file):

    newHit = getDeltaTime(move_start, move_hit)
    newHitFrame = newHit / 16.67
    newFAF = getDeltaTime(move_start, move_end)
    newFAFFrame = newFAF / 16.67

    file.write(f"**{move_name}**: \n\t__Hit__ *Frame {math.ceil(newHitFrame)}* \t{printComparison(math.ceil(newHitFrame), original_hit)}"
               f"\n\t__FAF__ *Frame {math.ceil(newFAFFrame)}* \t{printComparison(math.ceil(newFAFFrame), original_faf)}"
               f"{notes}\n")



short = open(f"summary.txt", "w+")
for i in range(source_file.__len__()):
    data = source_file[i].split()
    if data.__len__() > 0:
        if '#' not in data[0]:
            print(data[0])

    if data.__len__() >= 9:
        if '#' not in data[0]:
            move_name = data[0]
            move_start = data[1]
            move_start_image = data[2]
            move_hit = data[3]
            move_hit_image = data[4]
            move_end = data[5]
            move_end_image = data[6]
            original_hit = int(data[7])
            original_faf = int(data[8])
            aerial_flag = int(data[9])
            notes_index = 10
            if aerial_flag == 0:
                notes_index = 11

            notes = '\n'
            if data.__len__() > notes_index:
                notes += 'NOTES: '
                for i in range(10, data.__len__()):
                    notes += data[i] + ' '
                notes += '\n'

            newHit = getDeltaTime(move_start, move_hit)
            newHitFrame = newHit / 16.67

            newFAF = getDeltaTime(move_start, move_end)
            newFAFFrame = newFAF / 16.67


            shortScript(move_name, move_start, move_start_image, move_hit, move_hit_image, move_end, move_end_image, original_hit, original_faf, aerial_flag, notes, short)
            longScript(move_name, move_start, move_start_image, move_hit, move_hit_image, move_end, move_end_image, original_hit, original_faf, aerial_flag, notes)

short.close()

    #move[data[0]] = [ data[j].split(':') for j in range(1, data.__len__())]

# for i in move.keys():
#     print(i)
#     for j in move[i]:
#         print('https://www.youtube.com/watch?v=MhLrqVQCZ7Q&feature=youtu.be&t=' + j[0] + 'm' + j[1] + 's')
#     print('')
#
# #print(move)

