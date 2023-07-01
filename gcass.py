# GCode ASSembly code

import pygcode as pygcode
import sys

def main():
    '''
    read code line by line and parse all the different gcass statements.
    - first runthrough finds all marks for later reference.
    '''
    inPath = ""
    outPath = ""
    if len(sys.argv) == 2:
        inPath = sys.argv[1]
    elif len(sys.argv) == 3:
        inPath, outPath = sys.argv[1:]

    file = open(inPath, 'r')
    lines = file.readlines()
    marks = dict()
    
    for i, line in enumerate(lines):
        if "@mark" in line:
            mark = line.removeprefix('@mark ')
            if ";" in mark: mark = mark.split(';')[0]
            mark = mark.strip()
            marks[mark] = i

    output = list()

    cl = 0 # currentLine
    regs = {'w': 0.0,
            'x': 0.0,
            'y': 0.0,
            'z': 0.0}

    while cl<len(lines):
        if '@' in lines[cl]:
            if   '@mark' in lines[cl]:
                pass
            elif '@set' in lines[cl]: 
                _, r, v = lines[cl].split(';')[0].split()
                regs[r] = float(v)
            elif '@add' in lines[cl]:
                _, r, v = lines[cl].split(';')[0].split()
                regs[r] =  regs[r]+float(v)
            elif '@jiz' in lines[cl]:
                _, r, v = lines[cl].split(';')[0].split()
                if regs[r] == 0:
                    cl = marks[v]
            elif '@jinz' in lines[cl]:
                _, r, v = lines[cl].split(';')[0].split()
                if regs[r] != 0:
                    cl = marks[v]


        elif '<' in lines[cl]:
            reconstruct = list()
            deconstruct = lines[cl].split('<')
            for part in deconstruct:
                if '>' in part:
                    reconstruct += str(regs[part.split('>')[0]])
                else:
                    reconstruct += part
            output += ''.join(reconstruct) + '\n'

        else:
            output += lines[cl]
        cl += 1

    file.close()


    with open(outPath, 'w') as outFile:
        for line in output:
            outFile.write(line)
    
if __name__ == "__main__":
    main()
