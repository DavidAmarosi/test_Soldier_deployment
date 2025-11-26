from fastapi import FastAPI, HTTPException, Request, UploadFile, File
from pydantic import BaseModel
import sqlite3
import os
from datetime import datetime
import uvicorn
import csv
import io
from operator import itemgetter


app = FastAPI(title="Soldier deployment API (SQLite)", version="1.0.0")
@app.middleware("http")
def print_middleware(request: Request, call_next):
    print(f"Request: {request.method} {request.url.path}")
    response = call_next(request)
    return response

DB_FILE = "Soldier_deployment_db.sqlite"
class Soldier(BaseModel):
    soder_nomber: int 
    first_name: str
    last_name: str
    gender: str
    city:str
    distance: int


def import_csv_to_db(csv_content: bytes) -> dict:
    csv_text = csv_content.decode('utf-8')
    csv_reader = csv.DictReader(io.StringIO(csv_text))
 
    data = []
    for row in csv_reader:
        cleaned_row = {"soder_nomber":row["soder_nomber"],"first_name":row["first_name"],
                       "last_name":row["last_name"],"gender":row["gender"],"city":row["city"],"distance":row["distance"]}
        data.append(cleaned_row)

    print(data)
    return data

@app.post("/assignWithCsv")
async def upload_csv(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="File must be a CSV file")
    
    contents = await file.read()
    
    result = import_csv_to_db(contents)
    return result


def Sort_the_list_by_distance(list_soldier: list[dict]) -> list[dict]:
    a = int(list_soldier["distance"])
    list_soldier_by_distance = sorted(list_soldier, key=itemgetter("distance") ,reverse=True)
    return list_soldier_by_distance


def residential_house(soldiers: list[dict])-> list[dict]:
    house_1 = [[] for row in range(10)]
    house_2 = [[] for row in range(10)]
    List_after_population = []  
    index = 0
    for soldier in soldiers:
        if index < 80:
            soldier.update({"status":None,"house": "house_1","room": index // 8})
            List_after_population.append(soldier)


        elif index <= 160 and index > 80:
            soldier.update({"house": "house_2","room": (index-80) // 8})
            List_after_population.append(soldier)

        else:
            soldier.update({"status":"waiting list"})
            List_after_population.append(soldier)

        index +=1

        return List_after_population
    

def Population_mapping_and_waiting_list(soldiers: list[dict])-> list[dict]:
    Embedded_list = []
    List_of_non_embedded = []
    for soldier in soldiers:
        if soldier["status"] == None:
            Embedded_list.append(soldier)
    else:
        List_of_non_embedded.append(soldier)
        return { "num of the soldier embedded":len(Embedded_list)," num of the soldier non-embedded":len(List_of_non_embedded)}


    
def all_the_soldier(soldiers: list[dict])-> list[dict]:
    for soldier in soldiers:
        if soldier["status"] is None:
            return {"A":soldier["house"],"B":soldier["room"]}
        else:
            return {"C":soldier["soder_nomber"],"D":soldier["status"]}
        
 
@app.get("/assignWithCsv")
def get_all_soldier():
    return Population_mapping_and_waiting_list()


@app.get("/assignWithCsv")
def get_all_soldier():
    return all_the_soldier()

# class Base(BaseModel):
#     id_room: int
   

#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS Dorm A (
#             id_roon INTEGER PRIMARY KEY AUTOINCREMENT,
#             id_Bed INTEGER PRIMARY KEY AUTOINCREMENT,
#             soder_nomber INTEGER NOT NULL,
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             gender TEXT NOT NULL,
#             distance INTEGER NOT NULL,
#         )
#     """)






### uvicorn Soldier_deployment:app --reload
