## Verificatore di Teoremi del Millennio (Python + Lean 4)

Questo progetto implementa un sistema ibrido di verifica formale per i problemi del Millennium Prize, utilizzando:
- **Python** per l'analisi numerica e la generazione di controesempi.
- **Lean 4** per la verifica assiomatica (formalizzazione).
- **GitHub Actions** per la CI/CD e l'esecuzione automatica dei test.
- **Mermaid** per la generazione di diagrammi.

## Specifiche Tecniche
- **Python**: 3.10
- **Lean 4**: 4.10.0
- **Architettura**: Client-Server
- **Repository**: GitHub
- **Licenza**: MIT

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Architettura

```mermaid
flowchart LR
    User[Utente] -->|Input Tesi| Verifier[Sistema Verificatore]
    Verifier -->|Analisi Numerica| Python[Python Scripts]
    Verifier -->|Verifica Formale| Lean[Lean 4 Formalizer]
    Python -->|Generazione Controesempi| User
    Lean -->|Verifica Assiomatica| User
```

## Diagramma UML

```mermaid
classDiagram
    class Verifier {
        +analyze()
        +formulate()
        +verify()
    }
    class Python {
        +generate_counterexamples()
    }
    class Lean {
        +formalize_proof()
    }
    Verifier --> Python
    Verifier --> Lean
```

## Diagramma di Sequenza

```mermaid
sequenceDiagram
    participant User
    participant Verifier
    participant Python
    participant Lean

    User->>Verifier: Input Tesi
    Verifier->>Python: Analisi Numerica
    Python-->>Verifier: Risultati
    Verifier->>Lean: Verifica Formale
    Lean-->>Verifier: Esito Verifica
    Verifier-->>User: Output Risultato
```


## Licenza

Licenza MIT

## Contribution

Contributi ben accetti. Si prega di aprire una issue o una pull request.

## Disclaimer

Questo progetto è solo a scopo didattico e non è affiliato al Clay Mathematics Institute.


