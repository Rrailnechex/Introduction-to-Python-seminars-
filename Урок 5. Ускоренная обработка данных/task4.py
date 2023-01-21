

""" Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных."""


def rle_zip(inp):
    r = []
    cr = inp[0]  # current character
    cc = 1  # current count
    for i in range(1, len(inp)):
        if inp[i] == cr:
            cc += 1
        else:
            r.append((cr, cc))
            cr = inp[i]
            cc = 1
    r.append((cr, cc))
    return r


def rle_unzip(inp):
    r = ""
    for i in inp:
        r += i[0] * i[1]
    return r


my_file = "1111122233311111eeeeeeerrrrrtttttttttttttt11111111111"
# my_file = "attatttttttttttttaaaaaaaaaaaaaaaattattttatttatttt"


print("1", my_file)
my_new = rle_zip(my_file)
print("2", my_new)
unzipped = rle_unzip(my_new)
print("3", unzipped)
