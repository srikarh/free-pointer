import snscrape.modules.twitter as sntwitter
import pytesseract
import imutils
import string

picture_url = None
result = None
prev = "PREVIOUS_CODE"
# Using TwitterSearchScraper to scrape data
img = True
text = None
try:
    while True:
        for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:ChipotleTweets').get_items()):
            if not tweet.inReplyToTweetId and tweet.hashtags and ('ChipotleFreePointer' in tweet.hashtags):
                if tweet.media:
                    picture_url = tweet.media[0].fullUrl
                    break
                else:
                    img = False
                    text = tweet.rawContent
                    break
        if img:
            image = imutils.url_to_image(picture_url)
            text = pytesseract.image_to_string(image)
        text = text.translate({ord(c): None for c in string.whitespace})
        start, end = text.index("Text") + len("Text"), text.index("to888222")
        result = text[start:end].replace('$', '\$')
        if prev != result:
            break
except KeyboardInterrupt:
    pass


import os
RECIPIENT_NUMBER = "888222" 
os.system("osascript sendMessage.applescript " + RECIPIENT_NUMBER + " " + result)



