from customtwitter import APIX
<<<<<<< HEAD
=======
import pandas as pd
>>>>>>> abc
import json

if __name__ == '__main__':
    APIkey = "05f9eec068mshcb0f7471140a0a8p1ca951jsn9d87189f621b"
    
    inst = APIX(key = APIkey)

    obj = inst.searchTweet("BTC", search_type = "top")

    # print(json.dumps(obj, indent = 4))
<<<<<<< HEAD
    with open("latest_tweet_replies.txt", "w+") as f:
        f.write(json.dumps(obj, indent = 4))
=======
    # with open("latest_tweet_replies.txt", "w+") as f:
    #     f.write(json.dumps(obj, indent = 4))
    json_string = json.dumps(obj)

    df = pd.read_json(json_string)
    print(df)
>>>>>>> abc
