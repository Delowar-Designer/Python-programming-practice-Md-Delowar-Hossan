# Explain the try and except block in python
# code Block 1
'''try:
    client_obj.get_url(url)
except(URLError, ValueError, SocketTimeout):
    client_obj.remove_url(url)
# code Block 2
try:
    client_obj.get_url(url)
    except(URLError, ValueError):
    client_obj.get_url(url)
    except SocketTimeout:
    client_obj.handle_url_timeout(url)
# code Block 3
try:
    f = open(filename)
except(FileNotFoundError, PermissionError):

# code Block 4
try:
    f = open(filename)
except OSError as e:
    if e.errno == errno.ENOENT:
        logger.error('File not found')
    elif e.errno == errno.EZCCES:
        logger.error('Permission denied')
    else:
        logger.error("Unexpected error: % d", e.errno)'''

# code Block 5
try:
    f = open('missing')
except OSError:
    print('lt faled')
except FileNotFoundError:
    print('File not found')