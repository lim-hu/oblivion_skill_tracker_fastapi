# Oblivion Skill Tracker backend app
Self made Oblivion skill tracker backend app, created by fastapi

Run the code: uvicode app.main:app
Use 127.0.0.1:8000/docs or Postman or Insomnia etc. to use it.

## Functions:
### 127.0.0.1:8000/skills
GET Method, show all skill with collected perk points

### 127.0.0.1:8000/skills/add
POST Method, add a perk point to skill
Use JSON for input:
{
"name": "skill"
}
where "skill" is the skill name, ie. "name": "Hand To Hand".

Return JSON data if ie. "Hand To Hand" icreased:
{
  "STR": 1,
  "END": 0,
  "AGI": 0,
  "WIL": 0,
  "INT": 0,
  "PER": 0,
  "SPD": 0
}

### 127.0.0.1:8000/skills/sub
POST Method, remove a perk point from skill
Use JSON for input:
{
"name": "skill"
}
where "skill" is the skill name, ie. "name": "Light Armor"

### 127.0.0.1:8000/skills/reset
GET Method, reset collected skill point. You can use it at level up.

Return JSON data if ie. "Light Armor" will be removed and we can say, that SPD = 3:
{
  "STR": 0,
  "END": 0,
  "AGI": 0,
  "WIL": 0,
  "INT": 0,
  "PER": 0,
  "SPD": 2
}
SPD removed by 1 (from 3 to 2)
