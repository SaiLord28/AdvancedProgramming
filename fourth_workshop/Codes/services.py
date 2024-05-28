"""

NOTE: READ THE README FIRST!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


This was an workshop where we had to fix some of the problems in the codes.

This where my result

Author: Sergio Mendivelso

Date: 27/05/2024

Email: snmendivelsom@udistrial.edu.co
"""


#======================== IMPORTS =========================


import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI
from fastapi.responses import JSONResponse  # Imported JSONResponse
from fastapi.middleware.cors import CORSMiddleware #Imported CORSMiddleware


# ========================== DECLARATION =========================


# Initialize the application
app = FastAPI()

# Added CORS middleware to allow cross-origin requests, and don't create conflicts
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Reorganize the methods, now are under the database connection

#Session will be created at the start of each web service and will be closed at the end.


engine = create_engine('postgresql://postgres:postgres@postgres_container:5432/public')
metadata = MetaData()

products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))
Session = sessionmaker(bind=engine)

#Repited app = FastApi() deleted


#====================================== WEB SERVICES =================================


@app.get("/hello_ud")

def hello_ud() -> str:
    """

    main function:

    - This function returns a message to the user.

    steps:

    - return a message

    Parameters:

    - None

    return: 
    
    A string containing the welcome message.

    """
    return "Welcome to UD!"


#--------------------------------------


@app.get("/products")
def get_products():

    """

    main function:

    - This function returns a list of products.

    steps:

    - Create a session.
    - Create a query to select all the products.
    - Execute the query.
    - fetch all products
    - Close the session
    - Convert into dictionaries to make compatible with JSON
    - Return a JSON response with the product information.

    parameters:

    - None

    return:

    - A JSON response with the product information.

    """

    # declare products as global
    global products


    # Create a session
    session = Session()

    query = products.select()
    result = session.execute(query)

    products_info = result.fetchall()

    # Close the session
    session.close()

    # Convert into dictionaries to make compatible with JSON
    products_dict = [{"id": row.id, "name": row.name, "description": row.description} for row in products_info]

    # Return a JSON response with the product information
    return JSONResponse(content=products_dict)

    # ------------------------------------------------------------

@app.post("/products_pos")
def create_product(name: str, description: str):

    """
    main funciton:

    - This function creates a new product.

    steps:

    - Create a session.
    - Create a query to insert a new product.
    - Execute the query.
    - Commit the changes.
    - Close the session.
    - Return  a message indicating that the product was created successfully.

    parameters:

    - name (str): Name of the product.
    - description (str): Description of the product.

    return:

    - A message indicating that the product was created successfully.



    """

    # declare products as global
    global products

    # Create a session
    session = Session()

    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()

    # Close the session
    session.close()

    return {"message": "Product created successfully"}


#========================== PRICNIPAL MAIN ===============================================

if __name__ == "__main__":

    """
    main function:

    - This function runs the app.

    """
    uvicorn.run(app, host="0.0.0.0", port=8080)