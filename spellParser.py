def main():
	f = open('./roleplaySpells.txt', 'r')
	o = open('./roleplaySpells.csv', 'w')
	fileText = ""
	out = []
	for line in f:
		
		fileText+=line
	spells = fileText.split("\r\n\r\n")
	
	for spell in spells:
		
		spellLines = spell.split("\r\n")
		#lore,spellname, cost\rank, castingNo, reagents, cast time, wp cost, damage, range,aoe, duriation, description, MP
		outLine = ["","","","","","","","","","","","",""]
		for line in spellLines:
			if (len(spellLines)==1):
				if len(line)>1:
					#this is a name of a lore, add it
					outLine[0]=line
					
			else:
				print line
				outLine[1]=spellLines[0]
				if(line.startswith("Cost per Rank:")):
					outLine[2]=line.split(":")[1].strip()
				if(line.startswith("Casting Number:")):
					outLine[3]=line.split(":")[1].strip()								
				if(line.startswith("Reagents:")):
					outLine[4]=line.split(":")[1].strip()				
				if(line.startswith("Casting Time:")):
					outLine[5]=line.split(":")[1].strip()									
				if(line.startswith("WP Cost:")):
					outLine[6]=line.split(":")[1].strip()									
				if(line.startswith("Damage:")):
					outLine[7]=line.split(":")[1].strip()					
				if(line.startswith("Range:")):
					outLine[8]=line.split(":")[1].strip()					
				if(line.startswith("Area of Effect:")):
					outLine[9]=line.split(":")[1].strip()					
				if(line.startswith("Duration:")):
					outLine[10]=line.split(":")[1].strip()																			
				if(line.startswith("Effects:")):
					outLine[11]=line.split(":")[1].strip()					
				if(line.startswith("Minimum MP req:")):
					outLine[12]=line.split(":")[1].strip()
		out.append(outLine)
	
	print out
	
	for x in out:
		s=x[0]+","+x[1]+","+x[2]+","+x[3]+","+x[4]+","+x[5]+","+x[6]+","+x[7]+","+x[8]+","+x[9]+","+x[10]+","+x[11]+","+x[12]+"\r\n"
		print x
		print s
		o.write(s)
		
	
		

if __name__ == "__main__":
	main();
