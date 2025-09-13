class Solution:
    def sieve(self, n):
        if not(1<=n<=10**4):
            raise ValueError("Invalid")
            return 0
        prime = [True] * (n+1)
        prime[0] = prime[1] = False  

        
        p = 2
        while p * p <= n:
            if prime[p]:
                for i in range(p*p, n+1, p):
                    prime[i] = False
            p += 1

        
        result = [i for i in range(2, n+1) if prime[i]]
        return result
