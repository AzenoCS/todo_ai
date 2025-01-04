import uuid
from datetime import datetime

from .todo import Todo


def init_todo(name: str) -> Todo:
    """
    Initializes a to-do task with the provided name, generating a unique ID and
    capturing the creation timestamp. The task is assigned a "pending" status
    by default.

    :param name: The name of the task to initialize. Must not be empty.
    :type name: str
    :raises ValueError: If the provided task name is empty.
    :return: A Todo object containing the task's name, status, unique ID, and
        creation timestamp.
    :rtype: Todo
    """

    return Todo(name)
