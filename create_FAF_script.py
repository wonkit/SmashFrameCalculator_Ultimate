

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

def printMathTime(start, end, new, f):
    f.write(f"\n\nMath Time: ")
    f.write(f"\n```"
            f"StartingFrame - HitboxFrame")

    f.write(f"\n{start} - {end} = {new} ms"
            f"\n1 frame = 16.67 ms"
            f"\n{new} ms / 16.67 ms = {new / 16.67} => {math.ceil(new / 16.67)} frames")
    f.write(f"```")

# item is a tuple consisting of move[new], move[old], a string containing title
def printAllCalc(f, item, move_name):

    move_start = item[0][1]
    move_end = item[0][2]
    text = item[2]
    string_list1 = item[3]
    string_list2 = item[4]
    image_link = [item[0][3], item[0][4]]


    new = getDeltaTime(move_start, move_end)

    # print title
    f.write(f"\n\n*{text}*\n")

    f.write(f"\n{string_list1[0]} {move_name} {string_list1[1]} {move_start}"
            f"\n<{image_link[0]}>")
    f.write(f"\n\n{string_list2[0]} {move_name} {string_list2[1]} {move_end}"
            f"\n<{image_link[1]}>")

    f.write(f"\n\nAs a recap:"
            f"\n{string_list1[2]}: {move_start}"
            f"\n{string_list2[2]}: {move_end}")
    printMathTime(move_start, move_end, new, f)



    # f.write(f"\n\n*__First Active Frame__*")
    # f.write(f"\n\nMath Time: ")
    # f.write(f"\n```"
    #         f"StartingFrame - VisiblyActingFrame")
    #
    # f.write(f"\n{move_start} - {move_end} = {newFAF} ms"
    #         f"\n1 frame = 16.67 ms"
    #         f"\n{newHit} ms / 16.67 ms = {newFAFFrame} => {math.ceil(newFAFFrame)} frames")
    # f.write(f"```")
    #
    # f.write("\n\n__In total with conservative estimates:__")
    # f.write(f"\nFirst hitbox comes out on about **Frame {math.ceil(newHitFrame)}** "
    #         f"{printComparison(math.ceil(newHitFrame), original_hit)}")
    # f.write(f"\nFAF is about **Frame {math.ceil(newFAFFrame)}** "
    #         f"{printComparison(math.ceil(newFAFFrame), original_faf)}")
    # f.write(f"{notes}\n")
    




start_string = ['The first frame where', 'can start is at', 'StartingFrame']
hitbox_string = ['The first frame where', 'has a hitbox is at', 'HitboxFrame']
FAF_string = ['The first frame where', 'can be acted out of is', 'ActFrame']
land_string = ['The frame that', 'lands on is', 'LandFrame']


def longScript(dict):
    for i in dict:
        move_name = i

        # create file
        filename = f"{os.getcwd()}/moves/{move_name}.txt"

        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise
        f = open(filename, "w+")

        move = dict[i]
        # define variables

        # move_hit = 'NULL'
        # move_hit_image = 'NULL'
        # move_end = 'NULL'
        # move_end_image = 'NULL'
        # move_ac = 'NULL'
        # move_ac_image = 'NULL'
        # move_land = 'NULL'
        # move_land_image = 'NULL'
        # o_faf = -1
        # o_ac = -1
        # o_lg = -1


        list = []
        total = []

        if 'newHit' in dict[i]:
            list.append([move['newHit'], move['oldHit'], '__Hit Frame__', start_string, hitbox_string])
            new = math.ceil(move['newHit'][0])
            total.append(f"First Hitbox comes out on **Frame "
                         f"{new}** {printComparison(new, move['oldHit'])}")

        if 'newFAF' in dict[i]:
            list.append([move['newFAF'], move['oldFAF'], '__First Active Frame (FAF)__', start_string, FAF_string])
            new = math.ceil(move['newFAF'][0])
            total.append(f"Can act on **Frame "
                         f"{new}** {printComparison(new, move['oldFAF'])}")

        if 'newAC' in dict[i]:
            list.append([move['newAC'], move['oldAC'], '__Autocancel__', start_string, FAF_string])
            new = math.ceil(move['newAC'][0])
            total.append(f"Autocancels on **Frame "
                         f"{new}** {printComparison(new, move['oldAC'])}")

        if 'newLLag' in dict[i]:
            list.append([move['newLLag'], move['oldLLag'], '__Landing Lag__', land_string, FAF_string])
            new = math.ceil(move['newLLag'][0])
            total.append(f"Has this many frames of landing lag: **Frame "
                         f"{new}** {printComparison(new, move['oldLLag'])}")

        f.write("---------------------------------")
        f.write(f"\n**{move_name}**")
        f.write("\n---------------------------------")

        for item in list:
            printAllCalc(f, item, move_name)
        f.write(f"\n\n__In Total:__")
        for j in total:
            f.write(f"\n{j}")
        f.close()

def shortScript(dict):
    short = open("summary.txt", "w+")
    for i in dict:
        # get varibles from dictionary

        mymove = dict[i]
        #print to file
        short.write(f"**{i}**: ")

        if 'newHit' in mymove:
            oldHit = mymove.get('oldHit')
            newHit = math.ceil((mymove.get('newHit')[0]))
            short.write(f"\n\t__Hit__ *Frame {newHit}* "
                    f"\t{printComparison(newHit, oldHit)}")
        if 'newFAF' in mymove:
            oldFAF = mymove.get('oldFAF')
            newFAF = math.ceil((mymove.get('newFAF')[0]))
            short.write(f"\n\t__FAF__ *Frame {newFAF}* "
                    f"\t{printComparison(newFAF, oldFAF)}")
        if 'newLLag' in mymove:
            oldLLag = mymove.get('oldLLag')
            newLLag = math.ceil(mymove.get('newLLag')[0])
            short.write(f"\n\t__Landing Lag__ *Frame {newLLag}* "
                    f"\t{printComparison(newLLag, oldLLag)}")
# Autocancel
# Warning: Not that accurate
        if 'newAC' in mymove:
            oldAC = mymove.get('oldAC')
            newAC = math.ceil(mymove.get('newAC')[0])
            short.write(f"\n\t__AC__ *Frame {newAC}* "
                    f"\t{printComparison(newAC, oldAC)}")



        #print aerial information
        #short.write(f"\n\t__Landing Lag__ *Frame ")

        #print any notes
        if 'notes' in mymove:
            short.write(f"{mymove.get('notes')}\n")
        else:
            short.write('\n\n')
    short.close()



# calculates frame data based on start and finish of timer
def calculateNewFrame(start, end):
    new = getDeltaTime(start, end) / 16.67
    return [new , math.ceil(new)]


def add2dict(d, key, thing):
    if key not in d:
        d[key] = thing
    elif key == 'notes':
        d[key] = d[key] + thing


moves = {}
for i in range(source_file.__len__()):
    data = source_file[i].split()

    length = data.__len__()
    if length > 1:
        if '#' not in data[0]:
            move_name = data[0]
            move_start = 'NULL'
            move_start_image = 'NULL'
            move_hit = 'NULL'
            move_hit_image = 'NULL'
            move_end = 'NULL'
            move_end_image = 'NULL'
            original_hit = -1
            original_faf = -1
            aerial_flag = 0
            landing_frame = 'NULL'
            landing_frame_image = 'NULL'
            ac_frame = 'NULL'
            ac_frame_image = 'NULL'
            original_l_lag = -1
            original_ac_frame = -1;
            notes_index = -1

            # get all arguments
            counter = 1;
            while counter < length:
                param = data[counter]
                if (param == '-s'):
                    move_start = data[counter + 1]
                    counter += 2
                elif (param == '-h'):
                    move_hit = data[counter + 1]
                    counter += 2
                elif (param == '-e'):
                    move_end = data[counter + 1]
                    counter += 2
                elif (param == '-si'):
                    move_start_image = data[counter + 1]
                    counter += 2
                elif (param == '-hi'):
                    move_hit_image = data[counter + 1]
                    counter += 2
                elif (param == '-ei'):
                    move_end_image = data[counter + 1]
                    counter += 2
                elif (param == '-oh'):
                    original_hit = int(data[counter + 1])
                    counter += 2
                elif (param == '-of'):
                    original_faf = int(data[counter + 1])
                    counter += 2
                elif (param == '-a'):
                    aerial_flag = int(data[counter + 1])
                    counter += 2
                elif (param == '-lf'):
                    landing_frame = data[counter + 1]
                    counter += 2
                elif (param == '-lfi'):
                    landing_frame_image = data[counter + 1]
                    counter += 2
                elif (param == '-ac'):
                    ac_frame = data[counter + 1]
                    counter += 2
                elif (param == '-aci'):
                    ac_frame_image = data[counter + 1]
                    counter += 2
                elif (param == '-olg'):
                    original_l_lag = int(data[counter + 1])
                    counter += 2
                elif (param == '-oac'):
                    original_ac_frame = int(data[counter + 1])
                    counter += 2
                elif (param == '-n'):
                    notes_index = counter + 1
                    break;
                else: counter += 1

            notes = '\n'
            if notes_index > 1:
                notes += 'NOTES: '
                for i in range(notes_index, length):
                    notes += data[i] + ' '
                notes += '\n'

            # print('movestart', move_start)
            # print('move_hit', move_hit)
            # print('move_end', move_end)
            # print('original_hit', original_hit)
            # print('original_faf', original_faf)
            #
            # print('aerial_flag', aerial_flag)
            # print('landing_frame', landing_frame)
            # print('ac_frame', ac_frame)
            # print('original_l_lag', original_l_lag)
            # print('original_ac_frame', original_ac_frame)
            #
            # print('move_start_image',move_start_image)
            # print('move_hit_image', move_hit_image)
            # print('move_end_image', move_end_image)
            # print(notes)

            if move_name not in moves:
                moves[move_name] = {}
            d = moves[move_name]

            # add new hit frame
            if move_hit != 'NULL':
                newHit, newHitFrame = calculateNewFrame(move_start, move_hit)
                add2dict(d, 'newHit', [newHit, move_start, move_hit , move_start_image, move_hit_image])

            if move_end != 'NULL':
                # check landing frames
                if landing_frame != 'NULL':
                    newLLag, newLLagFrame = calculateNewFrame(landing_frame, move_end)
                    add2dict(d, 'newLLag', [newLLag, landing_frame, move_end, landing_frame_image, move_end_image])
                # check faf
                else:
                    newFAF, newFAFFrame = calculateNewFrame(move_start, move_end)
                    add2dict(d, 'newFAF', [newFAF, move_start, move_end, move_start_image, move_end_image])
            # check autocancel frames
            elif ac_frame != 'NULL':
                newAC, newACFrame = calculateNewFrame(move_start, ac_frame)
                add2dict(d, 'newAC', [newAC, move_start, ac_frame, '', ''])

            add2dict(d, 'oldHit', original_hit)
            add2dict(d, 'oldFAF', original_faf)
            add2dict(d, 'oldLLag', original_l_lag)
            add2dict(d, 'oldAC', original_ac_frame)

            if notes != '\n':
                add2dict(d, 'notes', notes)


shortScript(moves)
longScript(moves)


