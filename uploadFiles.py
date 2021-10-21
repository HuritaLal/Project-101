import os
import dropbox

class TransferData():
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):
            for name in files:
                path = os.path.join(root, name)
                print(path)

                relative_path = os.path.relpath(path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(path, "rb") as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)

def main():
    access_token = "sl.A6waerueYEWjdMBk0ouF_hJ4BlM3gWnXdJxsLCvTx8cXUw7givFt0BoKI7HWuUd8HnLojhPPlhXiJP6P1VlPeKBCrVoRxSzi1LbAbNEqNoT5MY7C0NJAU0xuAZ1nZ2gCp3VLTA0"
    transfer__data = TransferData(access_token)

    file_from = input("Enter The Path Of File To Be Taken:- ")
    file_to = input("Enter The Path Where The File Is To Be Dropped:- ")

    transfer__data.upload_file(file_from, file_to)

    print("Your file has been uploaded successfully")
    
main()