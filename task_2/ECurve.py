from ECPoint import ECPoint
import decimal
from ModArith import ModArith

class ECurve(object):
    """
        ECurve implenents elliptic curves of type:
        y^2 = x^3 + a*x + b
    """

    a = None
    b = None
    mod = None
    basePoint = None

    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b

    def setMod(self, mod):

        """Prime number greater than 3"""

        self.mod = mod


    def BasePointGSet(self, x, y):
        self.basePoint = ECPoint(x, y)


    def BasePointGGet(self) -> ECPoint:
        return self.basePoint


    def ECPointGen(self, x, y) -> ECPoint:
        return ECPoint(x, y)


    def IsOnCurveCheck(self, a: ECPoint) -> bool:


        # left = ( (a.x ** 3) + (self.a * a.x) + self.b - (a.y ** 2) )

        modular = ModArith()
        left = modular.get_x_power_optimal(a.x, 3, self.mod)
        A = self.a * a.x
        if(A != 0):
            left += modular.get_x(A, self.mod)
        left += modular.get_x(self.b, self.mod)
        left -= modular.get_x_power_optimal(a.y, 2, self.mod)

        cond =  left % self.mod

        return not bool(cond)


    def AddECPoints(self, a: ECPoint, b: ECPoint, skipCheck = False) -> ECPoint:

        # Check for point to be on the curve
        cond_a = True
        cond_b = True
        if(skipCheck == False):
            cond_a = self.IsOnCurveCheck(a)
            cond_b = self.IsOnCurveCheck(b)

        if( (cond_a and cond_b) or skipCheck == True):

            lmbd = (b.y - a.y) / (b.x - a.x)
            x = (lmbd * lmbd) - a.x - b.x
            y = lmbd * (a.x - x) - a.y

            return self.ECPointGen(x, y)
        else:
            raise ValueError("Points are not on the same curve")


    def AddECPointsBinary(self, a: ECPoint, b: ECPoint) -> ECPoint:

        modular = ModArith()

        if(a.x == b.x and a.y == b.y):

            beta = (3 * a.x * a.x + self.a) * modular.get_x_bin(2 * a.y, self.mod)

        else:

            beta = (b.y - a.y) * modular.get_x_bin((b.x - a.x), self.mod)

        x = beta * beta - a.x - b.x
        y = beta * (a.x - x) - a.y

        x = x % self.mod
        y = y % self.mod

        while(x < 0):
            x = x + self.mod

        while(y < 0):
            y = y + self.mod

        return self.ECPointGen(x, y)



    def DoubleECPoints(self, a: ECPoint, skipCheck = False) -> ECPoint:

        # Check for point to be on the curve
        cond_a = True
        if(skipCheck == False):
            cond_a = self.IsOnCurveCheck(a)

        if(cond_a or skipCheck == True):

            lmbd = ( (3 * (a.x * a.x) ) + self.a ) / (2 * a.y)
            x = (lmbd * lmbd) - (2 * a.x)
            y = lmbd * (a.x - x) - a.y

            return self.ECPointGen(x, y)
        else:
            raise ValueError("Point is not on the curve")


    def ScalarMult(self, a: ECPoint, k) -> ECPoint:

        if(k == 0):
            raise ValueError("Multiplication by zero")

        if(k == 1):
            return a

        if(k % 2 == 1):
            return self.AddECPoints(a, self.ScalarMult(a, k - 1), True)
        else:
            return self.ScalarMult(self.DoubleECPoints(a, True), k / 2 )


    def ScalarMultBinary(self, a: ECPoint, k) -> ECPoint:

        point = self.ECPointGen(a.x, a.y)

        kBin = bin(k)
        kBin = kBin[2:len(kBin)]

        for i in range(1, len(kBin)):
            bit = kBin[i:i + 1]

            point = self.AddECPointsBinary(point, point)

            if bit == '1':

                point = self.AddECPointsBinary(point, a)

        return point


    def ECPointToString(self, a: ECPoint) -> str:
        return "({}, {})".format(a.x, a.y)

    def PrintECPoint(self, a: ECPoint):
        print(self.ECPointToString(a))
