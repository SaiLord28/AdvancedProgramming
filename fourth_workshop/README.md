# Fixing errors - worskshop

The objetive of this workshop was rewritte some codes in order to fix the problem in each one. So, in this files are some comments to explain all the changes I did.

## "#" and ' """ ' Comments 


the "#" Comments are indicated by the changes I did to the original file.


Meanwhile the ' """ ' comments are new comments I add to the files.


## How to start? Config Docker and more.

### 1. Create a Docker Network

 First, be sure you have a good configuration of Docker, after, you have to create a new connection using:


    docker network create connection
        
  
in the Docker folder.


### 2. Create a PostgreSQL Container

Now, create a new container of postgres in that connection using: 

    docker run --name postgres_container --network connection -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=public -p 5432:5432 -d postgres


### 3. Build the Application Image

After that, create a container to execute the application using:


    docker build -t 4wspimage:latest .


### 4. Create the table in the DataBase:

Create a table using:

    docker exec -it postgres_container psql -U postgres

and after:

    CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255)
    );



### 5. Run the Application Container

Now, run an image with:


    docker run -it --rm --name 4wspimage --network connection -p 8000:8080 -v ${PWD}:/Codes/app 4wspimage

in the Codes folder

### 6. Upload the table to the DataBase

Go to the Navigator and writte the localgost:8000/docs and execute the post /products_post commands, push the try it out button

### 7. Start the HTML

Start the html and push each button to watch it functionality


## Prerequisites

- Ensure you have Docker properly configured on your system.

## Contact

- Sergio Nicolás Mendivelso: snmendivelsom@udistrital.edu.co
