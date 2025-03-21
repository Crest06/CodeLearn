function sieveOfEratosthenes(max) {
    const sieve = new Array(max + 1).fill(true);
    sieve[0] = false;
    sieve[1] = false;

    for (let p = 2; p * p <= max; p++) {
        if (sieve[p]) {
            for (let i = p * p; i <= max; i += p) {
                sieve[i] = false;
            }
        }
    }

    const primes = [];
    for (let i = 2; i <= max; i++) {
        if (sieve[i]) {
            primes.push(i);
        }
    }

    return primes;
}

const maxRange = 50; // Change this to set the maximum range
const primeNumbers = sieveOfEratosthenes(maxRange);

console.log(`Prime numbers up to ${maxRange}: ${primeNumbers.join(', ')}`);
