import dropbox
class TransferData():
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        for root,dirs,files in os.walk(file_from):
         dbx=dropbox.Dropbox(self.access_token)
         f=open(file_from,"rb")
         dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        for filename in files: local_path = os.path.join(root, filename):
            relative_path=os.path.relpath(local_path,file_from)
            dropbox.path=os.path.join(file_to,relative_path)
        with open(local_path,"rb") as f:
            dbx.files_upload(f.read(),dropbox_path,mode=WriteMode("overwrite"))
def main():
    access_token="sl.Apq6u48qBk4t-Gpv1Aqr_BdKDHq3STnQUdWgWFUWxmrL1HOKpuaoWAB9OheAC_q3B3B83lXo1XkCljG2YAMwlCcorzgJb2c_aIKnnV3ohcERiQb3osI878f_wdUt92bvamYnAFc"
    transferData=TransferData(access_token)
    file_from=input("Enter the file that you want to transfer:")
    file_to=input("Enter the full path to upload to the dropbox: ")
    transferData.upload_file(file_from,file_to)
    print("file has been succesfully moved")
