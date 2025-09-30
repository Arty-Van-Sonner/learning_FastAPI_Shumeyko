from typing import Annotated
from fastapi import APIRouter, Depends

from repository import TaskRepositoty
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)

@router.post('')
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepositoty.add_one(task)
    return STaskId.model_validate({'ok': True, 'task_id': task_id})

@router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepositoty.find_all()
    return {'tasks': tasks}