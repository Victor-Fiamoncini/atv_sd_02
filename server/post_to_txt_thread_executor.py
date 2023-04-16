''' This module defines the PostToTxtThreadExecutor class '''

from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

from typing import Generator, List

from file_handler import FileHandler
from mappers import map_post_dto_to_post_dict
from post import Post

class PostToTxtThreadExecutor:
    ''' PostToTxtThreadExecutor class '''

    file_handler: FileHandler = None
    _posts: List[Post] = []

    MAX_THREADS: int = 4

    def __init__(self, file_handler: FileHandler) -> None:
        self.file_handler = file_handler
        self._posts = []

    @property
    def posts(self):
        ''' posts getter '''

        return self._posts

    @posts.setter
    def posts(self, value):
        ''' posts setter '''

        self._posts = value

    def execute_concurrently(self) -> Generator:
        ''' Executes the following tasks (save_json_as_txt) concurrently '''

        if len(self._posts) == 0:
            return

        with ThreadPoolExecutor(max_workers=self.MAX_THREADS) as executor:
            save_post_to_txt_futures = [
                executor.submit(
                    self.file_handler.save_json_as_txt,
                    f'post-{post.id}.txt',
                    map_post_dto_to_post_dict(post)
                )
                for post in self._posts
            ]

            for future in futures.as_completed(save_post_to_txt_futures):
                exception = future.exception()

                yield exception if exception else future.result()
