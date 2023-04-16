''' Main program module '''

import json

from paths import Paths
from rpc_connection import RpcConnection

SERVER_HOST = 'localhost'
SERVER_PORT = 3333

def main() -> None:
    ''' Main client program entrypoint '''

    with open(Paths.INPUT_FILEPATH, encoding='utf-8') as posts_json_file:
        posts_file_text_content = posts_json_file.read()
        parsed_posts_json = json.loads(posts_file_text_content)

        rpc_connection = RpcConnection(SERVER_HOST, SERVER_PORT)
        rpc_connection.bind()

        rpc_connection.call_procedure('convert_posts_to_json', parsed_posts_json)

if __name__ == '__main__':
    main()
