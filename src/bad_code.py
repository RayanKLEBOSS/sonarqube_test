import os

def calculate_average(numbers):
    # Code Smell : Variable inutile et boucle mal optimisée
    total = 0
    for i in range(len(numbers)):
        total = total + numbers[i]
    
    # BUG : Division par zéro possible si la liste est vide !
    return total / len(numbers)

def authenticate_user(user, password):
    # VULNÉRABILITÉ SÉCURITÉ : Mot de passe codé en dur (Hardcoded credentials)
    if user == "admin" and password == "SuperSecret123!":
        print("Accès accordé")
        return True
    return False

def execute_command(cmd):
    # VULNÉRABILITÉ SÉCURITÉ : Injection de commande (Command Injection)
    os.system("echo " + cmd)