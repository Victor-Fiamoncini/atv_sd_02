''' Main program module '''

from os import listdir, remove
from os.path import join

import rpyc

from file_handler import FileHandler
from mappers import map_post_dict_to_post_dto
from paths import Paths
from post_to_txt_thread_executor import PostToTxtThreadExecutor
from rpyc.utils.server import ThreadedServer

SERVER_HOST = 'localhost'
SERVER_PORT = 3333

def remove_all_txt_files_from_output() -> None:
    ''' Removes all .txt files from output directory '''

    output_files = listdir(Paths.OUTPUT_DIRPATH)
    output_txt_files = filter(lambda file: file.endswith('.txt'), output_files)

    for txt_file in list(output_txt_files):
        path_to_file = join(Paths.OUTPUT_DIRPATH, txt_file)

        remove(path_to_file)

@rpyc.service
class ConvertPostsToJsonService(rpyc.Service):
    ''' TestService class '''

    file_handler: FileHandler = None

    def __init__(self, file_handler: FileHandler) -> None:
        super().__init__()

        self.file_handler = file_handler

    @rpyc.exposed
    def convert_posts_to_json(self, *args) -> None:
        ''' Call convert posts to json concurrent routines '''

        posts_json = args[0][0]

        mapped_posts = map(map_post_dict_to_post_dto, posts_json)
        post_to_txt_thread_executor = PostToTxtThreadExecutor(self.file_handler, list(mapped_posts))

        for generated_filename in post_to_txt_thread_executor.execute_concurrently():
            print(f'File generated: {generated_filename}')

def main() -> None:
    ''' Main program entrypoint '''

    print(f'Starting server at {SERVER_HOST}:{SERVER_PORT}')

    file_handler = FileHandler()
    convert_posts_to_json_service = ConvertPostsToJsonService(file_handler)

    server = ThreadedServer(convert_posts_to_json_service, hostname=SERVER_HOST, port=SERVER_PORT)
    server.start()

if __name__ == '__main__':
    main()
