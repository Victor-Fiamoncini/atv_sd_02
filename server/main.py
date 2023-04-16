''' Main program module '''

import rpyc

from rpyc.utils.server import ThreadedServer

SERVER_HOST = 'localhost'
SERVER_PORT = 3333

@rpyc.service
class ConvertPostsToJsonService(rpyc.Service):
    ''' TestService class '''

    @rpyc.exposed
    def convert_posts_to_json(self, *args) -> None:
        ''' foo '''

        print(args)

def main() -> None:
    ''' Main program entrypoint '''

    server = ThreadedServer(ConvertPostsToJsonService, hostname=SERVER_HOST, port=SERVER_PORT)
    server.start()

if __name__ == '__main__':
    main()
