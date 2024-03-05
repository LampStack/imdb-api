#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# ┌──────────────────────────────────────┐
# │    > to run local server             │
# │        uvicorn main:app --reload     │
# │                                      │
# │    > developer :                     │
# │         @LampStack                   │
# └──────────────────────────────────────┘


from fastapi import FastAPI
from imdb import Cinemagoer, IMDbError

app = FastAPI()
ia = Cinemagoer()

@app.get("/")
async def root():
    return {"status": "error", "message": "to read docs open /docs"}


@app.get("/search/movie")
@app.get("/search/movie/{query}")
async def search_movie(query:str):
    try:
        movies = ia.search_movie(query)
        for i in range(len(movies)):
            movies[i]['movieID'] = movies[i].movieID
    except IMDbError as e:
        return {"status": "error", "message": e}
    else:
        return {"status": "ok", "result": movies}


@app.get("/search/person")
@app.get("/search/person/{query}")
async def search_person(query:str):
    try:
        peoples = ia.search_person(query)
        for i in range(len(peoples)):
            peoples[i]['personID'] = peoples[i].personID
    except IMDbError as e:
        return {"status": "error", "message": e}
    else:
        return {"status": "ok", "result": peoples}


@app.get("/get/movie")
@app.get("/get/movie/{query}")
async def get_movie(query:str):
    try:
        movie = ia.get_movie(query)
    except IMDbError as e:
        return {"status": "error", "message": e}
    else:
        return {"status": "ok", "result": movie}


@app.get("/get/person")
@app.get("/get/person/{query}")
async def get_person(query:str):
    try:
        person = ia.get_person(query)
    except IMDbError as e:
        return {"status": "error", "message": e}
    else:
        return {"status": "ok", "result": person}


@app.get("/search/keyword")
@app.get("/search/keyword/{query}")
async def search_keyword(query:str):
    try:
        keywords = ia.search_keyword(query)
    except IMDbError as e:
        return {"status": "error", "message": e}
    else:
        return {"status": "ok", "result": keywords}


@app.get("/get/keyword")
@app.get("/get/keyword/{query}")
async def get_keyword(query:str):
    try:
        keyword = ia.get_keyword(query)
    except IMDbError as e:
        return {"status": "error", "message": e}
    else:
        return {"status": "ok", "result": keyword}
