'''
Python code to define Server

SERVER RESPONSE MESSAGE:
------------------------
response_msg = {
    status_line: {
        protocol: 'TCP/UDP',
        status_code: 200/301...
    },
    header_lines: {
        date: date,
        accept_ranges: bytes,
        content_length: content_length,
        keep_alive: {
            timeout: 10,
            max: 100
        },
        connection: 'keep-alive'
    }
    data: data
}
'''

class Server():
    def __init__(self):
        pass