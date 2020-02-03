class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        maxi = 0

        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                #We use absolute function in python to get the modulus of the                    thing we need
                abso = abs(self.__elements[i] - self.__elements[j])
                if abso > maxi:
                    maxi = abso

        self.maximumDifference = maxi

    # Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)