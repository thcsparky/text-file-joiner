import os
biglist = []
tinylist = []

def getcontents(str):
    scans = os.scandir(str)
    dirs = []
    files = []
    for x in scans:
        if x.is_dir() == True:
            dirs.append(x.path)
        else:
            files.append(x.path)

    rout = dirs + files

    return(rout)
def compileOn():
    global tinylist

    a = tinylist

    b = input('file types to join: txt,rtf\n').rstrip()
    if b.find(',') > -1:
        multype = b.split(',')
    else:
        multype = [b]

    c = input('\nFile to save as: ').rstrip()

    with open(os.getcwd() + '/' + c, 'w') as out:
        for x in a: ##a being the list grabbed
            try:
                for y in multype:
                    if x.find(y) > -1 and x.endswith('.d') == False:

                        fileio = open(x)
                        reading = fileio.read()
                        out.write(reading)
                        fileio.close
            except Exception as i:
                print('Skipping ' + x + 'Reason: ')
                print(i)
                continue

    out.close()
    print('Written to: ' + os.getcwd() + '/' + c)
    quit()


def wholedir(str, w):
    dirsearch = []
    global tinylist #files
    global biglist

    try:
        tlist = os.scandir(str)
        filepaths = []

        for x in tlist:
            if x.is_file() == True and x.path not in tinylist:
                tinylist.append(x.path)
            if x.is_dir() == True and x.path not in biglist:
                biglist.append(x.path)

        if len(biglist) > 0:
            again = biglist.pop(0)
            runme = wholedir(again, w)
            return(runme)

        else:
            if w != 'n':

                compileOn()
                return(tinylist)
            else:
                return(tinylist)
    except Exception as e:
        print(e)
        print('\n')
        again = biglist.pop(0)
        runme = wholedir(again, w)
        return(runme)
def killdupes(str):
    a = open(str)
    b = a.read()
    b2 = b.splitlines()

    a.close()

    listdupes = []
    for x in b2:
        print('processing: ' + x  + '\n')
        for y in b2:
            if x == y:
                listdupes.append(y)


    print('dupes: ')
    finalstring = b
    for x in listdupes:
        for y in b2:
            if x == y:
                finalstring = finalstring.replace(x, '')

    fileio = open(str, 'w')
    fileio.write(finalstring)
    fileio.close
    print('COmplete: ')

def thisdir(str):
    a = getcontents(str)
    print ('\n\n')
    b = input('file types to join: txt,rtf\n').rstrip()
    if b.find(',') > -1:
        multype = b.split(',')
    else:
        multype = [b]

    c = input('\nFile to save as: ').rstrip()

    with open(os.getcwd() + '/' + c, 'w') as out:
        for x in a: ##a being the list grabbed
            try:
                for y in multype:
                    if x.find(y) > -1 and x.endswith('.d') == False:

                        fileio = open(x)
                        reading = fileio.read()
                        out.write(reading)
                        fileio.close
            except Exception as i:
                print('Skipping ' + x + 'Reason: ')
                print(i)
                continue

    out.close()
    print('Written to: ' + os.getcwd() + '/' + c)
    quit()


def main():
    inp = input('\n').rstrip()
    global biglist
    global tinylist
    ##list only
    print (inp.split(' ')[0])
    if inp.split(' ')[0] == 'killdupes':
        killdupes(inp.split(' ')[1])
        return(main())


    if inp.split(' ')[0] == 'listall':
        a = wholedir(inp.split(' ')[1], 'n')
        print(a)
        print('\n')
        return(main())

    if inp.split(' ')[0] == 'saveall':
        a = wholedir(inp.split(' ')[1], 'n')
        texte = ''
        for b in a:
            texte += b + '\n'

        fileio = open(os.getcwd() + '/allfiles.txt', 'w')
        fileio.write(texte)
        fileio.close()
        print('saved to allfiles.txt')

    if inp.split(' ')[0] == 'list':
        print('Getting contents for: '  + inp.split(' ')[1] + '\n\n')

        o = getcontents(inp.split(' ')[1])
        print(o)

    elif inp.split(' ')[0] == 'start':

        ##compile
        pos = inp.replace('start ', ' ').split(' ')

        if pos[2] != 'y' and pos[2] != 'n':
            print('no valid args')
            quit()
        else:
            if pos[2].find('y') > -1:
                biglist = []
                tinylist = []
                a = wholedir(pos[1], 'y')

                print(a)
            elif pos[2].find('n') > -1:
                a = thisdir(pos[1])
                print(a)
    main()

if __name__ == '__main__':
    print('start (/) (y/n) [Subdirs?] \n Alternatively: type list /')
    print('\nor type listall /\nkilldupes file.txt\n')
    print ('ALTERNATIVELY: biglistall /\n')
    print('/saveall filename\n')
    main()
