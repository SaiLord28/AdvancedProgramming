import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

# Inicializa la aplicación
app = FastAPI()

# Conecta con la base de datos
engine = create_engine('postgresql://postgres:postgres@localhost:5432/public')
metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))
Session = sessionmaker(bind=engine)

@app.get("/hello_ud")
def hello_ud():
    return "Welcome to UD!"

@app.get("/products")
def get_products():

    # Crea una sesión

    global products

    session = Session()

    query = products.select()
    result = session.execute(query)

    products_info = result.fetchall()

    # Cierra la sesión
    session.close()
    return products_info

@app.post("/products_pos")
def create_product(name: str, description: str):

    global products
    # Crea una sesión
    session = Session()

    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()

    # Cierra la sesión
    session.close()

    return {"message": "Product created successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)