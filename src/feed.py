import requests

def get_feed(organization, token):
  url = 'https://api.github.com/orgs/{}/events'.format(organization)
  headers = {'Authorization': token}
  return requests.get(url, headers = headers)