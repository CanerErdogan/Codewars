s = 'abcdefghi'

out = []
for i in range(0, len(s), 2):
    out.append(s[i:i+2]) if i+1 < len(s) else out.append(s[-1] + '_')

print(out)
