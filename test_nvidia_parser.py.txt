fullFileName = 'ibdiagnet_output.txt'


def handler(f):
    n_warn = n_err = s_warn = s_err = 0
    for line in f:

        if line.find('Nodes Information') > 0 and line.find(':') == -1:
            values = line.strip().split(' ')
            temp = []
            [temp.append(x) for x in values if x not in temp]
            # print(temp)
            n_warn = temp[-1]
            n_err = temp[-2]

        if line.startswith('-I- Speed / Width checks'):
            values = line.strip().split(' ')
            temp2 = []
            [temp2.append(x) for x in values if x not in temp2]
            # print(temp2)
            s_warn = temp2[-1]
            s_err = temp2[-2]
    return n_warn, n_err, s_warn, s_err


def reader(fn):
    try:
        with open(fn, encoding='utf-8') as f:
            print(f'=== Parsing: {fn} ====')
            print()
            n_warn, n_err, s_warn, s_err = handler(f)
            print(f'Nodes Information section has {n_warn} Warnings and {n_err} Errors')
            print(f'Speed / Width checks section has {s_warn} Warnings and {s_err} Errors')
    finally:
        print()
        print(f'=== Well, {fullFileName} was parsed ===')


if __name__ == '__main__':
    reader(fullFileName)
