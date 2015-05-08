import sys
import re
#this is bad because it keeps two files open for the entire running time :(
#but it doesn't use a lot of memory at runtime?
def main():
	f = open(sys.argv[1])
	o = open('result.out', 'w+')
	errors = []
	curpos = 0
	o.write('{\n  "entries": [')
	for line in f:	#lines!
		line = line.rstrip('\n') #no newlines
		ziperr = False #zip error
		phnerr = False #phn error
		k = map(str, line.split(",")) #make array from input
		
		if len(k) < 4: #badline
			errors.append(curpos) #note line no.
		
		elif len(k) == 4: #input type 1
			n = map(str,k[0].split(" ")) #will break if ex. Booker T. Washington. regex needed? names like firstname la Cruz will also break 
			fn = n[0].strip()
			ln = n[1].strip()
			cl = k[1].strip()
			if re.match("\d{5}$", k[2].strip()):
				zp = k[2].strip()
			else: #error recorded
				errors.append(curpos)
				ziperr = True 
			if re.match("\d{3}.?.\d{3}.\d{4}$",k[3].strip()):
				ph = k[3].strip().replace(" ","-")
			elif ziperr == False: #error recorded
				errors.append(curpos)
				phnerr = True
			#print ph,fn,ln,cl,zp

		elif k[4].strip().isdigit(): #input type 2
			ln = k[0].strip()
			fn = k[1].strip()
			if re.match(".?\d{3}.?.\d{3}.\d{4}$",k[2].strip()):
				ph = k[2].strip().replace("(","").replace(")","")
			else: #error recorded
				errors.append(curpos)
				phnerr = True
			cl = k[3].strip()
			if re.match("\d{5}$", k[4].strip()):
				zp = k[4][1:]
			elif phnerr == False: #error recorded
				errors.append(curpos)
				ziperr = True
			#print ph,fn,ln,cl,zp

		elif k[4].strip().isalpha(): #input type 3
			fn = k[0].strip()
			ln = k[1].strip()
			if re.match("\d{5}$", k[2].strip()):
				zp = k[2].strip()
			else: #error recorded
				errors.append(curpos)
				ziperr = True
			if re.match("\d{3}.?.\d{3}.\d{4}$",k[3].strip()):
				ph = k[3].strip().replace(" ","-")
			elif ziperr == False: #error recorded
				errors.append(curpos)
				phnerr = True
			cl = k[4].strip()	
			#print ph,fn,ln,cl,zp
		
		if len(k)>=4 and (phnerr == False and ziperr == False): #if no errors, write
			o.write('\n    {\n      "color":',)		
			o.write('"'+cl+'"')
			o.write('\n      "firstname":')
			o.write('"'+fn+'"')
			o.write('\n      "lastname":')
			o.write('"'+ln+'"')
			o.write('\n      "phonenumber":')
			o.write('"'+ph+'"')
			o.write('\n      "zipcode":')
			o.write('"'+zp+'"')
			o.write('\n    },')
		curpos+=1
	o.seek(-1,1) #remove last comma
	o.write('\n  ],')		
	o.write('\n  "errors": [')
	for i in errors: #write errors
		o.write('\n    ')
		o.write(str(i))
		o.write(',')
	o.seek(-1,1) #remove last comma
	o.write('\n  ]\n}')		
		
	f.close()
	o.close()
	print "done"
	#for i in errors:
	#	print i

if __name__ == "__main__":
  main()
