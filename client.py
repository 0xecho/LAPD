import wget,requests,json,time

web_api = "http://127.0.0.1:5000/"
GET = "get/"
ADD = "add/"
def add(url):
    r=requests.get(web_api+ADD+"?url="+str(url))
    resp=json.loads(r.text)

    if resp['success']:
        print("Log: Added "+resp["url"])
    else:
        print("Log: Error adding url")

def get():
    r=requests.get(web_api+GET)
    resp=json.loads(r.text)
    if resp['success']:
        print("Log: Got url",resp["url"])
        return resp["url"]
    else:
        print("Log: Error getting urls : "+resp["error"])
    return "-1"

def download(url):
    wget.download(url)

while(True):
    print("Log: Trying to get files...")
    resp=get()
    if not resp == "-1":
        download(resp)
    else:
        print("Log: Got no files, Sleeping for 10 seconds")
        time.sleep(10)
