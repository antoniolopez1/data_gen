import random
import faker
from faker import Faker

# Inicializa Faker
fake = Faker()

# Abre un archivo para escribir los datos SQL INSERT
with open('proveedores.sql', 'w') as file:

    # Define la cantidad de registros a generar
    num_registros = 100
    for i in range(1,num_registros):
        # Genera datos aleatorios
        prov_id = i
        prov_apellido = fake.last_name()
        prov_nombre = fake.first_name()
        ruc_numero = fake.random_int(min=1000000, max=9999999)
        ruc_digito = random.randint(1, 9)
        prov_ruc = f'{ruc_numero}-{ruc_digito}'
        prov_dir = fake.street_address()
        prov_mail = fake.email()
        prov_telefono = fake.phone_number()
        max_length = 50  # Define la longitud máxima de la observación
        prov_obs = fake.text(max_nb_chars=max_length) if random.choice([True, False]) else None
        
        # Genera la sentencia SQL INSERT
        insert_sql = f"INSERT INTO proveedores (PROV_ID, PROV_NOMBRE, PROV_RUC, PROV_DIR, PROV_MAIL, PROV_TELEFONO_, PROV_OBS) VALUES ({prov_id}, '{prov_nombre}', '{prov_ruc}', '{prov_dir}', '{prov_mail}', '{prov_telefono}', '{prov_obs}');"

        # Escribe la sentencia SQL en el archivo
        file.write(insert_sql + '\n')

print(f"Se han generado {num_registros} registros y se han guardado en 'datos_prueba.sql'.")
