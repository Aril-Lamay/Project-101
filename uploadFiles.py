import os
from posixpath import relpath
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root,dirs,files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root,filename)
            
            realtive_path = os.path.relpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,realtive_path)

            with open(local_path,'rb') as f:
                dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

def main():
    access_token = 'sl.BIkEHYQtsN1OAH_u2cdxYpQwJ7pTjOvxWZ_qP_Fcluiho-aeLbrsdBizYWKDkZb9Nk0rnQYL8I1Cx8tqiFEOrzDEr9UWyDo_QlXYaCKmxPd0WuB2i5Su57I9fpcckIlBxQwlEK2LSAbK'
    transferData = TransferData(access_token)

    file_from = '/Users/arill/Documents/NewFolder/'
    file_to = '/Test/'

    transferData.upload_files(file_from, file_to)
    print("file has been moved")

main()
