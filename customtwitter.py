"""
Custom Implementation of retrieval of tweets using the X (formerly Twitter) API provided by Alexander Vikhorev through Rapid API platform.
For more details, visit https://rapidapi.com/alexanderxbx/api/twitter-api45/

"""
import requests

class APIX:
    """
    Implements endpoints of the X (formerly Twitter) API provided by the API provider in Python using the requests module.

    ...

    Attributes
    ----------
    key : str
        The X - RapidAPI personal key of the user
    host : str
        The host URL of the X - RapidAPI (default is: twitter-api45.p.rapidapi.com)
    APIheaders : dict
        A key-value pair of API key and API host
    params : dict
        The parameters to be passed to access the endpoint.

    Methods
    -------
    getLatestReplies(id)
        Gets the Latest Replies of the tweet.

    getRetweets(id)
        Gets the list of users who retweeted the tweet

    searchTweet(keyword, search_type = "", cursor = None)
        Returns the search results for the specified query in Twitter Search

    getTweetInfo(id)
        Fetches tweet info by its ID

    getTweetThread(id, cursor = None)
        Get the basic tweet info and the replies to it

    getUserInfo(screenname, twitter_id = None)
        Returns information about user by the screenname.

    getUserTimeline(screenname, twitter_id = None, cursor = None)
        Returns user's latest tweets by its screenname.

    """
    key : str
    host : str
    APIheaders : dict
    params : dict

    def __init__(self, key, host = "twitter-api45.p.rapidapi.com"):
        """
        Initializes the APIX object

        Parameters
        ----------
        key : str
            The X - RapidAPI personal key of the user
        host : str 
            The host URL of the X - RapidAPI 
            (Default: twitter-api45.p.rapidapi.com)

        """
        self.key = key
        self.host = host
        self.APIheaders = {}
        self.APIheaders["X-RapidAPI-Key"] = key
        self.APIheaders["X-RapidAPI-Host"] = host

    def getLatestReplies(self, id : str):
        """
        Gets the Latest Replies of the tweet

        Parameters
        ----------
        id : str
            The tweet's unique id for which replies are to be fetched.

        Raises
        ------
        ValueError: 
            When tweet id is invalid

        Returns
        -------
        response in JSON format after successful access of the latest_replies endpoint.

        """
        try:
            id_int = int(id)
        except ValueError:
            raise ValueError("Invalid Tweet ID")
        self.params = {}
        self.params["id"] = id

        url = "https://twitter-api45.p.rapidapi.com/latest_replies.php"

        response = requests.get(url, headers = self.APIheaders, params = self.params)
        return response.json()
    
    def getRetweets(self, id : str):
        """
        Gets the list of users who retweeted the tweet

        Parameters
        ----------
        id : str
            The tweet's unique id for which the list of users that retweeted are to be fetched.

        Raises
        ------
        ValueError: 
            When tweet id is invalid

        Returns
        -------
        response in JSON format after successful access of the retweets endpoint.
        
        """
        try:
            id_int = int(id)
        except ValueError:
            raise ValueError("Invalid Tweet ID")
        self.params = {}
        self.params["id"] = id

        url = "https://twitter-api45.p.rapidapi.com/retweets.php"

        response = requests.get(url, headers = self.APIheaders, params = self.params)
        return response.json()
    
    def searchTweet(self, keyword : str, search_type : str = "", cursor : str = None):
        """
        Returns the search results for the specified query in Twitter Search

        Parameters
        ----------
        keyword : str
            Keyword that is to be searched
        search_type : str
            The type of search to be performed
            (Possible Values: "", "top", "latest", "media", "people", "lists")
            (Default : "")
        cursor : str
            A string that points to the next page of the result.
            (Default : None)

        Raises
        ------
        ValueError: 
            When search_type is invalid and does not belong to the values specified in the parameter.

        Returns
        -------
        response in JSON format after successful access of the search endpoint.
        
        """
        search_type = search_type.upper()
        types = set(["TOP", "LATEST", "MEDIA", "PEOPLE", "LISTS"])
        if search_type not in types and search_type != "":
            raise ValueError("Invalid search_type. The search_type does not belong to [TOP, LATEST, MEDIA, PEOPLE, LISTS] ")
        
        self.params = {}
        self.params["query"] = keyword
        if search_type in types:
            self.params["search_types"] = search_type
        if (cursor != None):
            self.params["cursor"] = cursor
        
        url = "https://twitter-api45.p.rapidapi.com/search.php"

        response = requests.get(url, headers = self.APIheaders, params = self.params)
        return response.json()
    
    def getTweetInfo(self, id : str):
        """
        Fetches tweet info by its ID.

        Parameters
        ----------
        id : str
            The tweet's unique id for which the information is to be fetched.

        Raises
        ------
        ValueError: 
            When tweet id is invalid

        Returns
        -------
        response in JSON format after successful access of the tweet endpoint.
        
        """
        try:
            id_int = int(id)
        except ValueError:
            raise ValueError("Invalid Tweet ID")
        self.params = {}
        self.params["id"] = id

        url = "https://twitter-api45.p.rapidapi.com/tweet.php"

        response = requests.get(url, headers = self.APIheaders, params = self.params)
        return response.json()
    
    def getTweetThread(self, id : str, cursor : str = None):
        """
        Get the basic tweet info and the replies to it.

        Parameters
        ----------
        id : str
            The tweet's unique id for which the information is to be fetched.
        cursor : str
            A string that points to the next page of the result.
            (Default : None)

        Raises
        ------
        ValueError: 
            When tweet id is invalid

        Returns
        -------
        response in JSON format after successful access of the tweet_thread endpoint.
        
        """
        try:
            id_int = int(id)
        except ValueError:
            raise ValueError("Invalid Tweet ID")
        self.params = {}
        self.params["id"] = id
        if (cursor != None):
            self.params["cursor"] = cursor

        url = "https://twitter-api45.p.rapidapi.com/tweet_thread.php"

        response = requests.get(url, headers = self.APIheaders, params = self.params)
        return response.json()
    
    def getUserInfo(self, screenname : str, twitter_id : str = None):
        """
        Returns information about user by the screenname.

        Parameters
        ----------
        screenname : str
            The screen name of the user for which the information is to be fetched.
        twitter_id : str
            The unique twiiter id of the user. This parameter overrides the screenname parameter when endpoint is called.
            (Default : None)

        Returns
        -------
        response in JSON format after successful access of the screenname endpoint.

        """
        self.params = {}
        self.params["screenname"] = screenname
        if (twitter_id != None):
            self.params["rest_id"] = twitter_id

        url = "https://twitter-api45.p.rapidapi.com/screenname.php"

        response = requests.get(url, headers = self.APIheaders, params = self.params)
        return response.json()
    
    def getUserTimeline(self, screenname : str, twitter_id : str = None, cursor : str = None):
        """
        Returns user's latest tweets by its screenname.

        Parameters
        ----------
        screenname : str
            The screen name of the user for which the information is to be fetched.
        twitter_id : str
            The unique twiiter id of the user. This parameter overrides the screenname parameter when endpoint is called.
            (Default : None)
        cursor : str
            A string that points to the next page of the result.
            (Default : None)

        Returns
        -------
        response in JSON format after successful access of the timeline endpoint.

        """
        self.params = {}
        self.params["screenname"] = screenname
        if (twitter_id != None):
            self.params["rest_id"] = twitter_id
        if (cursor != None):
            self.params["cursor"] = cursor

        url = "https://twitter-api45.p.rapidapi.com/timeline.php"

        response = requests.get(url, headers = self.APIheaders, params = self.params)
        return response.json()