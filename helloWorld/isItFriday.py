import tweepy
from privateFields import api
import logging
import time
import datetime

#Creates a logger for the bots actions
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
l = ['is', 'friday', 'the', '13th']
havePosted = False

#Datetime class that represents Pacific Standard Time and accounts for daylight savings time
class PST8PDT(datetime.tzinfo):

    def utcoffset(self, dt):
        return datetime.timedelta(hours=-8) + self.dst(dt)

    def dst(self, dt):
        d = datetime.datetime(dt.year, 3, 8)        #2nd Sunday in March
        self.dston = d + datetime.timedelta(days=6-d.weekday())
        d = datetime.datetime(dt.year, 11, 1)       #1st Sunday in Nov
        self.dstoff = d + datetime.timedelta(days=6-d.weekday())
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return datetime.timedelta(hours=1)
        else:
            return datetime.timedelta(0)

    def tzname(self, dt):
        return 'PST8PDT'

#sets the time tracker to track pacific standard time
dt = datetime.datetime.now(tz=PST8PDT())

#Schedules posts at a given hour.
def schedulePosts(hour) :
    if dt.hour == hour:
        if dt.day == 13 and dt.weekday() == 4 and havePosted == False:
            api.update_status("Yes.")
        else :
            api.update_status("No.")
        havePosted = True


def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if all(word in tweet.text.lower() for word in "is today friday the thirteenth"):
            logger.info(f"Answering to {tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                status="Please reach us via DM",
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

# def check_tweets() :

# def check_dms() :


def main() :
    since_id = 1
    while True:
        print(since_id)
        # since_id = check_mentions(api, ["When is it Friday the 13th"], since_id)
        schedulePosts(7)
        # check_mentions
        # check_tweets()
        # check_dms()
        logger.info("Waiting...")
        time.sleep(60)
