import requests
from flask import abort

def tracked_type(event):
  return event['type'] in ['IssueCommentEvent', 'IssuesEvent', 'PullRequestEvent', 'PullRequestReviewEvent',
    'PullRequestReviewCommentEvent', 'PushEvent']

def get_username(headers):
  url = 'https://api.github.com/user'
  r = requests.get(url, headers = headers)
  if r.status_code == requests.codes.ok:
    data = r.json()
    return data['login']
  else:
    return abort(r.status_code)

def get_feed(organization, token):
  headers = {'Authorization': token}
  username = get_username(headers)
  url = 'https://api.github.com/users/{}/events/orgs/{}'.format(username, organization)
  r = requests.get(url, headers = headers)
  if r.status_code == requests.codes.ok:
    return list(filter(lambda event: tracked_type(event), r.json()))
  else:
    return abort(r.status_code)