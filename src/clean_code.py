"""Module propre pour le calcul de moyennes et la validation."""

def calculate_average(numbers: list[float]) -> float:
    """Calcule la moyenne d'une liste de nombres en gérant les cas limites."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)