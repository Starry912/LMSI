

unit,seq 
def  findSNP(unit,seq):
	start=seq.find(unit)
	for i in range(start, len(seq)-start, len(unit)):
    	if seq[i:i + len(unit)] != unit:
    		tem=seq[i:i + len(unit)+1]
    		for j in range(len(unit)):
    			if tem[j] !=unit[j]:
    				print tem,tem[j],i
    				break
    		break


    	


