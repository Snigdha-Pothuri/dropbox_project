import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        
def main():
    access_token="sl.ApaZIweNzSGx8WCGMOvklMJvJJhcl6j6yUVatp5n-x_92Cu-7hEx4VgZAdkrHo_kfyGtgl__8bF7-5-H3i02ZjA5XlyGJFuRnmpbj_rjLpvzgjH7UXOgj2WrQMgfQrFw-QCZaVY"
    transferData=TransferData(access_token)
    file_from=input("Enter the file that you want to transfer:")
    file_to=input("Enter the full path to upload to the dropbox: ")
    transferData.upload_file(file_from,file_to)
    print("file has been succesfully moved")
main()

     