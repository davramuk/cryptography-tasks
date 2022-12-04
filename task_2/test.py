from ECPoint import ECPoint
from ECurve import ECurve


# Let's take secp256k1 curve for tests
# Its parameters:

# p = 17
# a = 0
# b = 7
# g = (15, 13)

p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
a = 0x0000000000000000000000000000000000000000000000000000000000000000
b = 0x0000000000000000000000000000000000000000000000000000000000000007
g = (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
     0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)


curve = ECurve()
curve.setMod(p)
curve.setA(a)
curve.setB(b)
curve.BasePointGSet(g[0], g[1])

# 1. Get base point of curve
basePoint = curve.BasePointGGet()
print("1. Base point of curve: ({}, {}) - is on curve: {}".format(basePoint.x, basePoint.y, curve.IsOnCurveCheck(basePoint)))

# 2. Define point and check if it on the curve
customPoint = curve.ECPointGen(12, 5)
print("2. Custom point: ({}, {}) - is on curve: {}".format(customPoint.x, customPoint.y, curve.IsOnCurveCheck(customPoint)))

# 3. Generate point with base point
# order = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140
order = 5
generatedPoint = curve.ScalarMultBinary(basePoint, order)
print("3. Generated from base point: ({}, {}) - is on curve: {}".format(generatedPoint.x, generatedPoint.y, curve.IsOnCurveCheck(generatedPoint)))

# 4. Double this point
doubledPoint = curve.AddECPointsBinary(generatedPoint, generatedPoint)
print("4. Doubled point ({}, {}) -> ({}, {}) - is on curve: {}".format(generatedPoint.x, generatedPoint.y, doubledPoint.x, doubledPoint.y, curve.IsOnCurveCheck(doubledPoint)))

# 5. Add two points this point
sumPoint = curve.AddECPointsBinary(generatedPoint, basePoint)
print("5. Sum of points ({}, {}) + ({}, {}) -> ({}, {}) - is on curve: {}".format(generatedPoint.x, generatedPoint.y, basePoint.x, basePoint.y, sumPoint.x, sumPoint.y, curve.IsOnCurveCheck(sumPoint)))

# 6. Print point
print("6. Print point:")
curve.PrintECPoint(sumPoint)
