def get_product(**datos):
    print(datos)
    print(datos["id"], datos["name"]) # Acceder a ciertos datos

get_product(id="01",
            name="iPhone",
            desc="Smartphone")