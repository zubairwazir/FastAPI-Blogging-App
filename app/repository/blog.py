from fastapi import status, HTTPException
from app.models.models import BlogModel


def get(id, db):
    blog = db.query(BlogModel).filter(BlogModel.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"No Blog with id {id} Found!")

    return blog


def get_all(db):
    blogs = db.query(BlogModel).all()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No Blog Found!")

    return blogs


def create(blog, db):
    new_blog = BlogModel(title=blog.title, description=blog.description)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def update(id, blog, db):
    get_blog = get(id, db)
    if not get_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with id {id} not Found!')
    get_blog.update(blog)
    db.commit()
    return {"detail": f"Blog with id {id} is updated!"}


def delete(id, db):
    get_blog = get(id, db)
    if not get_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not Found!")

    get_blog.delete(synchronize_session=False)
    db.commit()
    return {"detail": f"Blog with id {id} is deleted!"}