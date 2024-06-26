from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from db import get_db
import repository as repository_contacts
from schemas import ContactResponse
from typing import List

app = APIRouter(prefix='/contacts', tags=["contacts"])


@app.get('/', response_model=List[ContactResponse])
async def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(skip, limit, db)
    return contacts


@app.get('/{contact_id}', response_model=ContactResponse)
async def read_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@app.post("/", response_model=ContactResponse)
async def create_contact(body: ContactResponse, db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(body, db)


@app.put("/{contact_id}", response_model=ContactResponse)
async def update_contact(body: ContactResponse, contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact


@app.delete("/{contact_id}", response_model=ContactResponse)
async def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    contact = await repository_contacts.delete_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contact