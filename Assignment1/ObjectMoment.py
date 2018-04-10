import matplotlib.pyplot as plt 

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
        print(n)
        print (hist)
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

def PossitionOfHighValue(histogram):
    possition = [0]*5
    j = 0 
    for i in range(len(histogram)):
        if i != 255:
            if histogram[i] > 500:
                possition[j] = i
                j += 1
    return possition

def binImg(pic,value):
    binPic = [[0]*len(pic[0]) for i in range(len(pic))]
    for i in range(len(pic)):
        for j in range(len(pic[0])):
            if(pic[i][j] == value):
                binPic[i][j] = 1
            else: binPic[i][j] = 0
    
    return binPic

def pq_Moment(binPic,p,q):
    moment = 0
    for i in range(len(binPic)):
        for j in range(len(binPic[0])):
            moment += (j**p)*(i**q)*binPic[i][j]
    return moment 

def central_Moment(binPic,p,q,mx,my):
    Cmoment = 0
    for i in range(len(binPic)):
        for j in range(len(binPic[0])):
            Cmoment += ((j-mx)**p)*((i-my)**q)*binPic[i][j]
    return Cmoment        

def normalize_Moment(binPic,p,q,mx,my):
    Up = central_Moment(binPic,p,q,mx,my)
    U0 = central_Moment(binPic,0,0,mx,my)
    Np = Up/(U0**(((p+q)/2)+1))
    return Np

def quantity(n20,n02):
    quan = n20+n02
    return quan

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
            file.write(str(chr(picture[i][j])))
    
    file.close()

def plot_graph(histogram):
    y = histogram
    plt.plot(y)
    plt.xlabel("Range of Color")
    plt.ylabel("Pixel")
    plt.title("Histogram")
    

if __name__=='__main__':
    hist = getHistogram('images/scaled_shapes.pgm')
    plot_graph(hist)
    plt.show()
    pic = getPicture('images/scaled_shapes.pgm')
    valueImg = PossitionOfHighValue(hist)
    print(pic)
    for i in range(len(valueImg)):
        Pic01 = binImg(pic,valueImg[i])
        createPGM(Pic01,'images/scaled_shape['+str(i)+'].pgm')
        m00 = pq_Moment(Pic01,0,0)
        m01 = pq_Moment(Pic01,0,1)
        m10 = pq_Moment(Pic01,1,0)
        mx = m10/m00
        my = m01/m00
        u20 = central_Moment(Pic01,2,0,mx,my)
        u02 = central_Moment(Pic01,0,2,mx,my)
        n20 = normalize_Moment(Pic01,2,0,mx,my)
        n02 = normalize_Moment(Pic01,0,2,mx,my)
        quan = quantity(n20,n02)
        print(valueImg[i])
        print("Center Of Mass x = ", mx , " y = ",my)
        print("Center Of Moment u20 = ", u20 , " u02 = ",u02)
        print("Quantity", i+1 ," = ",quan)