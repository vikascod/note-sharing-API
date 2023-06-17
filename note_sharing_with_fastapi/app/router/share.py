from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db


router = APIRouter(
    tags=['Share']
)

@router.post('/share-note')
async def share_notes(user_id:int, note_id:int, share:schemas.ShareNote, db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found {user_id}")
    note = db.query(models.Note).filter(models.Note.id==note_id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note not found {note_id}")

    share_note = models.Share(user_id=user_id, note_id=note_id)
    db.add(share_note)
    db.commit()
    db.refresh(share_note)
    return "Successfully shared!"