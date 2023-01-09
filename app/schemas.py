from pydantic import BaseModel


class SkillChange(BaseModel):
    name: str


class SkillGet(BaseModel):
    attribute: str


class SkillOut(SkillChange):
    id: int
    collected: int
    attribute: str

    class Config:
        orm_mode = True
