import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "PNKaqft17CZJC3mNzNe2ZjOnX",
    "consumer_secret"     : "wKZU64lF10ZerXmbV8ROMqdVxtaGbKfgB3C43Bn357RJVfQkR2",
    "access_token"        : "711529082832363520-tWk3ecKd5qLjhL6xBkmsQzOk6ResQIh",
    "access_token_secret" : "7WEN42IPXEhoKZ6QukPrl6m0M6TaRNlVinDhLIiyt5ccC" 
    }

  api = get_api(cfg)
  tweet = "Hello, world!"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()
