import pwd

def get_user():
  all_user = {}
  for user in pwd.getpwall():
    all_user[user[0]] = all_user[user[2]] = user
  return all_user

def userinfo(uid):
  return get_user()[uid]

print userinfo(0)
print userinfo('root')
