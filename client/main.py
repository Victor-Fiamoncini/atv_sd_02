''' Main program module '''

from os.path import dirname, join

import json

from rpc_connection import RpcConnection

SERVER_HOST = 'localhost'
SERVER_PORT = 3333

POSTS_FILEPATH = join(dirname(__file__), 'input', 'posts.json')

def main() -> None:
    ''' Main client program entrypoint '''

    with open(POSTS_FILEPATH, encoding='utf-8') as posts_json_file:
        posts_file_text_content = posts_json_file.read()
        parsed_posts_json = json.loads(posts_file_text_content)

        rpc_connection = RpcConnection(SERVER_HOST, SERVER_PORT)
        rpc_connection.bind()
        rpc_connection.call_procedure('convert_posts_to_json', parsed_posts_json)

if __name__ == '__main__':
    main()
