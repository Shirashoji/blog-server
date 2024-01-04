from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session


from api.dps import get_db
from api import auth
from common import schemas, crud

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/blog/", response_model=schemas.Blog, tags=["blogs"])
async def create_blog(
    blog: schemas.BlogCreate, db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
):
    user = await auth.get_current_user(token, db)
    print("user_id: " + str(user.id))
    return crud.create_blog(db=db, blog=blog, owner_id=user.id)


@router.get("/blog/", response_model=list[schemas.Blog], tags=["blogs"])
def read_blogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    blogs = crud.get_blogs(db, skip=skip, limit=limit)
    return blogs


@router.get("/blog/{id}", response_model=schemas.Blog, tags=["blogs"])
def read_blog(id: int, db: Session = Depends(get_db)):
    db_blog = crud.get_blog_by_id(db, blog_id=id)
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    return db_blog
