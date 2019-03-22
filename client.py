import wget,requests,json

web_api = "http://127.0.0.1:5000/"
GET = "get/"
ADD = "add/"
def add(url):
    r=requests.get(web_api+ADD+"?url="+str(url))
    resp=json.loads(r.text)

    if resp['success']:
        print("added "+resp["url"])
    else:
        print("error adding url")

def get():
    r=requests.get(web_api+GET)
    resp=json.loads(r.text)
    if resp['success']:
        print("got",resp["url"])
        return resp["url"]
    else:
        print("error getting data : "+resp["error"])
    return "-1"

def download(url):
    wget.download(url)

resp=get()
if not resp == "-1":
    download(resp)
