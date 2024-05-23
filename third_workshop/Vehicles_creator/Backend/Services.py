from fastapi import FastAPI

app = FastAPI()

# possible vehicles

vehicles = []

# services


@app.get("/vehicles/")
async def get_vehicles():

    #Note: the vehicle is created with the engine, so it will show the engine too
    return {"message": "Get all vehicles"}

@app.post("/engines/")
async def add_engine():
    return {"message": "Add a new engine"}

@app.post("/vehicles/")
async def add_vehicle():
    return {"message": "Add a new vehicle"}
