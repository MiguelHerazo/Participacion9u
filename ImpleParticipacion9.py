rom typing import Tuple

class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo
    
    def procesar_datos(self) -> Tuple[float, float, float, float, str]:
        suma_temperatura = 0
        suma_humedad = 0
        suma_presion = 0
        suma_velocidad_viento = 0
        conteo_registros = 0
        conteo_direcciones = {}

        with open('datos_meteorologicos.txt', 'r',) as archivo:
            for i in archivo:
                if not i.strip():
                    continue

                if i.startswith('Temperatura:'):
                    suma_temperatura += float(i.split(':')[1])
                elif i.startswith('Humedad:'):
                    suma_humedad += float(i.split(':')[1])
                elif i.startswith('Presión:'):
                    suma_presion += float(i.split(':')[1])
                elif i.startswith('Viento:'):
                    viento = i.split(':')[1].strip().split(',')
                    suma_velocidad_viento += float(viento[0])
        
                direccion_viento = viento[1]
                if direccion_viento in conteo_direcciones:
                    conteo_direcciones[direccion_viento] += 1
                else:
                    conteo_direcciones[direccion_viento] = 1

                conteo_registros += 1

        temp_promedio = suma_temperatura / conteo_registros
        hum_promedio = suma_humedad / conteo_registros
        pres_promedio = suma_presion / conteo_registros
        vel_viento_promedio = suma_velocidad_viento / conteo_registros

        conteo_max = 0
        direccion_viento_prominente = ""

        for direccion, conteo in conteo_direcciones.items():
            if conteo > conteo_max:
                conteo_max = conteo
                direccion_viento_prominente = direccion

        return (temp_promedio, hum_promedio, pres_promedio, vel_viento_promedio, direccion_viento_prominente)



        



