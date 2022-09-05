class StringCalculator:
    def add(self,Number):
        sum=0
        neg=[]
        for x in Number:
            if x == 0:
                sum=0
            else :
                if x.isalpha():
                    x=x.lower()
                    sum =sum + int(str(ord(x)-96))
                else:
                    if int(x) < 1000:
                        try:
                            assert int(x) > 0
                            sum=sum+int(x)
                        except AssertionError:
                            print("Negative number not Allowed")
                            neg.append(x)
        print("Sum is :",sum)

        for i in neg:
            print("negative number is :",i)
            


number=str(input("Enter number sepreted by Comma :"))
Numberlist=number.split(",")
Sc=StringCalculator()
Sc.add(Numberlist)
 