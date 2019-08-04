import requests
from . import settings
from . import exceptions

__all__ = ("LinkedinAPI", "ProfileAPI", "ShareAPI")


class LinkedinAPI(object):

    def __init__(self, token, api_url=settings.LINKEDIN_API_URL, api_version=settings.LINKEDIN_API_VERSION):
        self.token = token
        self.api_url = "%s%s" % (api_url, api_version)

    @property
    def headers(self):
        return {
            'X-Restli-Protocol-Version': '2.0.0',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer %s' % self.token
        }

    def _make_get(self, url):
        r = requests.get(url, headers=self.headers)
        if not r.ok:
            raise exceptions.BaseLinkedinException()
        return r.json()


class ProfileAPI(LinkedinAPI):
    def get_profile(self):
        url = "%s/me" % self.api_url
        try:
            return self._make_get(url)
        except exceptions.BaseLinkedinException as e:
            raise exceptions.ProfileException(e)


class ShareAPI(LinkedinAPI):
    def create(self):
        pass

    def retrieve(self):
        pass
