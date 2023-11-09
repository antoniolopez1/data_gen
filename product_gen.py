import random
import faker
from faker import Faker

# Inicializa Faker
fake = Faker()

# Abre un archivo para escribir los datos SQL INSERT
with open('proveedores.sql', 'w') as file:
    num_registros_presentacion = 20

    # Define la cantidad de registros a generar para la tabla "producto_tipos"
    num_registros_tipos = 10

    # Define la cantidad de registros a generar para la tabla "producto_origen"
    num_registros_origen = 2

    # Define la cantidad de registros a generar para la tabla "productos"
    num_registros_productos = 50  # Puedes ajustar este número según tu necesidad

     # Genera datos para la tabla "producto_presentacion"
    for _ in range(num_registros_presentacion):
        preprod_name = fake.unique.word()
        insert_sql = f"INSERT INTO producto_presentacion (PREPROD_NAME) VALUES ('{preprod_name}');"
        file.write(insert_sql + '\n')

    # Genera datos para la tabla "producto_tipos"
    for _ in range(num_registros_tipos):
        tprod_name = fake.unique.word()
        insert_sql = f"INSERT INTO producto_tipos (TPROD_NAME) VALUES ('{tprod_name}');"
        file.write(insert_sql + '\n')

    # Genera datos para la tabla "producto_origen"
    for _ in range(num_registros_origen):
        oprod_name = fake.unique.random_element(elements=('nacional', 'importada'))
        insert_sql = f"INSERT INTO producto_origen (OPROD_NAME) VALUES ('{oprod_name}');"
        file.write(insert_sql + '\n')

    # Genera datos para la tabla "productos"
    for _ in range(num_registros_productos):
        tprod_id = random.randint(1, num_registros_tipos)
        oprod_id = random.randint(1, num_registros_origen)
        preprod_id = random.randint(1, num_registros_presentacion)
        prod_desc = fake.word()
        prod_pcosto = round(random.uniform(3500, 350000), 2)
        prod_pmayo = round(prod_pcosto * 1.15, 2)
        prod_pmino = round(prod_pcosto * 1.35, 2)
        prod_cant = random.randint(0, 200)

        insert_sql = f"INSERT INTO productos (TPROD_ID, OPROD_ID, PREPROD_ID, PROD_DESC, PROD_PCOSTO, PROD_PMAYO, PROD_PMINO, PROD_CANT) VALUES ({tprod_id}, {oprod_id}, {preprod_id}, '{prod_desc}', {prod_pcosto}, {prod_pmayo}, {prod_pmino}, {prod_cant});"
        file.write(insert_sql + '\n')