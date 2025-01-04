from datetime import datetime, timedelta
from unittest.mock import patch
import uuid
import pytest
from freezegun import freeze_time

from core.todos.create_todo import init_todo
from core.todos.todo import Status, Todo


def test_create_basic_valid_todo() -> None:
    mock_uuid4 = uuid.UUID("352c9582-2d41-4ba7-9b9e-d8e7d72ee7ac")

    with freeze_time("2024-12-12"), patch("uuid.uuid4", return_value=mock_uuid4):
        todo: Todo = init_todo(name="Learn Flask")

    assert todo == Todo(
        name="Learn Flask",
    )


def test_create_todo_empty_name() -> None:
    with pytest.raises(ValueError, match="Task name is required"):
        init_todo(name="")


def test_create_todo_invalid_name() -> None:
    with pytest.raises(ValueError, match="Task name is required"):
        init_todo(name="  ")


@pytest.mark.skip(reason="Not implemented yet")
def test_create_todo_with_all_options() -> None:
    with freeze_time("2024-12-12"):
        start_datetime = datetime.now() + timedelta(days=1)
        data = {
            "name": "Learn Flask",
            "description": "Learn Flask in 2025",
            "start_dt": start_datetime,
            "duration": timedelta(minutes=10),
            "estimated_duration": timedelta(minutes=10),
            "type": "workshop",
            "priority": "critical",
            "status": "pending",
        }

        todo = init_todo(**data)

        assert todo == {
            **data,
            "id": 1,
            "status":
                "pending",
            "created_at": datetime(2024, 12, 12)
        }


@pytest.mark.skip(reason="Not implemented yet")
def test_create_todo_with_past_start_date() -> None:
    with freeze_time("2024-12-12"):
        start_datetime = datetime(2024, 12, 11)
        with pytest.raises(ValueError, match="Start date cannot be in the past"):
            init_todo(name="Learn Flask", start_dt=start_datetime)


def test_create_todo_with_non_positive_duration():
    pass


def test_create_todo_with_non_positive_estimated_duration():
    pass
