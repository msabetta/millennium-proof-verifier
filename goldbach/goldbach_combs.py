# goldbach/goldbach_combs.py
import sympy

def goldbach_partitions(n):
    """Restituisce tutte le coppie di primi che sommate danno n."""
    if n <= 2 or n % 2 != 0:
        return []
    
    partitions = []
    # Controlliamo i primi fino a n/2
    for p in sympy.primerange(2, n // 2 + 1):
        q = n - p
        if sympy.isprime(q):
            partitions.append((p, q))
    return partitions

def verify_goldbach_bounds(max_even, theoretical_formula=None):
    """Verifica la congettura e la deviazione rispetto a una formula teorica."""
    print(f"[*] Analisi densità di Goldbach fino a n = {max_even}...")
    for n in range(4, max_even + 1, 2):
        pairs = goldbach_partitions(n)
        
        if len(pairs) == 0:
            print(f"[CRITICAL] CONTROESEMPIO TROVATO: {n} non ha partizioni di Goldbach!")
            return False
        
        # Se hai proposto una formula per la "Cometa di Goldbach", la validiamo qui
        if theoretical_formula:
            calculated = len(pairs)
            expected = theoretical_formula(n)
            error = abs(calculated - expected)
            print(f"n: {n} | Partizioni reali: {calculated} | Attese: {expected} | Delta: {error}")
            
    print(f"[SUCCESS] Congettura verificata numericamente fino a n = {max_even}.")
    return True



if __name__ == "__main__":
    # Esempio banale senza formula teorica
    verify_goldbach_bounds(max_even=100000)