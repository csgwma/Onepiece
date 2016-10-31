
while val != 0:
val = int(raw_input("enter a score"))
    if val == 0 or val < 0:
        print "you enter a invalide number", val
        break
    if val >= 90:
        print "A"
    elif val >= 80:
        print "B"
    elif val >= 70:
        print "C"
    elif val >= 60:
        print "D"
    else:
        print "E"
else:
    print "the while loop is over"

print "Done"
