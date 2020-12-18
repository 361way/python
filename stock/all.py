#!/usr/bin/env python
# coding=utf-8
#
import urllib2,re



#get gg money go to 
zjgg = []
html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._AB&sty=DCFFMBFMS&st=(BalFlowMain)&sr=-1&p=1&ps=160&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f')
for line in  re.split('","',html.read()):
    line = line.strip('"')
    zjgg.append(line.split(",")[1])

#print zjgg


# get 概念

gngg = []
html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._BKGN&sty=DCFFMBFMS&st=(ChangePercent)&sr=-1&p=1&ps=5&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f')
for line in  re.split('","',html.read()):
    line = line.strip('"')
    #print line
    #print [line.split(",")[i] for i in (1, 2)]
    #print line.split(",")[1]
    value = line.split(",")
    #print value[1],value[2]
    gnurl = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C.' + value[1] + '1&sty=DCFFMBFMS&st=(BalFlowMain)&sr=-1&p=1&ps=&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f'
    for line in re.split('","',urllib2.urlopen(gnurl).read()):
        line = line.strip('"')
        ggvalue = line.split(",")
        
        #print ggvalue[1],ggvalue[2],value[2]
        #gngg.append([ggvalue[1],ggvalue[2],value[2]])

        if  ggvalue[1]  in zjgg:
            gngg.append(ggvalue[1])

#print gngg

# get 行业
hygg = []

html = urllib2.urlopen(r'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._BKHY&sty=DCFFMBFMS&st=(ChangePercent)&sr=-1&p=1&ps=5&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f')
for line in  re.split('","',html.read()):
    line = line.strip('"')
    #print line
    #print [line.split(",")[i] for i in (1, 2)]
    #print line.split(",")[1]
    value = line.split(",")
    #print value[1],value[2]
    gnurl = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C.' + value[1] + '1&sty=DCFFMBFMS&st=(BalFlowMain)&sr=-1&p=1&ps=&cb=&js=(x)&token=0b9469e9fdfd123fcec4532ae1c20f4f'
    for line in re.split('","',urllib2.urlopen(gnurl).read()):
        line = line.strip('"')
        ggvalue = line.split(",")

        if  ggvalue[1]  in zjgg:
            #print ggvalue[1],ggvalue[2],value[2]
            if  ggvalue[1]  in   gngg:
                print ggvalue[1],ggvalue[2],value[2]

