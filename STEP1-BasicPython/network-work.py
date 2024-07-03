#socket
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(("data.pr4e.org", 80))
cmd= 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()

mysocket.send(cmd)

while True:
    data=mysocket.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysocket.close()


#urllib
import urllib.request, urllib.parse, urllib.error

filehandle= urllib.request.urlopen("http://data.pr4e.org/romeo.txt)
for line in filehandle:
    #print(line.decode().strip())
    words= line.decode().strip()
    for word in words:
        counts[word]= counts.get(word,0)+1
print(counts)

#webscraping
