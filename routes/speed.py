from fastapi import APIRouter, Query
from sqlalchemy import  text
from config.db import conn
import datetime
from typing import List

router= APIRouter()


@router.get('/info')
async def get_info():
    sql=text('SELECT * FROM SpeedTestColbun')
    results = conn.execute(sql)
    names = results.fetchall()

    return names

@router.post('/')
async def insert_bd(item:dict):
    now = datetime.datetime.now()
    conteo=text("SELECT COUNT(Date) FROM SpeedTestColbun")
    stmt=conn.execute("INSERT INTO SpeedTestColbun (Date, Ping, Download, Upload, Fecha, Server) VALUES (%s,%s,%s,%s,%s,%s)",(now, item["Ping"],item["Download"], item["Upload"], item["Fecha"], item["Server"]))
    count = conn.execute(conteo)
    count=count.fetchall()
    if(count[0][0]>1000):
        delete=text("DELETE TOP(100) from SpeedTestColbun where Date < GETDATE()-3")
        del_first = conn.execute(delete)
    return item