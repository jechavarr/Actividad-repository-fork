# Lista de productos, donde cada producto es un diccionario con nombre, categoría y precio
productos = [
    {"nombre": "camisa", "categoría": "ropa", "precio": 25.0},
    {"nombre": "pantalón", "categoría": "ropa", "precio": 40.0},
    {"nombre": "libro", "categoría": "papelería", "precio": 15.0},
    {"nombre": "cuaderno", "categoría": "papelería", "precio": 5.0},
    {"nombre": "zapatos", "categoría": "calzado", "precio": 60.0},
    {"nombre": "sandalias", "categoría": "calzado", "precio": 30.0}
]

# Función que filtra productos por categoría
def filtrar_por_categoria(lista_productos, categoria):
    """
    Recibe una lista de productos y una categoría,
    devuelve una lista con los nombres de productos que pertenecen a esa categoría.
    """
    resultado = []  # Lista para guardar los nombres que coincidan
    for producto in lista_productos:
        # Comprobamos si la categoría del producto es igual a la categoría dada
        if producto["categoría"] == categoria:
            resultado.append(producto["nombre"])  # Añadimos el nombre a la lista resultado
    return resultado

# Función que calcula el precio total de todos los productos
def calcular_precio_total(lista_productos):
    """
    Recibe una lista de productos,
    retorna la suma de los precios de todos ellos.
    """
    total = 0  # Variable para acumular el total
    for producto in lista_productos:
        total += producto["precio"]  # Sumamos el precio de cada producto al total
    return total

# Función que encuentra el producto más caro
def producto_mas_caro(lista_productos):
    """
    Recibe una lista de productos,
    retorna una tupla con el nombre y precio del producto con el precio más alto.
    """
    # Suponemos que el primer producto es el más caro inicialmente
    mas_caro = lista_productos[0]
    for producto in lista_productos:
        # Si encontramos un producto con precio mayor, actualizamos mas_caro
        if producto["precio"] > mas_caro["precio"]:
            mas_caro = producto
    return (mas_caro["nombre"], mas_caro["precio"])

# Ejemplos de uso
ropa = filtrar_por_categoria(productos, "ropa")
print(ropa)  # Salida esperada: ['camisa', 'pantalón']

total = calcular_precio_total(productos)
print(total)  # Salida esperada: 175.0

mas_caro = producto_mas_caro(productos)
print(mas_caro)  # Salida esperada: ('zapatos', 60.0)
