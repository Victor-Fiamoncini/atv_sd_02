''' Main program module '''

from rpc_connection import RpcConnection

SERVER_HOST = 'localhost'
SERVER_PORT = 3333

def main() -> None:
    ''' Main client program entrypoint '''

    rpc_connection = RpcConnection(SERVER_HOST, SERVER_PORT)
    rpc_connection.bind()

    rpc_connection.call_procedure('convert_posts_to_json', {'prop': 'value'})

if __name__ == '__main__':
    main()
