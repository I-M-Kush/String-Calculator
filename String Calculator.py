class StringCalculator:
    def add(self,Number):
        sum=0
        for x in Number:
            if x == 0:
                sum=0
            else :
                 if x.isalpha():
                    x=x.lower()
                    sum =sum + int(str(ord(x)-96))
                 else:
                    try:
                        assert int(x) > 0
                        sum=sum+int(x)
                    except AssertionError:
                        print("Negative number not Allowed")
                        sum=x
        print(sum)
            


number=str(input("Enter number sepreted by Comma :"))
Numberlist=number.split(",")
Sc=StringCalculator()
Sc.add(Numberlist)
