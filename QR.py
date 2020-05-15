import png

def RSCorrectionCode(codes):
    genPolinom = [173, 125, 158, 2, 103, 182, 118, 17, 145, 201, 111, 28, 165, 53, 161, 21, 245, 142, 13, 102, 48, 227, 153, 145, 218, 70]

    galoisField = [
        1, 2, 4, 8, 16, 32, 64, 128, 29, 58, 116, 232, 205, 135, 19, 38, 76, 152,
        45, 90, 180, 117, 234, 201, 143, 3, 6, 12, 24, 48, 96, 192, 157, 39, 78,
        156, 37, 74, 148, 53, 106, 212, 181, 119, 238, 193, 159, 35, 70, 140, 5,
        10, 20, 40, 80, 160, 93, 186, 105, 210, 185, 111, 222, 161, 95, 190, 97,
        194, 153, 47, 94, 188, 101, 202, 137, 15, 30, 60, 120, 240, 253, 231, 211,
        187, 107, 214, 177, 127, 254, 225, 223, 163, 91, 182, 113, 226, 217, 175,
        67, 134, 17, 34, 68, 136, 13, 26, 52, 104, 208, 189, 103, 206, 129, 31,
        62, 124, 248, 237, 199, 147, 59, 118, 236, 197, 151, 51, 102, 204, 133,
        23, 46, 92, 184, 109, 218, 169, 79, 158, 33, 66, 132, 21, 42, 84, 168, 77,
        154, 41, 82, 164, 85, 170, 73, 146, 57, 114, 228, 213, 183, 115, 230, 209,
        191, 99, 198, 145, 63, 126, 252, 229, 215, 179, 123, 246, 241, 255, 227,
        219, 171, 75, 150, 49, 98, 196, 149, 55, 110, 220, 165, 87, 174, 65, 130,
        25, 50, 100, 200, 141, 7, 14, 28, 56, 112, 224, 221, 167, 83, 166, 81,
        162, 89, 178, 121, 242, 249, 239, 195, 155, 43, 86, 172, 69, 138, 9, 18,
        36, 72, 144, 61, 122, 244, 245, 247, 243, 251, 235, 203, 139, 11, 22, 44,
        88, 176, 125, 250, 233, 207, 131, 27, 54, 108, 216, 173, 71, 142, 1,]

    galoisAntiField = [
        None, 0, 1, 25, 2, 50, 26, 198, 3, 223, 51, 238, 27, 104, 199, 75, 4, 100,
        224, 14, 52, 141, 239, 129, 28, 193, 105, 248, 200, 8, 76, 113, 5, 138,
        101, 47, 225, 36, 15, 33, 53, 147, 142, 218, 240, 18, 130, 69, 29, 181,
        194, 125, 106, 39, 249, 185, 201, 154, 9, 120, 77, 228, 114, 166, 6, 191,
        139, 98, 102, 221, 48, 253, 226, 152, 37, 179, 16, 145, 34, 136, 54, 208,
        148, 206, 143, 150, 219, 189, 241, 210, 19, 92, 131, 56, 70, 64, 30, 66,
        182, 163, 195, 72, 126, 110, 107, 58, 40, 84, 250, 133, 186, 61, 202, 94,
        155, 159, 10, 21, 121, 43, 78, 212, 229, 172, 115, 243, 167, 87, 7, 112,
        192, 247, 140, 128, 99, 13, 103, 74, 222, 237, 49, 197, 254, 24, 227, 165,
        153, 119, 38, 184, 180, 124, 17, 68, 146, 217, 35, 32, 137, 46, 55, 63,
        209, 91, 149, 188, 207, 205, 144, 135, 151, 178, 220, 252, 190, 97, 242,
        86, 211, 171, 20, 42, 93, 158, 132, 60, 57, 83, 71, 109, 65, 162, 31, 45,
        67, 216, 183, 123, 164, 118, 196, 23, 73, 236, 127, 12, 111, 246, 108,
        161, 59, 82, 41, 157, 85, 170, 251, 96, 134, 177, 187, 204, 62, 90, 203,
        89, 95, 176, 156, 169, 160, 81, 11, 245, 22, 235, 122, 117, 44, 215, 79,
        174, 213, 233, 230, 231, 173, 232, 116, 214, 244, 234, 168, 80, 88, 175,]
        
    for i in range(len(codes)):
        codes[i] = int(codes[i], 2)
    
    for _ in range(108):
        a = codes[0]
        codes.pop(0)
        codes.append(0)

        if a == 0:
            continue
        
        b = galoisAntiField[a]

        for i in range(26):
            v = (genPolinom[i] + b)%255
            v = galoisField[v]
            codes[i] = codes[i]^v

    codes = codes[0:25]
    for i in range(len(codes)):
        codes[i] = bin(codes[i])[2:].zfill(8)

    return codes

def codetopng(picture):
    pic = []

    for i in picture:
        z = []
        for j in i:
            z += [j]*10
        pic += [z]*10

    palette=[(0xff,0xff,0xff), (0x00,0x00,0x00)]
    s = pic
    w = png.Writer(len(s[0]), len(s), bitdepth=1, palette=palette)
    f = open('png.png', 'wb')
    w.write(f, s)
    f.close()

def encodeToQR(tex):
    tex = list(tex)
    length = len(tex)
    modeOfEncoding = "0100"
    binstr = []
    for i in tex:
        byte = bin(ord(i))[2:].zfill(8)
        binstr.append(byte)
    binlength = bin(length)[2:].zfill(8)
    binstr.insert(0, binlength)
    binstr.insert(0, modeOfEncoding)

    binstr += ["0","0","0","0"]
    binstr = "".join(binstr)

    fillers = ['11101100', '00010001']
    for i in range(108 - len(binstr)//8):
        binstr += fillers[i%2]
    binstr = [binstr[i*8: (i+1)*8] for i in range(108)]

    forerror = binstr[:]
    errorblock = RSCorrectionCode(forerror)
    binstr.extend(errorblock)

    picture = []
    for i in range(37):
        x = []
        for _ in range(37):
            x.append(2)
        picture.append(x)

    for i in range(37):
        picture[i][6] = (i+1)%2
        picture[6][i] = (i+1)%2

    x = 0
    y = 0
    for i in range(8):
        for j in range(8):
            picture[x+i][y+j] = 0
    for i in [1,2,3]:
        x = y = i-1
        for j in range(3+(3-i)*2):
            for k in range(3+(3-i)*2):
                picture[j+x][k+y] = i%2

    a = 29
    b = 0
    for i in range(8):
        for j in range(8):
            picture[a+i][b+j] = 0
    a = 30
    b = 0
    for i in [1,2,3]:
        x = a + i -1
        y = b + i - 1
        for j in range(3+(3-i)*2):
            for k in range(3+(3-i)*2):
                picture[j+x][k+y] = i%2

    a = 0
    b = 29
    for i in range(8):
        for j in range(8):
            picture[a+i][b+j] = 0
    a = 0
    b = 30
    for i in [1,2,3]:
        x = a + i -1
        y = b + i - 1
        for j in range(3+(3-i)*2):
            for k in range(3+(3-i)*2):
                picture[j+x][k+y] = i%2

    a = 28
    b = 28
    for i in [1,2,3]:
        x = a + i -1
        y = b + i - 1
        for j in range(1+(3-i)*2):
            for k in range(1+(3-i)*2):
                picture[j+x][k+y] = i%2

    maskwithcorrection = list("111011111000100")

    picture[29][8] = 1

    i = 0
    j = 0
    while (len(maskwithcorrection) != 0):
        if picture[8][i + 21*(i//8)] != 2:
            i = i +1
        picture[8][i + 21*(i//8)] = int(maskwithcorrection[0])
        i += 1

        key = 0
        if j >= 7 :
            key = 1
        if picture[36 - (j + 21*key)][8] != 2:
            j += 1
        picture[36 - (j + 21*key)][8] = int(maskwithcorrection[0])
        j += 1

        maskwithcorrection.pop(0)

    binstr = "".join(binstr)
    binstr = list(binstr)

    count = 0
    for i in range(37):
        for j in range(37):
            if picture[i][j] == 2:
                count += 1

    for i in range(count - len(binstr)):
        binstr.append(0)

    x = 36
    y = 36
    isUpper = True

    while len(binstr) != 0:
        if y == -1:
            y = 0
            x -= 2
            isUpper = False
            continue
        if y == 37:
            y = 36
            x -= 2
            isUpper = True
            continue
        if x == 6:
            x = 5
            continue

  
        if picture[y][x] == 2:
            bit = binstr.pop(0)
            picture[y][x] = int(bit) ^ ((x + y + 1)%2)

        x -= 1
  
        if picture[y][x] == 2:
            bit = binstr.pop(0)
            picture[y][x] = int(bit) ^ ((x + y + 1)%2)

        x += 1
        if isUpper:
            y -= 1
        else:
            y += 1

    for row in picture:
        for _ in range(6):
            row.append(0)
            row.insert(0, 0)

    for i in range(6):
        picture.append([0]*49)
        
        picture.insert(0, [0]*49)

    codetopng(picture)
    
    return 0
    

def main():
    intra = input("Please type text: ")

    encodeToQR(intra)

main()