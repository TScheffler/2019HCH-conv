#!/usr/bin/python

# Author: Wladimir Sidorenko, Tatjana Scheffler

##################################################################
# Libraries
import json
from collections import defaultdict
import datetime


##################################################################
# Class
class Discussion:
    """Class representing discussion trees."""

    def __init__(self, root_id, discussion, tweets, users, times, parent_layers = 0):
        """Construct discussion tree from given root node."""
        # id of tweet
        self.id     = root_id
        # number of layers relative to the root of discussion
        self.parent_layers = parent_layers
        # number of layers following this tweet
        self.layers = 1
        # total number of replies and nested subreplies to this tweet
        self.total  = 1
        # indentation needed for printing, the bigger the level the more the
        # indentation level is
        self.offset = '~' * self.parent_layers
        # list of replies to this tweet
        self.children  = []
        # text of given message
        self.text = tweets[self.id] if self.id in tweets else  ""
        self.user = users[self.id] if self.id in users else  "unknown"
        self.time = str(times[self.id]) if self.id in times else  "unknown"
        # if we have seen tweet with this id in our read data, iterate over all
        # its replies. Create an own Discussion thread for each of the replies,
        # and gather these children in self.children list
        if root_id in discussion and discussion[root_id]:
            # discussion[root_id] is an adjacency list of all reply id's to
            # tweet with root_id
            for ch in discussion[self.id]:
                self.children.append(Discussion(ch, discussion, tweets, users, times, \
                                                self.parent_layers + 1))
            # the maximal number of layers of children + 1 is the number of layers
            # of current node
            self.layers += max([ch.layers for ch in self.children])
            # the total number of replies in given thread is this message +
            # number of all replies + number of all replies to replies
            self.total  += sum([ch.total for ch in self.children])

    def __str__(self):
        """String representation of object."""
        # string representation of a discussion thread is string representation
        # of root tweet + string representation of all its child discussions,
        if self.children :
            olist = [ str(len(self.offset)) + ' id=' + self.id + ' user=' + str(self.user) + " " + self.text.replace('\n',' ') ] + [str(ch) for ch in sorted(self.children, key=(lambda child: child.time)) ] 
        else :
            olist = [ str(len(self.offset)) + ' id=' + self.id + ' user=' + str(self.user) + " " + self.text.replace('\n',' ') ]
        return('\n'.join(olist))


##################################################################
# Add a tweet to an existing set of conversations

def add_tweet(tweet_id, inreply_id, tweet_text, tweet_user, tweet_time, tweets, users, times, discussion_roots, discussion): 
    if tweets[tweet_id]: # we've already seen this tweet
        return()
    if inreply_id == "None":
        inreply_id = ""
    tweets[tweet_id] = tweet_text
    users[tweet_id] = tweet_user
    times[tweet_id] = tweet_time     # save global time offset to sort sisters later 
    # if this tweet was a reply
    if inreply_id:
        # populate adjacency list of replies, i.e. tweet with `inreply_id'
        # will have a list of replies among which our current tweet will
        # also be present
        discussion[inreply_id].append(tweet_id)
        # if we find that current message is already stored as discussion
        # root, we'll remove it, since it's reply by itself
        if tweet_id in discussion_roots:
            discussion_roots.remove(tweet_id)
            # if we haven't seen the original tweet to which this tweet
            # replies, we'll store it as root of the discussion
        if inreply_id not in tweets:
            discussion_roots.add(inreply_id)
    else:
        # if a tweet doesn't have an inreply_id element, we'll assume it to
        # be root of a possible discussion thread
        discussion_roots.add(tweet_id)
    return()


##################################################################
# Construct a set of conversations based on a dictionary of tweets (eg read from JSON)

def make_discussions(tweet_dict):

    # dict of mappings between tweet ids and their text
    tweets      = defaultdict(str)
    # dict of mappings between tweet ids and their user id
    users  = defaultdict(str)
    # dict of mappings between tweet ids and their global time offset
    times  = defaultdict(str)
    # adjacency list with tweet ids as keys and all their respective replies as answers
    discussion  = defaultdict(list)
    # list of whole discussions
    discussion_threads  = []
    # set of tweets which started discussion
    discussion_roots = set([])

    for tweet in tweet_dict:
        add_tweet(tweet['id_str'], tweet['in_reply_to_status_id_str'], tweet['full_text'], tweet['user']['id_str'], tweet['created_at'], tweets, users, times, discussion_roots, discussion)
        
    # discussion_roots stores id's of tweets which start discussions
    for t_id in discussion_roots:
        # start descending on given root finding whole discussion
        discussion_threads.append(Discussion(t_id, discussion,tweets,users,times))
    # we don't need the set of discussion roots any more, since
    del discussion_roots

    # sort discussion threads according to total number of replies and subreplies,
    # with the thread having maximum number of reply-tweets going first
    discussion_threads.sort(key=lambda x: x.total, reverse = True)

    return(discussion_threads, discussion)

def print_discussions(discussion_threads):

    thread_id = 0

    for dt in discussion_threads:
        # skip singleton threads
        if dt.total == 1:
            continue
        # skip short threads for now (debug)
        #    if dt.total < 15:
        #        continue
        thread_id += 1
        print("#Thread " + str(thread_id) + ", size: " + str(dt.total) + ", max_depth: " + str(dt.layers)) 
        print(dt)

    return()


##################################################################
# Usage example

# # Main
#
# tweets = []
# 
# with open("cangertweets.json") as f:
#     for line in f:
#         tweet = json.loads(line)
#         tweets.append(tweet)
# 
# print(len(tweets))
# 
# discussion_threads, replies_dict = make_discussions(tweets)
# print(len(discussion_threads))
# print_discussions(discussion_threads)
