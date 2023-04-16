''' Main program module '''

from os import listdir, remove
from os.path import join

from rpyc.utils.server import ThreadedServer

from file_handler import FileHandler
from paths import Paths
from post_to_txt_thread_executor import PostToTxtThreadExecutor
from rpc_convert_posts_to_json_service import RpcConvertPostsToJsonService

SERVER_HOST = 'localhost'
SERVER_PORT = 3333

def remove_all_txt_files_from_output() -> None:
    ''' Removes all .txt files from output directory '''

    output_files = listdir(Paths.OUTPUT_DIRPATH)
    output_txt_files = filter(lambda file: file.endswith('.txt'), output_files)

    for txt_file in list(output_txt_files):
        path_to_file = join(Paths.OUTPUT_DIRPATH, txt_file)

        remove(path_to_file)

def main() -> None:
    ''' Main program entrypoint '''

    print(f'Starting server at {SERVER_HOST}:{SERVER_PORT}')

    file_handler = FileHandler()
    post_to_txt_thread_executor = PostToTxtThreadExecutor(file_handler)
    rpc_convert_posts_to_json_service = RpcConvertPostsToJsonService(post_to_txt_thread_executor)

    server = ThreadedServer(
        rpc_convert_posts_to_json_service,
        hostname=SERVER_HOST,
        port=SERVER_PORT
    )
    server.start()

if __name__ == '__main__':
    main()
