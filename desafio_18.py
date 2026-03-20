tempo_gasto_horas = int(input( ))
velocidade_media_kmh = int(input( ))

distancia = tempo_gasto_horas * velocidade_media_kmh

litros_necessarios = distancia / 12

print(f"{litros_necessarios:.3f}")

