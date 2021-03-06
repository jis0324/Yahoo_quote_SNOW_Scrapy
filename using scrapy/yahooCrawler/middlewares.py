import base64
import random
from yahooCrawler.settings import USER_AGENT_LIST
#from scrapy import log
# from yelpCrawler.settings import PROXIES
# from w3lib.http import basic_auth_header
# from scrapy.conf import settings



class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        # settings.get(USER_AGENT_LIST)
        # print settings.get(USER_AGENT_LIST)

        ua = random.choice(USER_AGENT_LIST)
        if ua:
            print('Changing user_agent: ' + ua)
            request.headers.setdefault('User-Agent', ua)
            # this is just to check which user agent is being used for request
            '''spider.log(
                u'User-Agent: {} {}'.format(request.headers.get('User-Agent'), request),
                level=log.DEBUG
            )'''
