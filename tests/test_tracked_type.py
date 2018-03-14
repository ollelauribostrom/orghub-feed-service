from src.feed import tracked_type

def test_tracked_type():
  event_a = { 'type': 'IssueCommentEvent'}
  event_b = { 'type': 'IssuesEvent'}
  event_c = { 'type': 'PullRequestEvent'}
  event_d = { 'type': 'PullRequestReviewEvent'}
  event_e = { 'type': 'PullRequestReviewCommentEvent'}
  event_f = { 'type': 'PushEvent'}
  event_g = { 'type': 'MemberEvent'}
  event_h = { }
  assert tracked_type(event_a) == True
  assert tracked_type(event_b) == True
  assert tracked_type(event_c) == True
  assert tracked_type(event_d) == True
  assert tracked_type(event_e) == True
  assert tracked_type(event_f) == True
  assert tracked_type(event_g) == False
  assert tracked_type(event_h) == False

