from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, models
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(
    prefix='/skills',
    tags=['Skill']
)

# SHOW COLLECTED ATTRIBUTES
def show_attributes(db):
    attr_collected: dict = {
        "STR": 0,
        "END": 0,
        "AGI": 0,
        "WIL": 0,
        "INT": 0,
        "PER": 0,
        "SPD": 0,        
    }
    skills = db.query(models.Skill).all()
    
    for skill in skills:
        sum_collected = attr_collected[skill.attribute]
        sum_collected += skill.collected
        
        attr_collected.update({skill.attribute: sum_collected})
        
    return attr_collected

# GET - RETURN ALL SKILLS (ONLY FOR INFORMATION)
@router.get('/', response_model=List[schemas.SkillOut])
def get_posts(db: Session = Depends(get_db)):
    skills = db.query(models.Skill).all()

    return skills

# ADD A POINT TO COLLECTED SKILL
@router.post('/add')
def add_attribute(skill: schemas.SkillChange, db: Session = Depends(get_db)):
    skill_query = db.query(models.Skill).filter(models.Skill.name == skill.name).first()

    if skill_query is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Skill not found.')
    
    skill_query.collected += 1
    db.commit()
    
    attr_collected = show_attributes(db)
        
    return attr_collected

# REMOVE A POINT TO COLLECTED SKILL (if needed)
@router.post('/sub')
def sub_attribute(skill: schemas.SkillChange, db: Session = Depends(get_db)):
    skill_query = db.query(models.Skill).filter(models.Skill.name == skill.name).first()
    
    
    if skill_query.collected >= 1:
        skill_query.collected -= 1
        
    db.commit()
    
    attr_collected = show_attributes(db)
        
    return attr_collected


# RESET THE COLLECTED SKILL POINT (AT LEVEL UP)
@router.get('/reset')
def reset_attribute(db: Session = Depends(get_db)):
    skills = db.query(models.Skill).all()
    
    for skill in skills:
        skill.collected = 0
        
    db.commit()
    
    attr_collected = show_attributes(db)
        
    return attr_collected