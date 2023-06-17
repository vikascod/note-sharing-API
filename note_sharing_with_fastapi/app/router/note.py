from fastapi import APIRouter, Depends, status, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app import schemas, models
from app.database import get_db
from typing import List
from app.oauth2 import get_current_user
import shutil
import os

router = APIRouter(
    tags=['Notes']
)

@router.post('/upload-note', status_code=status.HTTP_201_CREATED)
async def upload_note(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: int = Depends(get_current_user)):
    
    upload_folder = 'files'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, file.filename)

    with open(file_path, 'wb') as f:
        shutil.copyfileobj(file.file, f)

    new_file = models.Note(user_id=current_user.id, filename=file.filename, content=file_path)
    db.add(new_file)
    db.commit()
    db.refresh(new_file)

    return [{'filename': new_file.filename, 'id': new_file.id}]
    
@router.get('/note', response_model=List[schemas.Note])
async def read_all_notes(db:Session=Depends(get_db)):
    notes = db.query(models.Note).all()
    return notes


@router.get('/note/{note_id}', response_model=schemas.Note)
async def read_note(note_id:int, db:Session=Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.id==note_id).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note not found {note_id}")
    return note

    
@router.get('/note/subject-name/{note_name}', response_model=schemas.Note)
async def read_note(note_name:str, db:Session=Depends(get_db)):
    note = db.query(models.Note).filter(models.Note.subject_name==note_name).first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note not found {note_name}")
    return note


@router.delete('/delete-note/{note_id}')
async def destroy_note(note_id:int, db:Session=Depends(get_db), current_user:int=Depends(get_current_user)):
    note = db.query(models.Note).filter(models.Note.id==note_id).first()
    if note.user.id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform action")
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Note not found {note_id}")
    db.delete(note)
    db.commit()
    return "Deleted"