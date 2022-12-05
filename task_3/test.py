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

basePoint = curve.BasePointGGet()

# 1. Private keys
alice_private_key = 123
alice_public_key = curve.ScalarMultBinary(basePoint, alice_private_key)

bob_private_key = 436
bob_public_key = curve.ScalarMultBinary(basePoint, bob_private_key)

bob_alice_pk = curve.ScalarMultBinary(alice_public_key, bob_private_key)
alice_bob_pk = curve.ScalarMultBinary(bob_public_key, alice_private_key)

print("a * Hb = ({}, {})".format(bob_alice_pk.x, bob_alice_pk.y))
print("b * Ha = ({}, {})".format(alice_bob_pk.x, alice_bob_pk.y))
