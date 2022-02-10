
from database import engine
import models
from fastapi import FastAPI
from routers import post, user, auth, vote
import uvicorn

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='1228',
#                                 cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was succesfull!")
#         break
#     except Exception as error:
#         print("Connection was failed.\n")
#         print("Error: ", error)
#         time.sleep(2)    



if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')