import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)
        
def main():
        access_token = 'sl.Ardr3gvbmUttfq9f9AtELzTVRUUneb0TOtqrsdhk8GWZjnLRjyOol41vkAEUqkYEb-7RSp-Qw5h5btMPO_D_ZVSlNleSBbjy_iMT14oKWhS1-_wrsnsGpd__Xo-bVgxqTQZn9bs'
        transferData = TransferData(access_token)
        #C:/Users/HP/Pictures/Webcam Fun/handsome.jpg
        #https://www.dropbox.com/home/Wos
        file_from = input("Enter from")
        file_to = input("enter to")
        # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
        # API v2
        transferData.upload_file(file_from, file_to)
        print("file has been moved !!!")
main()
