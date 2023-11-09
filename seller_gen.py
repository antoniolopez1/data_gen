import random
import faker
from faker import Faker

# Inicializa Faker
fake = Faker()

# Abre un archivo para escribir los datos SQL INSERT
with open('vendedores.sql', 'w') as file:

    # Define la cantidad de registros a generar
    num_registros = 100

    for _ in range(num_registros):
        # Genera datos aleatorios
        vend_id = random.randint(1, 100)
        vend_apellido = fake.last_name()
        vend_nombre = fake.first_name()
        ruc_numero = fake.random_int(min=1000000, max=9999999)
        ruc_digito = random.randint(1, 9)
        vend_ruc = f'{ruc_numero}-{ruc_digito}'
        vend_dir = fake.street_address()
        vend_mail = fake.email()
        prov_telefono = fake.phone_number()
        max_length = 50  # Define la longitud máxima de la observación
        vend_obs = fake.text(max_nb_chars=max_length) if random.choice([True, False]) else None
        
        # Genera la sentencia SQL INSERT
        insert_sql = f"INSERT INTO vendedores (VEND_ID,  VEND_APELLIDO, VEND_NOMBRE, VEND_RUC, VEND_DIR, VEND_MAIL, PROV_TELEFONO_, VEND_OBS) VALUES ({vend_id}, '{vend_apellido}', '{vend_nombre}', '{vend_ruc}', '{vend_dir}', '{vend_mail}', '{prov_telefono}', '{vend_obs}');"

        # Escribe la sentencia SQL en el archivo
        file.write(insert_sql + '\n')

print(f"Se han generado {num_registros} registros y se han guardado en 'datos_prueba.sql'.")
