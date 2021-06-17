
import requests
res = requests.get("https://youtu.be/SXPvx4Jf-io")
f = open("senorita.mp4",'wb')
for data in res.iter_content():
  f.write(data)
print("successfully downloaded...")
