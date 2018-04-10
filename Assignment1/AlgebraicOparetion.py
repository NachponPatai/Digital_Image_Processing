def getHistogram(imginput):
    with open(imginput,'rb') as f:
        #Getype of File 
        data = f.readline()
        typeImg = data.decode('utf-8')
        #print(typeImg)
        
        # Kill Line 2 
        data = f.readline()

        # Keep Row Column from Line 3 
        data = f.readline()
        sizeImg = data.decode('utf-8')
        row,column = sizeImg.split(" ")
        row = int(row)
        column = int(column)
        # print (row)
        # print (column)

        # Keep Max value of image 
        data = f.readline()
        Dmax = data.decode('utf-8')
        Dmax = int(Dmax)
        # print(Dmax)
        n = 0
        hist = [0]*(Dmax+1)
        while True:
            c = f.read(1)
            if not c:
                print ("End of file")
                break
            hist[ord(c)] += 1
            n = n + 1
        # print(n)
        # print (hist)
    return hist

def getPicture(imginput):
    with open(imginput,'rb') as f:
        #Getype of File 
        data = f.readline()
        typeImg = data.decode('utf-8')
        #print(typeImg)

        # Kill Line 2 
        data = f.readline()

        # Keep Row Column from Line 3
        data = f.readline()
        sizeImg = data.decode('utf-8')
        row,column = sizeImg.split(" ")
        row = int(row)
        column = int(column)
        #print (row)
        #print (column)

        # Keep Max value of image 
        data = f.readline()
        Dmax = data.decode('utf-8')
        # Dmax = int(Dmax)
        # print(Dmax)
        n = 0
        dataPic = [[0]*column for i in range(row)]
        for i in range(row):
            for j in range(column):
                c = f.read(1)
                dataPic[i][j] = ord(c)
                n = n + 1
        # print("dataPic",dataPic) 

    return dataPic

def excess_Green(picblue,picred,picgreen):
    numrow = len(picblue)
    numcolumn = len(picblue[0])
    excessGreen = [[0]*numcolumn for i in range(numrow)]
    for i in range(numrow):
        for j in range(numcolumn):
            pixel = 2*picgreen[i][j] - picred[i][j] - picblue[i][j]
            if(pixel < 0):
                pixel = 0
            elif (pixel > 255):
                pixel = 255

            excessGreen[i][j] = pixel

    return excessGreen

def R_diff_B(picblue,picred):
    numrow = len(picblue)
    numcolumn = len(picblue[0])
    RDiffB = [[0]*numcolumn for i in range(numrow)]
    for i in range(numrow):
        for j in range(numcolumn):
            pixel = picred[i][j] - picblue[i][j]
            if(pixel < 0):
                pixel = 0
            elif (pixel > 255):
                pixel = 255

            RDiffB[i][j] = pixel

    return RDiffB

def Intensity(picblue,picred,picgreen):
    numrow = len(picblue)
    numcolumn = len(picblue[0])
    intensity = [[0]*numcolumn for i in range(numrow)]
    for i in range(numrow):
        for j in range(numcolumn):
            pixel = (picblue[i][j]+picred[i][j]+picgreen[i][j])/3
            if(pixel < 0):
                pixel = 0
            elif (pixel > 255):
                pixel = 255

            intensity[i][j] = round(pixel-0.5)

    return intensity

def createPGM(picture,dest):
    numrow = len(picture)
    numcolumn = len(picture[0])
    file = open(dest,'w',encoding="ISO-8859-1")
    file.write("P5\r\n")
    file.write("# d:/jub/cmu/dipundergrad/testtest.pgm\r\n")
    file.write(str(numrow)+" "+str(numcolumn)+"\r\n")
    file.write("255\r\n")
    for i in range(numrow):
        for j in range(numcolumn):
            file.write((chr(picture[i][j])))
    
    file.close()



if __name__=='__main__':
    picb = getPicture('images/SanFranPeak_blue.pgm')
    picr = getPicture('images/SanFranPeak_red.pgm')
    picg = getPicture('images/SanFranPeak_green.pgm')
    excessGreen = excess_Green(picb,picr,picg)
    RDiffB = R_diff_B(picb,picr)
    Intensity = Intensity(picb,picr,picg)
    print(Intensity)
    createPGM(excessGreen,'images/excessGreen.pgm')
    createPGM(RDiffB,'images/RDiffB.pgm')
    createPGM(Intensity,'images/Intensity.pgm')