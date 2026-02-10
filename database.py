from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import insert
from sqlalchemy.orm import Session
from sqlalchemy import select



class Base(DeclarativeBase):
    pass

class Storage(Base):
    __tablename__ = "Storage"
    name: Mapped[str] = mapped_column(String(30))
    imagename: Mapped[str] =  mapped_column(String(30))
    profile: Mapped[str] =  mapped_column(String(100000))
    id: Mapped[int] = mapped_column(primary_key=True)


from sqlalchemy import create_engine
engine = create_engine("sqlite:///mydatabase.sqlite", echo=True)
Base.metadata.create_all(engine)

def Create(name, imagename, profile):
    stmt = insert(Storage).values(name=name, imagename=imagename , profile=profile)
    mysession = Session(engine)
    mysession.execute(stmt) 
    mysession.commit()
def fetchprofiles():
    Code = select(Storage)
    Connect = Session(engine)
    crazydata = Connect.scalars (Code).all()
    return crazydata

def Read():
    pass
def Update():
    pass
def Delete():
    pass

fetchprofiles()



