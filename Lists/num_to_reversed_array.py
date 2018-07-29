def digitize(n):
    return [int(x) for x in str(n)[::-1]]

print(digitize(4555))
# =============================================
def find_next_letter(chars):
    return chr(ord(chars[-1]) +1)

print(find_next_letter(['O','P','Q','R','S']))
# =============================================
def find_missing_letter(chars):
    n = 0
    while ord(chars[n]) == ord(chars[n+1]) - 1:
        n += 1
    return chr(1+ord(chars[n]))

print(find_missing_letter(['O','Q','R','S']))
