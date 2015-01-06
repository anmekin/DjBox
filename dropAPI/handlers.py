__author__ = 'andrey'

import dropbox
from django.conf import settings

# def handle_uploaded_file(f):
#     print f.name
#     print f.__class__
#     #auth dropbox
#     APP_KEY = 'q860zezp5zss55a'
#     APP_SECRET = '0ekwbpg9czsu8l9'
#     #dropbox upload
#     with open('testt.txt', 'wb') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#     #dropbox return path to file
#     path = "/testt.txt"
#     return path

def upload_to_dropbox(path, f):
    client = dropbox.client.DropboxClient(settings.AUTH_TOKEN)
    response = client.put_file(path, f)
    # print 'uploaded: ', response
    # return response['path']
