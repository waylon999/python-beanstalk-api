import requests
import json

class BeanstalkAuth(object):
    _instance = None
    def __new__(cls, domain, username, password):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance
    
    def __init__(self, domain, username, password):
        self.domain = domain
        self.username = username
        self.password = password
        self.api_url = 'https://{0}.beanstalkapp.com/api/'.format(self.domain)
    
    @staticmethod
    def get_instance():
        if BeanstalkAuth._instance:
            return BeanstalkAuth._instance
        else:
            raise Exception("You need to setup this class first!")






class Base():
    
    def _do_request(self, url, method, data=None):
        auth = BeanstalkAuth.get_instance()
        request_url = auth.api_url+url
           
        r = getattr(requests, method)(request_url,
                                      data=json.dumps(data),
                                      auth=(auth.username, auth.password),
                                      headers={'content-type': 'application/json'})
        r.raise_for_status()
        return r.json
