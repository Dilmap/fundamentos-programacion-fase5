# ---------------------------------------------------------
# Nombre del estudiante: Diego Rafael Abdala Florez
# Grupo: 213022_103
# Programa: Ingeniería de Sistemas
# Código Fuente: autoría propia con asistencia de IA para depuración
# ---------------------------------------------------------

def determinar_cantidad_pedido(stock_actual, stock_minimo):
    """
    Módulo (Función) que calcula la cantidad exacta a pedir para un artículo.
    
    Lógica de negocio:
    - Si el Stock Actual es menor al Stock Mínimo, se pide la diferencia.
    - Si el Stock Actual es suficiente, la cantidad a pedir es cero.
    """
    # Guardia de tipos: Asegura que los parámetros sean numéricos (TypeError)
    if not isinstance(stock_actual, (int, float)) or not isinstance(stock_minimo, (int, float)):
        raise TypeError(f"Los stocks deben ser numéricos. Recibido: stock_actual={type(stock_actual).__name__}, stock_minimo={type(stock_minimo).__name__}")
    
    # Validaciones semánticas (ValueError)
    if stock_actual < 0:
        raise ValueError(f"El stock actual no puede ser negativo: {stock_actual}")
    if stock_minimo <= 0:
        raise ValueError(f"El stock mínimo debe ser mayor a cero: {stock_minimo}")
    
    # Aplicación de la lógica de negocio
    if stock_actual < stock_minimo:
        cantidad_a_pedir = int(stock_minimo - stock_actual)  # Forzamos int para evitar pedir fracciones de hardware
    else:
        cantidad_a_pedir = 0
        
    return cantidad_a_pedir


def generar_informe_auditoria(matriz_inventario):
    """
    Módulo que recorre la matriz de inventario, procesa cada artículo
    e imprime la lista de pedidos final manejando excepciones por fila.
    """
    print("\n=============================================")
    print("   INFORME DE AUDITORÍA Y REABASTECIMIENTO   ")
    print("=============================================")
    print(f"{'ARTÍCULO':<20} | {'CANTIDAD A PEDIR':<15}")
    print("---------------------------------------------")
    
    # Caso borde: Validación de matriz vacía
    if not matriz_inventario:
        print(f"{'[ADVERTENCIA]':<20} | No hay datos de inventario para procesar.")
        print("=============================================\n")
        return

    # Recorremos cada fila de la matriz
    for i, articulo in enumerate(matriz_inventario):
        try:
            # Validación de integridad de la estructura de la matriz (IndexError)
            if len(articulo) < 4:
                raise IndexError(f"Fila {i} incompleta: se esperan 4 campos, se encontraron {len(articulo)}")
            
            codigo       = articulo[0]
            nombre       = articulo[1]
            stock_actual = articulo[2]
            stock_minimo = articulo[3]
            
            # Intentamos realizar las conversiones a enteros por si vienen datos erróneos de usuario
            stock_actual = int(stock_actual)
            stock_minimo = int(stock_minimo)
            
            # Llamamos a la función de lógica de negocio
            pedido_exacto = determinar_cantidad_pedido(stock_actual, stock_minimo)
            
            # Imprimimos los resultados controlando el límite visual de caracteres para el formato
            print(f"{nombre[:20]:<20} | {pedido_exacto:<15}")
            
        except (TypeError, ValueError, IndexError) as e:
            # Captura el error específico de la fila, lo reporta y permite que el ciclo continúe
            print(f"{f'[ERROR FILA {i}]':<20} | {str(e)}")
            
    print("=============================================\n")


# --- Bloque Principal del Programa ---
if __name__ == "__main__":
    # Matriz inicial con 5 artículos: [Código, Nombre, Stock Actual, Stock Mínimo]
    # Incluye un caso con error controlado para demostrar la robustez del try-except
    inventario_auditoria = [
        [101, "Teclado Mecánico", 12, 15],      # Falta stock (Pide 3)
        [102, "Mouse Óptico",      25, 20],      # Stock suficiente (Pide 0)
        [103, "Monitor Gamer",     -4,  8],      # ERROR CONTROLADO: Stock negativo (ValueError)
        [104, "Auriculares Pro",   18, 15],      # Stock suficiente (Pide 0)
        [105, "Alfombrilla XL",     3, 10]       # Falta stock (Pide 7)
    ]
    
    # Ejecución del informe
    generar_informe_auditoria(inventario_auditoria)