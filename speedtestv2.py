import matplotlib.pyplot as plt
import speedtest as sp
import time
list_download_speed = []
list_upload_speed = []
x = [1,2,3,4,5]
for i in range(5):
    st = sp.Speedtest()
    download_speed = round(st.download()/1000000,2)
    list_download_speed.append(download_speed)
    print(list_download_speed)
    upload_speed = round(st.upload()/1000000,2)
    list_upload_speed.append(upload_speed)
    print(list_upload_speed)
    time.sleep(60)
plt.title("Internet Speed")
plt.plot(x,list_download_speed,label="Download Speed")
plt.plot(x,list_upload_speed,label="Upload Speed")
plt.legend()
plt.show()  
