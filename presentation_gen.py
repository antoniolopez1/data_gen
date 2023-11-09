import random
import faker
from faker import Faker

# Inicializa Faker
fake = Faker()

# Abre un archivo para escribir los datos SQL INSERT
with open('presentacion.sql', 'w') as file:

    # Define la cantidad de registros a generar
    num_registros = 5
    
    for _ in range(num_registros):
        preprod_name = fake.unique.word()  # Genera descripciones de presentación únicas
        insert_sql = f"INSERT INTO producto_presentacion (PREPROD_NAME) VALUES ('{preprod_name}');"
        file.write(insert_sql + '\n')
    
print(f"Se han generado  {num_registros} registros para la tabla 'producto_presentacion'.")