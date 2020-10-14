def brain_luck(code, program_input):
    out = ''
    data = [0] * 4096
    ord_input = list(map(ord, program_input))
    ip = dp = 0
    while ip != len(code):
        if code[ip] == ',': data[dp] = ord_input.pop(0)
        elif code[ip] == '>': dp += 1
        elif code[ip] == '<': dp -= 1
        elif code[ip] == '+':
            if data[dp] != 255: data[dp] += 1
            else: data[dp] = 0
        elif code[ip] == '-':
            if data[dp] != 0: data[dp] -= 1
            else: data[dp] = 255
        elif code[ip] == '.': out += chr(data[dp])
        elif code[ip] == '[':
            jump = 0
            if data[dp] == 0:
                lc = 1
                jump = ip + 1
                while code[jump] != ']' or lc != 0:
                    jump += 1
                    if code[jump] == '[': lc += 1
                    elif code[jump] == ']': lc -= 1
                else: ip = jump
            else: jump = ip
        elif code[ip] == ']':
            jump = 0
            if data[dp] != 0:
                lc = 1
                jump = ip - 1
                while code[jump] != '[' or lc != 0:
                    jump -= 1
                    if code[jump] == '[': lc -= 1
                    elif code[jump] == ']': lc += 1
                else: ip = jump
        else: pass
        ip += 1

    return out


assert brain_luck(',+[-.,+]', 'Codewars' + chr(255)) == 'Codewars'
assert brain_luck(',[.[-],]', 'Codewars' + chr(0)) == 'Codewars'
assert brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.',
                  chr(8) + chr(9)) == chr(72)
assert brain_luck(
    '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.', '') == 'Hello World!\n'
