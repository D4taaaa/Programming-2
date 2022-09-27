# Dāvis Karpovskis(pašlaik pārdomā izvēli iet tālāk programmēšanā)


class Rekinatajs:
    def __init__(self):
        pass

    def factorial(self, num):
        i = num
        AHHh = 1
        while i != 0:
            AHHh = AHHh * i
            i = i - 1
        return AHHh

    def Sum(self, num):
        i = num
        AHHh = 0
        while i != 0:
            AHHh = AHHh + i
            i = i - 1
        return AHHh

    def testPrime(self, num):
        test = False
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    test = True

                    break

        if test:
            return f"{num} is not a prime number😢"
        else:
            return f"{num} is a prime number🤓"

    def TableMult(self, num):
        for i in range(1, num + 1):
            for j in range(1, num + 1):
                print(i * j, end='\t')
            print('')
        return ''  # lai neraditu None pec tabulas

    def listDiv(self, num):
        for i in range(1, num + 1):
            if num % i == 0:
                print(i)
        return ''

    def listDivPrime(self, num):
        c = 2
        while (num > 1):

            if (num % c == 0):
                print(c, end=" ")
                num = num / c
            else:
                c = c + 1
        return ''



f = Rekinatajs()
print(f.listDivPrime(315))
