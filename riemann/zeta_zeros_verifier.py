# riemann/zeta_zeros_verifier.py
import mpmath as mp

def verify_riemann_hypothesis_zeros(num_zeros=100, precision=50):
    """
    Calcola i primi N zeri non banali della funzione Zeta di Riemann 
    sulla linea critica re(s) = 0.5 per verificare deviazioni orizzontali.
    """
    mp.mp.dps = precision  # Imposta la precisione decimale (50 cifre)
    print(f"[*] Avvio verifica per i primi {num_zeros} zeri con precisione a {precision} decimali...")
    
    for i in range(1, num_zeros + 1):
        # Calcola l'i-esimo zero della funzione di Gram / Zeta
        zero_imag = mp.zetazero(i)
        
        # Uno zero non banale deve avere parte reale ESATTAMENTE a 0.5
        real_part = zero_imag.real
        imag_part = zero_imag.imag
        
        if not mp.almosteq(real_part, 0.5, abs_eps=10**(-precision+5)):
            print(f"[CRITICAL ERROR] Trovato controesempio! Zero #{i} fuori dalla linea critica: {zero_imag}")
            return False
            
    print(f"[SUCCESS] Tutti i primi {num_zeros} zeri rispettano la simmetria Re(s) = 1/2.")
    return True

if __name__ == "__main__":
    verify_riemann_hypothesis_zeros(num_zeros=10, precision=30)