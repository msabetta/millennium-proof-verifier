# navier_stokes/singularity_detector.py
import numpy as np

def monitor_smoothness(velocity_field, dt, t_max):
    """
    Monitora se il gradiente del campo di velocità nabla u 
    subisce un'esplosione (blow-up) che rompe la regolarità.
    """
    t = 0.0
    u = np.array(velocity_field, dtype=float)
    
    print("[*] Monitoraggio regolarità Navier-Stokes avviato...")
    
    while t < t_max:
        # Calcolo del gradiente spaziale (differenze finite)
        grad_u = np.gradient(u)
        # Calcolo della norma di Enstrofia (dissipazione di energia)
        enstrophy = np.sum(np.square(grad_u))
        
        # Condizione di Blow-up: l'enstrofia tende a infinito in tempo finito
        if np.isinf(enstrophy) or enstrophy > 1e10:
            print(f"[SINGULARITY DETECTED] Esplosione della soluzione al tempo t = {t:.4f}!")
            print(f"Norma del Gradiente (Enstrofia): {enstrophy}")
            return "Singular"
            
        # Evoluzione fittizia (qui andrebbe il solutore PDE specifico)
        u += np.random.normal(0, 0.01, u.shape)  # Simulazione fluttuazione
        t += dt
        
    print("[SUCCESS] La soluzione è rimasta regolare (smooth) per tutto l'intervallo temporale.")
    return "Smooth"

if __name__ == "__main__":
    # Inizializza un cubo di velocità 3D 10x10x10
    mock_velocity = np.random.rand(10, 10, 10)
    monitor_smoothness(mock_velocity, dt=0.01, t_max=1.0)