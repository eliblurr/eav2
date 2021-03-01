

#  single column search
async def read(skip:int, limit:int, search:str, value:str, db:Session):
    base = db.query(models.Ads)
    if search and value:
        try:
            base = base.filter(models.Ads.__table__.c[search].like("%" + value + "%"))
        except KeyError:
            return base.offset(skip).limit(limit).all()
    return base.offset(skip).limit(limit).all()

# multi column search
from sqlalchemy import or_

async def read(skip:int, limit:int, search:List[str], value:str, db:Session):
    base = db.query(models.Ads)
    if search and value:
        try:
            search_args = [models.Ads.__table__.c[col].like("%" + value + "%") for col in search]
            base = base.filter(or_(*search_args))
        except KeyError:
            return base.offset(skip).limit(limit).all()
    return base.offset(skip).limit(limit).all()

