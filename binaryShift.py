#Binary left shift and Binary right shift
#The shift  operators in python are a pair of digraphs << and >>, clearly suggesting in which direction the shift will act 
#
var = 17
#varRight will move up to one value so the one will become 2 and divide var by 2
varRight = var >> 1 #Shifting to the right by one bit is the same as interger division by two.
#varRight will 2 numbers up so two will turn to four and will multiply var by 4 which will be 17
varLeft = var << 2 # Shifting to the left by two bits is the same as interger multiplication by four. 

print(var, varLeft, varRight) #(17, 68, 8)
