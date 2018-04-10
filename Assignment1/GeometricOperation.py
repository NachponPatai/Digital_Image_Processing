import math
def getHistogram(imginput):
    with open(imginput,'rb') as f:
        #Getype of File 
        data = f.readline()
        typeImg = data.decode('utf-8')
        #print(typeImg)

        # Keep Row Column from Line 2 
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

        # Keep Row Column from Line 2 
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
    return dataPic


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


def PointGrid():
    pointgrid = [[0,0],[15,0],[31,0],[47,0],[63,0],[79,0],[95,0],[111,0],[127,0],[143,0],[159,0],[175,0],[191,0],[207,0],[223,0],[239,0],[255,0],
                [0,15],[15,15],[31,15],[47,15],[63,15],[79,15],[95,15],[111,15],[127,15],[143,15],[159,15],[175,15],[191,15],[207,15],[223,15],[239,15],[255,15],
                [0,31],[15,31],[31,31],[47,31],[63,31],[79,31],[95,31],[111,31],[127,31],[143,31],[159,31],[175,31],[191,31],[207,31],[223,31],[239,31],[255,31],
                [0,47],[15,47],[31,47],[47,47],[63,47],[79,47],[95,47],[111,47],[127,47],[143,47],[159,47],[175,47],[191,47],[207,47],[223,47],[239,47],[255,47],
                [0,63],[15,63],[31,63],[47,63],[63,63],[79,63],[95,63],[111,63],[127,63],[143,63],[159,63],[175,63],[191,63],[207,63],[223,63],[239,63],[255,63],
                [0,79],[15,79],[31,79],[47,79],[63,79],[79,79],[95,79],[111,79],[127,79],[143,79],[159,79],[175,79],[191,79],[207,79],[223,79],[239,79],[255,79],
                [0,95],[15,95],[31,95],[47,95],[63,95],[79,95],[95,95],[111,95],[127,95],[143,95],[159,95],[175,95],[191,95],[207,95],[223,95],[239,95],[255,95],
                [0,111],[15,111],[31,111],[47,111],[63,111],[79,111],[95,111],[111,111],[127,111],[143,111],[159,111],[175,111],[191,111],[207,111],[223,111],[239,111],[255,111],
                [0,127],[15,127],[31,127],[47,127],[63,127],[79,127],[95,127],[111,127],[127,127],[143,127],[159,127],[175,127],[191,127],[207,127],[223,127],[239,127],[255,127],
                [0,143],[15,143],[31,143],[47,143],[63,143],[79,143],[95,143],[111,143],[127,143],[143,143],[159,143],[175,143],[191,143],[207,143],[223,143],[239,143],[255,143],
                [0,159],[15,159],[31,159],[47,159],[63,159],[79,159],[95,159],[111,159],[127,159],[143,159],[159,159],[175,159],[191,159],[207,159],[223,159],[239,159],[255,159],
                [0,175],[15,175],[31,175],[47,175],[63,175],[79,175],[95,175],[111,175],[127,175],[143,175],[159,175],[175,175],[191,175],[207,175],[223,175],[239,175],[255,175],
                [0,191],[15,191],[31,191],[47,191],[63,191],[79,191],[95,191],[111,191],[127,191],[143,191],[159,191],[175,191],[191,191],[207,191],[223,191],[239,191],[255,191],
                [0,207],[15,207],[31,207],[47,207],[63,207],[79,207],[95,207],[111,207],[127,207],[143,207],[159,207],[175,207],[191,207],[207,207],[223,207],[239,207],[255,207],
                [0,223],[15,223],[31,223],[47,223],[63,223],[79,223],[95,223],[111,223],[127,223],[143,223],[159,223],[175,223],[191,223],[207,223],[223,223],[239,223],[255,223],
                [0,239],[15,239],[31,239],[47,239],[63,239],[79,239],[95,239],[111,239],[127,239],[143,239],[159,239],[175,239],[191,239],[207,239],[223,239],[239,239],[255,239],
                [0,255],[15,255],[31,255],[47,255],[63,255],[79,255],[95,255],[111,255],[127,255],[143,255],[159,255],[175,255],[191,255],[207,255],[223,255],[239,255],[255,255]]
    return pointgrid


def PointDistGrid():                                                                            
    pointdistgrid = [[0, 0],[16, 0],[32, 0],[48, 0],[64, 0],[80, 0],[96, 0],[112, 0],[128, 0],[144, 0],[160, 0],[176, 0],[192, 0],[208, 0],[224, 0],[240, 0],[255, 0],
		            [0, 16],[16, 16],[32, 16],[48, 16],[64, 16],[80, 16],[97, 16],[115, 18],[130, 18],[146, 18],[161, 18],[176, 16],[192, 16],[208, 16],[224, 16],[240, 16],[255, 16],
		            [0, 32],[16, 32],[32, 32],[48, 32],[66, 33],[85, 35],[105, 38],[120, 40],[136, 42],[150, 43],[164, 42],[177, 38],[193, 34],[208, 32],[225, 32],[240, 32],[255, 32],
		            [0, 48],[16, 48],[32, 48],[51, 49],[71, 50],[93, 53],[112, 57],[128, 60],[141, 63],[155, 65],[165, 65],[178, 62],[192, 56],[207, 50],[224, 47],[240, 48],[255, 48],
		            [0, 64],[16, 64],[34, 64],[57, 66],[80, 66],[100, 67],[118, 72],[132, 77],[144, 80],[155, 84],[167, 85],[178, 83],[190, 80],[205, 74],[223, 66],[240, 64],[255, 64],
		            [0, 80],[16, 80],[38, 78],[62, 77],[84, 77],[103, 81],[119, 84],[132, 89],[144, 95],[155, 100],[165, 103],[177, 103],[188, 100],[203, 94],[221, 85],[239, 80],[255, 80],
		            [0, 96],[18, 95],[41, 92],[65, 90],[86, 89],[103, 91],[118, 95],[131, 102],[142, 109],[151, 114],[161, 117],[172, 119],[184, 117],[200, 112],[218, 104],[238, 97],[255, 96],
		            [0, 112],[18, 110],[42, 106],[65, 103],[84, 101],[100, 102],[114, 105],[127, 112],[136, 119],[145, 126],[154, 130],[167, 132],[180, 132],[196, 128],[215, 122],[238, 114],[255, 112],
		            [0, 128],[19, 125],[43, 119],[64, 114],[82, 111],[96, 111],[110, 114],[121, 120],[130, 128],[138, 135],[149, 140],[161, 143],[176, 143],[193, 141],[213, 136],[238, 130],[255, 128],
		            [0, 144],[19, 141],[41, 135],[61, 128],[77, 124],[92, 123],[103, 124],[112, 130],[122, 136],[133, 141],[142, 150],[156, 153],[172, 155],[190, 154],[213, 150],[236, 145],[255, 144],
		            [0, 160],[18, 158],[39, 151],[57, 143],[73, 139],[86, 137],[97, 137],[107, 141],[116, 147],[127, 154],[138, 160],[153, 164],[171, 166],[190, 165],[214, 163],[238, 161],[255, 160],
		            [0, 176],[16, 176],[36, 170],[54, 161],[69, 155],[82, 152],[93, 152],[103, 155],[113, 160],[125, 165],[138, 171],[153, 175],[172, 177],[193, 178],[218, 177],[239, 175],[255, 176],
		            [0, 192],[16, 192],[34, 189],[52, 182],[66, 175],[79, 170],[90, 169],[101, 172],[112, 174],[125, 179],[139, 183],[156, 187],[175, 189],[199, 191],[221, 191],[240, 192],[255, 192],
		            [0, 208],[16, 208],[32, 208],[50, 204],[65, 198],[78, 192],[90, 190],[102, 189],[114, 192],[128, 195],[143, 198],[161, 202],[182, 205],[204, 206],[224, 208],[240, 208],[255, 208],
		            [0, 224],[16, 224],[32, 224],[48, 223],[64, 220],[79, 215],[93, 213],[106, 212],[120, 212],[135, 214],[151, 217],[170, 220],[189, 222],[208, 224],[224, 224],[240, 224],[255, 224],
		            [0, 240],[16, 240],[32, 240],[48, 240],[64, 240],[80, 238],[96, 239],[111, 235],[125, 235],[142, 236],[159, 237],[175, 238],[192, 240],[208, 240],[224, 240],[240, 240],[255, 240],
		            [0, 255],[15, 255],[32, 255],[48, 255],[64, 255],[80, 255],[96, 255],[112, 255],[128, 255],[144, 255],[160, 255],[176, 255],[192, 255],[208, 255],[224, 255],[240, 255],[255, 255]]

    return pointdistgrid


def controlGrid(grid,distgrid,image):
    gx = [None]*4
    gy = [None]*4
    dgx = [None]*4
    dgy = [None]*4
    # matA = [[0 for x in range(len(eqgx))] for y in range(len(eqgx[0]))]
    pic = [[0 for x in range(len(image))] for y in range(len(image[0]))]
    for i in range (16):
        for j in range (16):
            row = 17 * i
            gx[0] = grid[row+j][0]
            gx[1] = grid[row+j+1][0]
            gx[2] = grid[row+17+j][0]
            gx[3] = grid[row+17+j+1][0]

            gy[0] = grid[row+j][1]
            gy[1] = grid[row+j+1][1]
            gy[2] = grid[row+17+j][1]
            gy[3] = grid[row+17+j+1][1]

            dgx[0] = distgrid[row+j][0]
            dgx[1] = distgrid[row+j+1][0]
            dgx[2] = distgrid[row+17+j][0]
            dgx[3] = distgrid[row+17+j+1][0]
            bX = [dgx[0],dgx[1],dgx[2],dgx[3]]

            dgy[0] = distgrid[row+j][1]
            dgy[1] = distgrid[row+j+1][1]
            dgy[2] = distgrid[row+17+j][1]
            dgy[3] = distgrid[row+17+j+1][1]
            bY = [dgy[0],dgy[1],dgy[2],dgy[3]]

            matA = [[gx[0],gy[0],gx[0]*gy[0],1],
                    [gx[1],gy[1],gx[1]*gy[1],1],
                    [gx[2],gy[2],gx[2]*gy[2],1],
                    [gx[3],gy[3],gx[3]*gy[3],1]]
    
            ans = solveDet44(matA)
            Ainv = inversemat(matA,ans)

            wx = getW(Ainv,bX)
            wy = getW(Ainv,bY)

            for y in range(gy[0],gy[2]):
                for x in range(gx[0],gx[1]):
                    x_ = int(round(wx[0]*x + wx[1]*y + wx[2]*x*y + wx[3]))
                    y_ = int(round(wy[0]*x + wy[1]*y + wy[2]*x*y + wy[3]))
                    

                    pic[y][x] = image[y_][x_]

    return pic


             
def solveDet44(matA) :
    detA = [[matA[1][1], matA[1][2], matA[1][3]], 
            [matA[2][1], matA[2][2], matA[2][3]], 
            [matA[3][1], matA[3][2], matA[3][3]]]
    detB = [[matA[1][0], matA[1][2], matA[1][3]], 
            [matA[2][0], matA[2][2], matA[2][3]], 
            [matA[3][0], matA[3][2], matA[3][3]]]
    detC = [[matA[1][0], matA[1][1], matA[1][3]], 
            [matA[2][0], matA[2][1], matA[2][3]], 
            [matA[3][0], matA[3][1], matA[3][3]]]
    detD = [[matA[1][0], matA[1][1], matA[1][2]], 
            [matA[2][0], matA[2][1], matA[2][2]], 
            [matA[3][0], matA[3][1], matA[3][2]]]
    deta = 0
    detb = 0
    detc = 0
    detd = 0

    if(matA[0][0]) :
        deta = matA[0][0]*solve(detA)
    if(matA[0][1]) :
        detb = matA[0][1]*solve(detB)
    if(matA[0][2]) :
        detc = matA[0][2]*solve(detC)
    if(matA[0][3]) :
        detd = matA[0][3]*solve(detD)

    Det = deta - detb + detc - detd
    return  Det
   

def solve(matA):
    n=len(matA)
    if (n>2):
        i=1
        t=0
        sum=0
        while t<=n-1:
            d={}
            t1=1
            while t1<=n-1:
                m=0
                d[t1]=[]
                while m<=n-1:
                    if (m==t):
                        u=0
                    else:
                        d[t1].append(matA[t1][m])
                    m+=1
                t1+=1
            A1=[d[x] for x in d]
            sum=sum+i*(matA[0][t])*(solve(A1))
            i=i*(-1)
            t+=1
        return sum
    else:
        return (matA[0][0]*matA[1][1]-matA[0][1]*matA[1][0])


def inversemat(A,detA):
    b = [[0 for i in range(4)] for j in range(4)]
    Ainv = [[0 for i in range(4)] for j in range(4)]
    b[0][0] = A[1][1]*A[2][2]*A[3][3] + A[1][2]*A[2][3]*A[3][1] + A[1][3]*A[2][1]*A[3][2] - A[1][1]*A[2][3]*A[3][2] - A[1][2]*A[2][1]*A[3][3] - A[1][3]*A[2][2]*A[3][1]
    b[0][1] = A[0][1]*A[2][3]*A[3][2] + A[0][2]*A[2][1]*A[3][3] + A[0][3]*A[2][2]*A[3][1] - A[0][1]*A[2][2]*A[3][3] - A[0][2]*A[2][3]*A[3][1] - A[0][3]*A[2][1]*A[3][2]
    b[0][2] = A[0][1]*A[1][2]*A[3][3] + A[0][2]*A[1][3]*A[3][1] + A[0][3]*A[1][1]*A[3][2] - A[0][1]*A[1][3]*A[3][2] - A[0][2]*A[1][1]*A[3][3] - A[0][3]*A[1][2]*A[3][1]
    b[0][3] = A[0][1]*A[1][3]*A[2][2] + A[0][2]*A[1][1]*A[2][3] + A[0][3]*A[1][2]*A[2][1] - A[0][1]*A[1][2]*A[2][3] - A[0][2]*A[1][3]*A[2][1] - A[0][3]*A[1][1]*A[2][2]

    b[1][0] = A[1][0]*A[2][3]*A[3][2] + A[1][2]*A[2][0]*A[3][3] + A[1][3]*A[2][2]*A[3][0] - A[1][0]*A[2][2]*A[3][3] - A[1][2]*A[2][3]*A[3][0] - A[1][3]*A[2][0]*A[3][2]
    b[1][1] = A[0][0]*A[2][2]*A[3][3] + A[0][2]*A[2][3]*A[3][0] + A[0][3]*A[2][0]*A[3][2] - A[0][0]*A[2][3]*A[3][2] - A[0][2]*A[2][0]*A[3][3] - A[0][3]*A[2][2]*A[3][0]
    b[1][2] = A[0][0]*A[1][3]*A[3][2] + A[0][2]*A[1][0]*A[3][3] + A[0][3]*A[1][2]*A[3][0] - A[0][0]*A[1][2]*A[3][3] - A[0][2]*A[1][3]*A[3][0] - A[0][3]*A[1][0]*A[3][2]
    b[1][3] = A[0][0]*A[1][2]*A[2][3] + A[0][2]*A[1][3]*A[2][0] + A[0][3]*A[1][0]*A[2][2] - A[0][0]*A[1][3]*A[2][2] - A[0][2]*A[1][0]*A[2][3] - A[0][3]*A[1][2]*A[2][0]

    b[2][0] = A[1][0]*A[2][1]*A[3][3] + A[1][1]*A[2][3]*A[3][0] + A[1][3]*A[2][0]*A[3][1] - A[1][0]*A[2][3]*A[3][1] - A[1][1]*A[2][0]*A[3][3] - A[1][3]*A[2][1]*A[3][0]
    b[2][1] = A[0][0]*A[2][3]*A[3][1] + A[0][1]*A[2][0]*A[3][3] + A[0][3]*A[2][1]*A[3][0] - A[0][0]*A[2][1]*A[3][3] - A[0][1]*A[2][3]*A[3][0] - A[0][3]*A[2][0]*A[3][1]
    b[2][2] = A[0][0]*A[1][1]*A[3][3] + A[0][1]*A[1][3]*A[3][0] + A[0][3]*A[1][0]*A[3][1] - A[0][0]*A[1][3]*A[3][1] - A[0][1]*A[1][0]*A[3][3] - A[0][3]*A[1][1]*A[3][0]
    b[2][3] = A[0][0]*A[1][3]*A[2][1] + A[0][1]*A[1][0]*A[2][3] + A[0][3]*A[1][1]*A[2][0] - A[0][0]*A[1][1]*A[2][3] - A[0][1]*A[1][3]*A[2][0] - A[0][3]*A[1][0]*A[2][1]

    b[3][0] = A[1][0]*A[2][2]*A[3][1] + A[1][1]*A[2][0]*A[3][2] + A[1][2]*A[2][1]*A[3][0] - A[1][0]*A[2][1]*A[3][2] - A[1][1]*A[2][2]*A[3][0] - A[1][2]*A[2][0]*A[3][1]
    b[3][1] = A[0][0]*A[2][1]*A[3][2] + A[0][1]*A[2][2]*A[3][0] + A[0][2]*A[2][0]*A[3][1] - A[0][0]*A[2][2]*A[3][1] - A[0][1]*A[2][0]*A[3][2] - A[0][2]*A[2][1]*A[3][0]
    b[3][2] = A[0][0]*A[1][2]*A[3][1] + A[0][1]*A[1][0]*A[3][2] + A[0][2]*A[1][1]*A[3][0] - A[0][0]*A[1][1]*A[3][2] - A[0][1]*A[1][2]*A[3][0] - A[0][2]*A[1][0]*A[3][1]
    b[3][3] = A[0][0]*A[1][1]*A[2][2] + A[0][1]*A[1][2]*A[2][0] + A[0][2]*A[1][0]*A[2][1] - A[0][0]*A[1][2]*A[2][1] - A[0][1]*A[1][0]*A[2][2] - A[0][2]*A[1][1]*A[2][0]

    for i in range (4):
        for j in range (4):
            Ainv[i][j] = b[i][j]/detA

    return Ainv


def getW(inverseMat,MatA):
    w = []
    for i in range (4) :
        ans = 0
        for j in range (4) :
            ans = ans + ( MatA[j] * inverseMat[i][j] )
        w.append(ans)
    return w


if __name__=='__main__':
    grid = PointGrid()
    distgrid = PointDistGrid()
    distlenna = getPicture('images/distlenna.pgm')
    distortgrid = getPicture('images/distgrid.pgm')
    lenna = controlGrid(grid,distgrid,distlenna)
    regrid = controlGrid(grid,distgrid,distortgrid) 
    createPGM(lenna,'images/lenna.pgm')
    createPGM(regrid,'images/regrid.pgm')

