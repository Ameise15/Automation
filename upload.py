import cv2
import dropbox
import time
import random
start_time=time.time()
def take_snapshot():
    number=random.randint(0,1)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name='img'+str(number)+'.png'
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print('Snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token='sl.BEVKEemnpQq7tNzZUDqocNMuDTwSSU5tjt3t6nDWYCdcUJLHYd7wZdKd8m6sCqgF176_9aIP0cM3bbTckXRRvkWfyKa088d3iKjpXiLCsX_1uTmxaa28AOW0qcpoQjgyXjaJO-grmp34'
    file=img_name
    file_from=file
    file_to='/testfolder'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)
main()