from fastapi import FastAPI ,  Depends , status ,HTTPException ,Path
from schemas.blog_schema import Blog_Schema
from models import blog_model
from models.blog_model import Blog_Model
from core.database import engine,  get_db
from typing import Annotated
from sqlalchemy.orm import Session

blog_model.Base.metadata.create_all(bind=engine)
app = FastAPI()

db_dependency = Annotated[Session,Depends(get_db)]

@app.get("/blogs")
async def get_all_blogs(db:db_dependency):
    return db.query(Blog_Model).all()

@app.get("/blog/{id}")
async def get_blog_by_id(db:db_dependency , id:int = Path(gt=0)):
    blog_data = db.query(Blog_Model).filter(Blog_Model.id == id).first()
    if blog_data is not None:
        return blog_data
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Blog not found")

@app.post("/blog" ,status_code=status.HTTP_201_CREATED)
async def create_blog(request:Blog_Schema ,  db:db_dependency):
    new_blog = Blog_Model(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

@app.put("/blog/{id}" ,  status_code=status.HTTP_202_ACCEPTED)
async def update_blog_by_id(db:db_dependency , request:Blog_Schema,id:int = Path(gt=0)):
    blog_data=db.query(Blog_Model).filter(Blog_Model.id == id).first()
    if blog_data is not None:
        blog_data.update(request.model_dump())
        db.commit()
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail="Blog not found")
    

@app.delete("/blog/{id}",status_code = status.HTTP_204_NO_CONTENT)
async def delete_blog_by_id(db:db_dependency , id:int = Path(gt=0) ):
    blog_data = db.query(Blog_Model).filter(Blog_Model.id == id).first()
    if blog_data is not None:
        blog_data.delete(synchronize_session=False)
        db.commit()
        return "done"
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Blog not found")
