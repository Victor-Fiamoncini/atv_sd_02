''' This module defines the RpcConvertPostsToJsonService class '''

import rpyc

from convert_posts_to_json_service import ConvertPostsToJsonService
from mappers import map_post_dict_to_post_dto
from post_to_txt_thread_executor import PostToTxtThreadExecutor

@rpyc.service
class RpcConvertPostsToJsonService(ConvertPostsToJsonService, rpyc.Service):
    ''' RpcConvertPostsToJsonService class '''

    post_to_txt_thread_executor: PostToTxtThreadExecutor = None

    def __init__(self, post_to_txt_thread_executor: PostToTxtThreadExecutor) -> None:
        super().__init__()

        self.post_to_txt_thread_executor = post_to_txt_thread_executor

    @rpyc.exposed
    def convert_posts_to_json(self, *args) -> None:
        ''' Call convert posts to json concurrent routines '''

        posts_json = args[0][0]
        mapped_posts = map(map_post_dict_to_post_dto, posts_json)

        self.post_to_txt_thread_executor.posts = list(mapped_posts)

        for generated_filename in self.post_to_txt_thread_executor.execute_concurrently():
            print(f'File generated: {generated_filename}')
