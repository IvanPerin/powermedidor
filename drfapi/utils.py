from .models import Medidor, Medicion


# Funcion que calcula los consumos
def calculo_consumos(key_id):

    # Cargo todas las mediciones correspondientes al medidor seleccionado
    mediciones = Medicion.objects.filter(Medidor=key_id)

    # Cargo el medidior seleccionado
    medidor = Medidor.objects.get(Llave_Ident=key_id)

    # Variables auxiliares
    aux_consumo_maximo = 0
    aux_consumo_minimo = 0
    aux_consumo_total = 0
    aux_cont_med = 0

    # Recorrer Objeto Mediciones to calculate consuption
    for medicion in mediciones:

        if aux_cont_med == 0:       # the first value is always the min and should be != 0
            aux_consumo_minimo = medicion.Consumo

        if medicion.Consumo > aux_consumo_maximo:
            aux_consumo_maximo = medicion.Consumo
        if medicion.Consumo < aux_consumo_minimo:
            aux_consumo_minimo = medicion.Consumo

        aux_consumo_total += medicion.Consumo
        aux_cont_med += 1

    medidor.Consumo_max = aux_consumo_maximo
    medidor.Consumo_min = aux_consumo_minimo
    medidor.Consumo_total = aux_consumo_total
    medidor.Consumo_prom = round((aux_consumo_total / aux_cont_med), 2)

    medidor.save()

    return
