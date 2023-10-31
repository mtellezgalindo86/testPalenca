# Test Palenca Endpoints

Se hace este proyecto donde se encuentra una prueba técnica para Palenca

## Estructura de Carpetas


```plaintext
testPalenca/
├── app/
│   ├── adapters/
│   │   ├── login/
│   │   │   ├── login.py
│   │   │   └── __init__.py
│   │   ├── profile/
│   │   │   ├── profile.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── config/
│   │   ├── settings.py
│   │   └── __init__.py
│   ├── domain/
│   │   ├── entities/
│   │   │   ├── user.py
│   │   │   └── __init__.py
│   │   ├── models/
│   │   │   ├── login_response.py
│   │   │   └── profile_response.py
│   │   └── __init__.py
│   ├── routes/
│   │   ├── login/
│   │   │   ├── login.py
│   │   │   └── __init__.py
│   │   ├── profile/
│   │   │   ├── profile.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── use_cases/
│   │   ├── login/
│   │   │   ├── login.py
│   │   │   └── __init__.py
│   │   ├── profile/
│   │   │   ├── profile.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   └── __init__.py
├── tests/
│   ├── unit/
│   │   ├── test_login.py
│   │   ├── test_profile.py
│   │   └── __init__.py
│   └── __init__.py
├── main.py
├── README.md
├── docker-compose.yml
├── Dockerfile
└── Dockerfile.tests
```

## Descripción de Carpetas

- **adapters**: Contiene adaptadores que se encargan de la logica de los endpoints.

- **config**: Contiene las constantes que se tienen para el manejo y validaciones de los datos. 

- **domain**: Define las entidades y modelos.

- **routes**: Define las rutas .

- **use_cases**: Contiene casos de uso que encapsulan la lógica d.

- **tests**: Aquí se encuentran todas las pruebas unitarias.

## Ejecución del Proyecto con Docker

### Docker Compose

Para ejecutar el proyecto  debes tener docker instaldor

Ejecuta el siguiente comando 
```bash
docker-compose up --build
```

## Dentro del proyecto encontraras un archivo llamado curl.txt donde se encuentran las peticiones que se tienen que hacer
