# Read input from STDIN. Print output to STDOUT
import math
def printMatrix(m):
    for r in m:
        s = ""
        for elem in r:
            s+=elem+" "
        s = s[:-1]
        print s

def getDepth(r,c):
    if(min(r,c)==0):
        return 0
    elif(min(r,c)==1):
        return 1
    return 1+getDepth(r-2,c-2)

def getTopRow(m,off,result):
    row = m[off]
    for i in xrange(off,len(row)-off,1):
        result.append(row[i])

def getRightColumn(m,off,result):
    for i in xrange(off+1,len(m)-off,1):
        row = m[i]
        result.append(row[-1-off])

def getBottomRow(m,off,result):
    if(len(m)-1-off==off):
        return
    row = m[len(m)-1-off]
    for i in xrange(len(row)-2-off,off-1,-1):
        result.append(row[i])

def getLeftColumn(m,off,result):
    for i in xrange(len(m)-2-off,off,-1):
        result.append(m[i][off])
        
def getMatrixLayers(m,off=0,result=[]):
    getTopRow(m,off,result)
    #print "After topRow:",result
    getRightColumn(m,off,result)
    #print "After rightColumn:",result
    getBottomRow(m,off,result)
    #print "After BottomRow:",result
    getLeftColumn(m,off,result)
    #print "After LeftColumn:",result

def rotateLayer(layer, rotation):
    off = rotation%len(layer)
    layer = layer[off:] + layer[:off]
    return layer

def createLayers(m,r,c,rotation):
    d = getDepth(r,c)
    layers = []
    for i in xrange(d):
        layers.append([])
        getMatrixLayers(m,i,layers[i])
        #print "layer:",i,layers[i]
        layers[i] = rotateLayer(layers[i],rotation)
        #print "after",rotation,"rotations"
        #print layers[i]
    return layers

    
def getDictFromLayer(layer,r,c,off):
    w = c - off*2
    h = int(abs(math.ceil((len(layer)-w*2)/2.0)))
    d = {}
    d["top"] = layer[:w]
    d["right"] = layer[w:w+h]
    d["bottom"] = layer[w+h:w*2+h][::-1]
    d["left"] = layer[w*2+h:][::-1]
    return d
def printLayerDicts(layerDict):
    for i in xrange(len(layerDict)):
        d = layerDict[i]
        print "for layer", i
        for keys in d:
            print keys, " = ", d[keys]
        print ""
def main(m,r,c,rotation):
    layers = createLayers(m,r,c,rotation)
    layerDicts = []
    for i in xrange(len(layers)):
        layerDicts.append(getDictFromLayer(layers[i],r,c,i))
    #printLayerDicts(layerDicts)
    
    rm = []
    ld = layerDicts[::-1]
    for d in ld:
        #print "start"
        #print "dleft",d["left"]
        if(d["left"]!=[]):
            #print "entered"
            l = d["left"]
            r = d["right"]
            for i in xrange(len(rm)):
                #print "in for"
                lt = [l[i]]
                rt = [r[i]]
                #print "***"
                #print lt,rt,rm[i]
                rm[i] = lt+rm[i]+rt
                #print len(rm)
                #print rm
            if(len(rm)==0):
                for k in xrange(len(l)):
                    rm.append([l[k],r[k]])
        rm[0:0]=[d["top"]]
        if(d["bottom"]!=[]):
            rm.append(d["bottom"])
    printMatrix(rm)
    
rows,columns,rotations = raw_input().split(" ")
rows = int(rows)
columns = int(columns)
rotations = int(rotations)
matrix = []
for i in xrange(int(rows)):
    matrix.append(raw_input().split(" "))

#getMatrixLayers(matrix,rows,columns,2,1)
#createLayers(matrix,rows,columns,rotations)
main(matrix,rows,columns,rotations)