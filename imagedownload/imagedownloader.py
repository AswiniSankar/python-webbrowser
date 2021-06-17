

import requests

res = requests.get("https://3.imimg.com/data3/WD/LE/MY-3040698/rose-flowers-250x250.jpg") #request is get from HTTP by using this url
#res.raise_for_status()  --> gives the statuss code from HTTP server
#print(res)              -->to print the status code
imgfile = open("flower.jpeg",'wb') #open a file in binary format and the name of the file also given
for chuck in res.iter_content():
  imgfile.write(chuck)             #write the file content 
print("image downloaded successfully..")
