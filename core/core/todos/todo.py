import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum
from uuid import UUID


class Status(StrEnum):
    pending = 'pending'
    done = 'done'
    cancelled = 'cancelled'
    in_progress = 'in_progress'


@dataclass(frozen=True)
class Todo:
    name: str
    id: UUID = uuid.uuid4()
    created_at: datetime = datetime.now()
    status: Status = Status.pending

    def __post_init__(self):
        cleaned_name: str = self.name.strip()

        if cleaned_name == '':
            raise ValueError('Task name is required.')



