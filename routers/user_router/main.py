from fastapi import APIRouter

router = APIRouter()

fake_users_db = {"plumbus": {"name": "Plumbus"}, "gun": {"name": "Portal Gun"}}

@router.get("/")
async def read_users():
    return fake_users_db
