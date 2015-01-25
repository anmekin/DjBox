__author__ = 'andrey'

import dropbox
from django.conf import settings

def upload_to_dropbox(path, f):
    client = dropbox.client.DropboxClient(settings.AUTH_TOKEN)
    response = client.put_file(path, f)
    # print 'uploaded: ', response
    # return response['path']
