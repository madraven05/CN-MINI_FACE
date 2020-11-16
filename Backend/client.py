'''
Python code to define Client

CLIENT REQUEST MESSAGE:
------------------------
req_msg = {
    command: "LOGIN/LOGOUT/FETCH...",
    header_lines: {
        server_id: server_id,
        accept_encoding: 'utf-8',
        ... 
    },
    body: 'data'
}
'''

class Client():
    def __init__(self):
        pass