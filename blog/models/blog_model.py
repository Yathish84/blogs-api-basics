from sqlalchemy import Column ,Integer,String
from core.database import Base

class Blog_Model(Base):
    __tablename__="blogs"
    
    id = Column(Integer ,primary_key=True,index=True)
    title =Column(String)
    body = Column(String)
    