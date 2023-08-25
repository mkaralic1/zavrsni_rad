from .. import models, schemas, oauth2
from fastapi import  status, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

router=APIRouter(
    prefix="/destination",
    tags=['Destinations']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_dest(dest: schemas.DestCreate, db: Session = Depends(get_db)):
    new_dest = models.Destination(**dest.dict())
    db.add(new_dest)
    db.commit()
    db.refresh(new_dest)
    return new_dest

@router.get("/", response_model=List[schemas.DestOut])
def get_destinations(db: Session = Depends(get_db)):
    destinations = db.query(models.Destination).all()
    destinations_out = [schemas.DestOut(id=dest.id,     name=dest.name) for dest in destinations]
    return destinations_out



