#! /usr/bin/env python3
import requests
import json
from api.util import settings



class RedisLiveRequest(object):
    """docstring for Client."""
    def __init__(self,redis_live_host='192.168.99.100',redis_live_port=8888):
        super(RedisLiveRequest, self).__init__()
        self.url="http://%s:%s" % (redis_live_host,str(redis_live_port))
        print(self.url)


    def getResponse(self,uri,data):
        url=self.url+uri
        try:
            r=requests.get(url,params=data,timeout=3)
        except requests.exceptions.RequestException as e:
            print('request failed, please check redis live host IP and port')
            return None
        resp=r.json()
        return resp


    def getInfo(self,server,start=None,end=None):
        data={
        'server':server,
        'from':start,
        'to':end
        }
        return self.getResponse('/api/info',data)

    def getCommands(self,server,start=None,end=None):
        data={
        'server':server,
        'from':start,
        'to':end
        }
        return self.getResponse('/api/commands',data)

    def getSlowlog(self,server):
        data={
        'server':server,
        }
        return self.getResponse('/api/slowlog',data)

    def getMemory():
        pass

    def getStatus(self,server,start=None,end=None):
        data={
        'server':server,
        'from':start,
        'to':end
        }
        return self.getResponse('/api/status',data)




# if __name__=='__main__':
#     rlr=RedisLiveRequest()
#     print(rlr.getInfo("192.168.99.100:32768"))
#     print(rlr.getSlowlog("192.168.99.100:32768"))
#     print(rlr.getCommands("192.168.99.100:32768"))
#     print(rlr.getStatus("192.168.99.100:32768"))
