from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List


router = APIRouter(
    tags=["Blog"]
)


@router.post("/create_blog", status_code=status.HTTP_201_CREATED, response_model=BlogResponseSchema)
def create_blog(blog: BlogSchema, db: Session = Depends(get_db)):
    new_blog = BlogModel(title=blog.title, description=blog.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/get_blog/{id}", status_code=status.HTTP_200_OK, response_model=BlogResponseSchema)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Blog with id {id} Found!")

    return blog


@router.put("/update_blog", status_code=status.HTTP_202_ACCEPTED, response_model=BlogResponseSchema)
def update_blog(id: int, blog: BlogUpdateSchema, db: Session = Depends(get_db)):
    update_blog = db.query(BlogModel).filter(BlogModel.id == id).first()

    if not update_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not Found!')
    update_blog.update(blog)
    db.commit()
    return {"detail": f"Blog with id {id} is updated!"}


@router.delete("/delete_blog", status_code=status.HTTP_204_NO_CONTENT, tags=['blog'])
def delete_user(id: int, db: Session = Depends(get_db)):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not Found!")

    blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id {id} is deleted!"}


@router.get("/get_blogs", status_code=status.HTTP_200_OK, response_model=List[BlogResponseSchema])
def get_blog(db: Session = Depends(get_db)):
    blogs = db.query(BlogModel).all()

    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Blog Found!")

    return blogs
