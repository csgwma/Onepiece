# coding=utf-8
__author__ = 'Ace'

resultfile = 'result_file_kdd_10000'
reader = file(resultfile, 'r')

results = list()

lineno = 0
for line in reader:
    tokens = line.strip().split()
    tokens[0] = tokens[0].strip()
    tokens[1] = int(tokens[1].strip())
    tokens[2] = float(tokens[2].strip())

    if lineno < 25:
        results.append(tokens)
    else:
        id = lineno % 25
        atuple = results[id]
        atuple[1] += tokens[1]
        atuple[2] += tokens[2]
    lineno += 1
reader.close()

times = lineno / 25 + 1
formatstrn = '%15s %10.6f %10.6f\n'
writer = file(resultfile+'_ok', 'w')  # Notice the output filename
for lr in results:
    writer.write(formatstrn % (lr[0],float(lr[1])/times, lr[2]/times))
writer.close()