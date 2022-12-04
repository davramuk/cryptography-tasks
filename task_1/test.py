from ModArith import ModArith

modular = ModArith()

# 1. Set m:
modular.set_m(4)
print("1.  m = {}".format(modular.m))

# 2. Solution for equation: a (mod m) = x
#    For example 6 (mod 5) = x
modular.set_a(6)
modular.set_m(5)

print("2.  {} (mod {}) = {}".format(modular.a, modular.m, modular.get_x()))

# 3. Solution for equation: a^b (mod m) = x
#    For example 6^3 (mod 7) = x
modular.set_a(6)
modular.set_b(3)
modular.set_m(7)

print("3.1 Not optimal: {}^{} (mod {}) = {}".format(modular.a, modular.b, modular.m, modular.get_x_power()))
print("3.2 Optimal: {}^{} (mod {}) = {}".format(modular.a, modular.b, modular.m, modular.get_x_power_optimal()))

# 4. Solution for equation: a*x = b (mod m)
#    For example 5*x = 6 (mod 7)
modular.set_a(5)
modular.set_b(6)
modular.set_m(7)

print("4.  {}*{} = {} (mod {})".format(modular.a, modular.get_x_linear(), modular.b, modular.m))

# 5. Random prime number in range(A, B)
A = 10
B = 35

print("5.  Random prime number (from {} to {}) -> {}".format(A, B, modular.get_random_prime(A, B)))
