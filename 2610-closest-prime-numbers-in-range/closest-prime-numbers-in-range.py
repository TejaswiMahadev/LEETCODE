class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def sieve(n):
            """Returns a list of prime numbers up to n using the Sieve of Eratosthenes."""
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            
            for i in range(2, int(n**0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            
            return [i for i in range(n + 1) if is_prime[i]]
        
        # Generate all prime numbers up to `right`
        primes = sieve(right)
        
        # Filter primes within the given range [left, right]
        primes_in_range = [p for p in primes if left <= p <= right]
        
        if len(primes_in_range) < 2:
            return [-1, -1]
        
        # Find the closest prime pair
        min_gap = float('inf')
        ans = [-1, -1]
        
        for i in range(len(primes_in_range) - 1):
            gap = primes_in_range[i + 1] - primes_in_range[i]
            if gap < min_gap:
                min_gap = gap
                ans = [primes_in_range[i], primes_in_range[i + 1]]
        
        return ans
