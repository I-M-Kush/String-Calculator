class StringCalculator:
    def add(self,Number):
        sum=0
        for x in Number:
            if x == 0:
                sum=0
            else:
                sum=sum+int(x)
        print(sum)
            


number=str(input("Enter number sepreted by Commm :"))
Numberlist=number.split(",")
Sc=StringCalculator()
Sc.add(Numberlist)
 