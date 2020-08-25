import tweepy
import logging
import os
def create_api():
    CONSUMER_KEY = "ca7JN8RWZTRUMsph2pp52p7ta"
    CONSUMER_SECRET = "OtATrbPyF06dOxJrtShEky2O2ion57rPvGq0gah6tTGbykeT4k"
    ACCESS_TOKEN = "1292096828226154501-2zfakwkyYRSSxPlJ7GOZmyL1BLd4Pv"
    ACCESS_TOKEN_SECRET = "6gyfbmfMW73bBh9VI7eZxulcYu8vVMqPEPg83reQ7eDF7"

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        print('Error creating API', exc_info=True)
        raise e
    print('API created')
    return api
import tweepy
import time
def emoji_follower_count(user):
    emoji_numbers = {0: "0️⃣", 1: "1️⃣", 2: "2️⃣", 3: "3️⃣",
                     4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}

    follower_count_list = [int(i) for i in str(user.followers_count)]

    emoji_followers = ''.join([emoji_numbers[k]
                               for k in follower_count_list if k in emoji_numbers.keys()])

    return emoji_followers # FOLLOWERS IN SMILEYS



def main():
    api = create_api()

    while True:
        # change to your own twitter_handle
        user = api.get_user('Bmuttika')

        if validate_follower_count(user) == emoji_follower_count(user):
            printf('you still have the same amount of followers, no update neccesary: {validate_follower_count(user) -> (emoji_follower_count(user)}')
        else:
            printf('your amount of followers has changed, updating twitter profile: {validate_follower_count(user) -> {emoji_follower_count(user)}')

            api.update_profile(name=f'veera424|{emoji_follower_count(user)} Followers')
      
        print("Waiting to refresh..")
        time.sleep(60)
        
