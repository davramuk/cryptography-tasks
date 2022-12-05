import random
import math


class ModArith(object):
    """ModArith class"""

    def __init__(self):
        self.m = None
        self.a = None
        self.b = None


    def set_m(self, m):
        self.m = int(m)


    def set_a(self, a):
        self.a = int(a)


    def set_b(self, b):
        self.b = int(b)


    def check_variables(self, vars):

        cond = True

        for var in vars:
            try:
                getattr(self, var)
            except Exception as e:
                print(e)
                cond = False

        return cond


    def get_x(self, a = False, m = False):

        """Finds the root of following equation: a (mod m) = x"""

        cur_a = self.a
        if(a != False):
            cur_a = a

        cur_m = self.m
        if(m != False):
            cur_m = m


        x = cur_a % cur_m

        return x


    def get_x_power(self, a = False, b = False, m = False):

        """Finds the root of following equation: a^b (mod m) = x"""

        cur_a = self.a
        if(a != False):
            cur_a = a

        cur_b = self.b
        if(b != False):
            cur_b = b

        cur_m = self.m
        if(m != False):
            cur_m = m


        x = (cur_a ** cur_b) % cur_m

        return x


    def get_x_power_optimal(self, a = False, b = False, m = False):

        """
            Finds the root of following equation: a^b (mod m) = x
            (optimal solution)
        """

        cur_a = self.a
        if(a != False):
            cur_a = a

        cur_b = self.b
        if(b != False):
            cur_b = b

        cur_m = self.m
        if(m != False):
            cur_m = m


        x = 1
        for i in range(cur_b):
            x = (x * cur_a) % cur_m

        return x


    def get_gcd(self, num_1, num_2):

        """Finds greatest common divisor via Euclidean algorithm"""

        if(num_1 == 0):
            return num_2

        while(num_2 != 0):
            if(num_1 > num_2):
                num_1 -= num_2

            else:
                num_2 -= num_1

        return num_1


    def get_euler(self, num):

        """Finds result of Euler function"""

        fi = 1

        for i in range(2, math.floor(num ** 0.5)):

            p = 1
            while(not num % i):
                p *= i
                num /= i

            p /= i

            if(p >= 1):
                fi = fi * p * (i - 1)

        num -= 1
        if(num):
            return num * fi
        else:
            return fi


    def get_x_linear(self, a = False, b = False, m = False):

        """Finds the root of following equation: a*x = b (mod m)"""

        cur_a = self.a
        if(a != False):
            cur_a = a

        cur_b = self.b
        if(b != False):
            cur_b = b

        cur_m = self.m
        if(m != False):
            cur_m = m


        # Check for GCD (a, m) == 1
        if(self.get_gcd(cur_a, cur_m) == 1):

            eul = self.get_euler(cur_m) - 1
            x = (self.get_x(cur_b, cur_m) * self.get_x_power_optimal(cur_a, eul, cur_m) ) % cur_m

            return x
        else:
            # No solutions
            return False


    def get_random_prime(self, start, end):

        """Returns random prime number from start to end arguments"""

        primes = []

        for i in range(int(start), int(end) + 1):
            if(i not in [0, 1]):
                cond = True
                for j in range(2, i):
                    if(i % j == 0):
                        cond = False
                        break

                if(cond == True):
                    primes.append(i)

        # Select random from primes
        len_primes = len(primes)
        if(len_primes == 0):
            return False

        index = random.randint(0, len_primes - 1)

        return primes[index]
