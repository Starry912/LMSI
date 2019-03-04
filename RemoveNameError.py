#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''#Remove reads that are not paired
#Input file should be sorted before running this script
import string
import linecache
import sys
Input = r'/home/xjd/Public/1000genomes_2/HG00513/HG00513.chrom11.sorted.sam'
OutPath = r'/home/xjd/Public/1000genomes_2/HG00513/HG00513.chrom11.sorted_NoNameError_1.sam'
lines = linecache.getlines(Input)
print r'Read Finished'
DataLength = len(lines)
print DataLength
LineNum = 0
print lines[0]
name = (lines[0].strip().split('\t'))[0]
LineNum += 1
while(LineNum < DataLength):
    TempName = lines[LineNum].strip().split('\t')[0]
    if name != TempName:
        lines[LineNum-1]=""
        name = TempName
        LineNum += 1
    else:
        try:
            name = lines[LineNum+1].strip().split('\t')[0]
        except IndexError:
            break
        LineNum += 2
    if LineNum % 1000 == 0:
        print 'Processing:'+str(LineNum) + '/' + str(DataLength) + "\r"
if LineNum % 2 ==1:
    lines[LineNum-1]=""
    lines[LineNum-2]=""
print 
output = open(OutPath, 'w')
for l in lines:
    if l:
        output.write(l)
output.close()
print r'Fin'
'''

#Remove reads that are not paired
#Input file should be sorted before running this script
import string
import linecache
import sys
Input = r'/home/xjd/Public/1000genomes_2/NA19240/NA19240.chrom20.sort.sam'
OutPath = r'/home/xjd/Public/1000genomes_2/NA19240/NA19240.chrom20.sort_NoNameError.sam'
lines = linecache.getlines(Input)
print r'Read Finished'
DataLength = len(lines)
print DataLength
LineNum = 0
print lines[0]
relines = []
name = (lines[0].strip().split('\t'))[0]
while(LineNum < DataLength-1):
    NextNum = LineNum + 1
    TempName = lines[NextNum].strip().split('\t')[0]
    if name == TempName:
        relines.append(lines[LineNum])
        relines.append(lines[NextNum])
        while NextNum < DataLength-1 and lines[NextNum].strip().split('\t')[0] == lines[LineNum].strip().split('\t')[0] :
            NextNum+=1
        LineNum = NextNum
	try:
            name = lines[LineNum].strip().split('\t')[0]
	except IndexError:
	    print "list out of index1"
    else:
        LineNum +=1
	try:
            name = lines[LineNum].strip().split('\t')[0]
	except IndexError:
	    print "list out of index2"
    if LineNum % 1000 == 0:
        print 'Processing:'+str(LineNum) + '/' + str(DataLength) + "\r"
output = open(OutPath, 'w')
newlength = len(relines)
print newlength
if newlength %2==0:
    for l in relines:
        if l:
            output.write(l)
    output.close()
else:
    for l in relines[:-2]:
        if l:
            output.write(l)
    output.close()
print r'Fin'
