"""
2da Regla
Calcular el porcentaje de aciertos prueba de ishihara
"""
def calculate_porcentaje_hits(total_answers = 1, success_answers = 1  ):
    if total_answers <=  0 or success_answers <= 0:
        pass

    porcentaje_hits = success_answers * 100 / total_answers

    return porcentaje_hits
