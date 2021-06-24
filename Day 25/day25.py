pos = 0
state = 'A'
tape = {}

steps = 12481997
for i in range(steps):

    per = (i / steps) * 100
    if per % 1 == 0:
        print(per,"% done")


    if pos not in tape:
        tape[pos] = 0
    val = tape[pos]

    if state == 'A':
        if val == 0:
            tape[pos] = 1
            pos += 1
            state = 'B'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'C'
    elif state == 'B':
        if val == 0:
            tape[pos] = 1
            pos -= 1
            state = 'A'
        else:
            tape[pos] = 1
            pos += 1
            state = 'D'
    elif state == 'C':
        if val == 0:
            tape[pos] = 0
            pos -= 1
            state = 'B'
        else:
            tape[pos] = 0
            pos -= 1
            state = 'E'
    elif state == 'D':
        if val == 0:
            tape[pos] = 1
            pos += 1
            state = 'A'
        else:
            tape[pos] = 0
            pos += 1
            state = 'B'
    elif state == 'E':
        if val == 0:
            tape[pos] = 1
            pos -= 1
            state = 'F'
        else:
            tape[pos] = 1
            pos -= 1
            state = 'C'
    elif state == 'F':
        if val == 0:
            tape[pos] = 1
            pos += 1
            state = 'D'
        else:
            tape[pos] = 1
            pos += 1
            state = 'A'

print( list(tape.values()).count(1) )
