from fastapi import APIRouter

router = APIRouter(prefix="/speedtyping")

@router.post("/speedtyping")
async def add_task(
        task: Annotated[]
)