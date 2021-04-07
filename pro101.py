import dropbox
import os

class TransferData :
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
         
        for root,dirs,files in os.walk(file_from) :
             relative_path = os.path.relpath(file_from,file_from)
             dropbox_path = os.path.join( file_to , relative_path)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = '1pwi4L6lSMgAAAAAAAAAAatJpoBSCT1cw9BvcHflo2zvYuk4BZZ6Ypi2QbuiMOve'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")  # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()