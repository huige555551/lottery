# coding: utf-8
#pip install xltd
#pip install xlwt-future
#http://bbs.aicai.com/thread-597961-1-1.html
import os
import os.path
import os
import Tkinter
import xlrd
import xlwt
import sys
import random
print 'asdf'

def getFileName():
  list = []
  for root,dirs,files in os.walk("."):
      if(root=="." ):
          for file in files:
              if(file.find("www.aicai.com")>0):
                  list.append(file)
  return list
def main():
    lists=[]
    srcNames = getFileName()
    for srcName in srcNames:
        threeAndOne = 0
        threeAndZero = 0
        oneAndZero = 0
        mainThree = 0
        firstThree =0
        secondThree =0
        mainOne = 0
        firstOne =0
        secondOne =0
        mainZero = 0
        firstZero =0
        secondZero =0
        #染色
        def isRed(num):
            if(num>=1):
                return True 
        def isBrown(num):
            if(0.96<=num and num<=0.99):
                return True
        def isWhite(num):
            if(0.9<=num and num<=0.95):
                return True
        def isBlue(num):
            if(0.86<=num and num<=0.89):
                return True
        def isGreen(num):
            if(num<=0.85):
                return True
        #求出舍弃之不符合的行后，距离赔付率最近的还有最远的两个的index
        def nearest(a,b,c,target):
            disa = abs(a-target)
            disb = abs(b-target)
            disc = abs(c-target)
            if( disa==0 and  disb==0):
                return [0,0]
            elif(disa==0 and disc==0):
                return [1,1]
            elif(disb==0 and  disc==0):
                return [3,3]
            dic = [(disa,3),(disb,1),(disc,0)]
            if(disa!=disb and disa!=disc and disb!=disc):
                dic = sorted(dic, key=lambda x:x[0],reverse=True)
                return [dic[0][1],dic[1][1]]
            if(disa==disb):
                if(disa<disc):
                    return [0,random.randrange(1,4,2)]
                elif(disa>disc):
                    threeOrOne = random.randrange(1,4,2)
                    return [threeOrOne,4-threeOrOne]
            elif(disb==disc):
                if(disb<disa):
                    return [3,random.randrange(0,2)]
                elif(disb>disa):
                    oneOrZero = random.randrange(0,2)
                    return [oneOrZero,1-oneOrZero]
            elif(disa==disc):
                if(disa<disb):
                    return [1,random.randrange(0,4,3)]
                elif(disa>disb):
                    zeroOrThree = random.randrange(0,4,3)
                    return [zeroOrThree,3-zeroOrThree]
        # data = xlrd.open_workbook("新浪爱彩(www.aicai.com)_指数数据_2016-2017_不来梅VS弗赖堡.xls")
        data = xlrd.open_workbook(srcName)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        for i in range(5 ,nrows-1 ):
              table.row_values(i)
        listItem = {}
        #从第五行开始整行读取
        for rownum in range(5,nrows-1):
            row = table.row_values(rownum)
            if row:
                app={}
                app['zhu'] =row[11]
                app['ping'] = row[12]
                app['ke'] = row[13]
                app['s'] = None
                app['c'] = None
                app['peifu'] =round( row[14]/100,4)
                #如果是出现只有蓝色，或者只有灰色那么就舍弃
                if(((isWhite(app['zhu']) or isBlue(app['zhu']))and 
                  (isWhite(app['ping'])or isBlue(app['ping']))and 
                  (isWhite(app['ke'])or isBlue(app['ke']))) or
                  ((isWhite(app['zhu']) or isBrown(app['zhu']))and 
                  (isWhite(app['ping'])or isBrown(app['ping']))and 
                  (isWhite(app['ke'])or isBrown(app['ke'])))
                  ):
                    continue
                if(app['zhu']>app['peifu']):
                    app['zhu']=app['peifu']
                if(app['ping']>app['peifu']):
                    app['ping']=app['peifu']
                if(app['ke']>app['peifu']):
                    app['ke']=app['peifu']
                appSC = nearest(app['zhu'],app['ping'],app['ke'],app['peifu'])
                
                app['s']= appSC[0]
                app['c']= appSC[1]  
                #统计结果
                if(appSC[0]==3 and appSC[1]==3):
                    mainThree+=1
                elif(appSC[0]==3 and appSC[1]==1):
                    threeAndOne+=1
                    firstThree+=1
                    secondOne+=1
                elif(appSC[0]==3 and appSC[1]==0):
                    threeAndZero+=1
                    firstThree+=1
                    secondZero+=1
                elif(appSC[0]==1 and appSC[1]==3):
                    threeAndOne+=1
                    firstOne+=1
                    secondThree+=1
                elif(appSC[0]==1 and appSC[1]==1):
                    mainOne+=1
                elif(appSC[0]==1 and appSC[1]==0):
                    oneAndZero+=1
                    firstOne+=1
                    secondZero+=1
                elif(appSC[0]==0 and appSC[1]==3):
                    threeAndZero+=1
                    firstZero+=1
                    secondThree+=1
                elif(appSC[0]==0 and appSC[1]==1):
                    oneAndZero+=1
                    firstZero+=1
                    secondOne+=1
                elif(appSC[0]==0 and appSC[1]==0):
                    mainZero+=1
                # listItem.append(app)
                # print row[0],app
        listItem['srcName']=srcName
        listItem['srcName'].decode('utf-8').encode('utf-8')
        listItem['mainThree']=mainThree
        listItem['mainOne']=mainOne
        listItem['mainZero']=mainZero
        listItem['firstThree']=firstThree
        listItem['firstOne']=firstOne
        listItem['firstZero']=firstZero
        listItem['secondThree']=secondThree
        listItem['secondOne']=secondOne
        listItem['secondZero']=secondZero
        listItem['firstThreePlusSecondThree']=firstThree+secondThree
        listItem['firstOnePlusSecondOne']=firstOne+secondOne
        listItem['firstZeroPlusSecondZero']=firstZero+secondZero
        listItem['mainThreePlusFirstThreePlusSecondThree']=mainThree+firstThree+secondThree
        listItem['mainOnePlusFirstOnePlusSecondOne']=mainOne+firstOne+secondOne
        listItem['mainZeroPlusFirstZeroPlusSecondZero']=mainZero+firstZero+secondZero
        listItem['threeAndOne']=threeAndOne
        listItem['threeAndZero']=threeAndZero
        listItem['oneAndZero']=oneAndZero
        listItem['fillThree']=secondThree
        listItem['fillOne']=secondOne
        listItem['fillZero']=secondZero
        lists.append(listItem)
        print srcName
        print "            3  1  0"
        print "胆        ",mainThree,mainOne,mainZero;
        print "首选      ",firstThree,firstOne,firstZero;
        print "次选      ",secondThree,secondOne,secondZero;
        print "首＋次    ",firstThree+secondThree,firstOne+secondOne,firstZero+secondZero;
        print "胆＋首＋次",mainThree+firstThree+secondThree,mainOne+firstOne+secondOne,mainZero+firstZero+secondZero;
        print "31:"+str(threeAndOne);
        print "30:"+str(threeAndZero);
        print "10:"+str(oneAndZero);
        print "补3:",secondThree;
        print "补1:",secondOne;
        print "补0:",secondZero;
    return lists
main()