from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    first_name: str
    last_name: str


class ContactResponse(ContactBase):
    id: int
    email: str
    phone_number: int
    born_date: int
    another_info: None
