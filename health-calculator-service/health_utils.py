def calculate_bmi(height: float, weight: float) -> float:
    """Calculer l'Indice de Masse Corporelle (BMI).
    
    Args:
        height: Taille en mètres
        weight: Poids en kg
        
    Returns:
        float: BMI arrondi à 2 décimales
    """
    if height <= 0:
        raise ValueError("La hauteur doit être supérieure à zéro.")
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def calculate_bmr(weight: float, height: float, age: int, gender: str) -> float:
    """Calculer le Taux Métabolique de Base (BMR) avec l'équation de Harris-Benedict.
    
    Args:
        weight: Poids en kg
        height: Taille en cm
        age: Âge en années
        gender: Genre ('male' ou 'female')
        
    Returns:
        float: BMR en calories par jour
    """
    if gender.lower() not in ['male', 'female']:
        raise ValueError("Le genre doit être 'male' ou 'female'.")
    
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:  # female
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    return round(bmr, 2)