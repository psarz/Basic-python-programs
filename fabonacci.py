#this program is made to print fabonacci series

while True:
       print("Enter x for exit.")
       terms = raw_input("upto how many terms? ")
       if terms == 'x' :
              break
       else:
              term = int(terms)
              a = 0
              b = 1
              count = 2
              if term <=0:
                      print("print a positive number")
              elif term == 1:
                     print(a)
              else:
                     print(a)
                     while count < term:
                             c = a + b
                             print(c)
                             a = b 
                             b = c
                             count = count +1
              print("\n")
