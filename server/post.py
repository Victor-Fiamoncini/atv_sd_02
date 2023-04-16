''' This module defines the Post DTO class '''

from dataclasses import dataclass

@dataclass(frozen=True)
class Post():
    ''' Post class '''

    id: int
    user_id: int
    title: str
    body: str
