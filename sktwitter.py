import tweepy                              #imports tweepy package from loibrary

def get_api(cfg):                          #function defintion 
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  cfg = { 
    "consumer_key"        : "%%%%%%%%%%%%%%%%%%%%",
    "consumer_secret"     : "###################",
    "access_token"        : "$$$$$$$$$$$$$$$$$$$$",
    "access_token_secret" : "nnnnnnnnnnnnnnnnnnnn" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 

if __name__ == "__main__":
  main()
