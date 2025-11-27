from typing import List
import heapq
from collections import defaultdict, deque


"""
LeetCode Design Twitter

Problem from LeetCode: https://leetcode.com/problems/design-twitter/

Description:
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themselves. Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Example:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
"""

class Twitter:
    """
    Design a simplified version of Twitter where users can post tweets,
    follow/unfollow other users, and see the 10 most recent tweets in the
    user's news feed.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.time_stamp = 0
        self.user_map = {}


    class User:
        """Inner class to represent a Twitter user."""

        def __init__(self, user_id: int):
            self.id = user_id
            self.followed = set()
            self.tweets = []
            self.follow(user_id)

        def follow(self, user_id: int):
            """
            Follow a user.
            
            Args:
                user_id: The ID of the user to follow
            """
            self.followed.add(user_id)

        def unfollow(self, user_id: int):
            """
            Unfollow a user.
            
            Args:
                user_id: The ID of the user to unfollow
            """
            if user_id != self.id:
                self.followed.discard(user_id)

    def post_tweet(self, userId: int, tweetId: int) ->None:
        """
        Compose a new tweet.
        
        Args:
            userId: The user posting the tweet
            tweetId: The ID of the new tweet
        """
        if userId not in self.user_map:
            self.user_map[userId] = self.User(userId)
        self.user_map[userId].tweets.append((self.time_stamp, tweetId))
        self.time_stamp += 1

    def get_news_feed(self, userId: int) ->List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user
        followed or by the user themself.
        Tweets must be ordered from most recent to least recent.
        
        Uses optimized k-way merge: O(k log k) where k = number of followed users,
        instead of O(n log n) where n = total tweets from all followed users.
        
        Args:
            userId: The user requesting their news feed
            
        Returns:
            List[int]: The 10 most recent tweet IDs in the user's news feed
        """
        if userId not in self.user_map:
            return []
        
        followed_users = self.user_map[userId].followed
        heap = []
        
        # Only add the most recent tweet from each followed user to the heap
        for followed_id in followed_users:
            if followed_id in self.user_map:
                tweets = self.user_map[followed_id].tweets
                if tweets:
                    idx = len(tweets) - 1
                    time, tweet_id = tweets[idx]
                    # Store: (-time, tweet_id, user_id, tweet_index)
                    heapq.heappush(heap, (-time, tweet_id, followed_id, idx))
        
        result = []
        while heap and len(result) < 10:
            _, tweet_id, user_id, idx = heapq.heappop(heap)
            result.append(tweet_id)
            
            # If this user has more tweets, add the next most recent one
            if idx > 0:
                next_time, next_tweet_id = self.user_map[user_id].tweets[idx - 1]
                heapq.heappush(heap, (-next_time, next_tweet_id, user_id, idx - 1))
        
        return result

    def follow(self, followerId: int, followeeId: int) ->None:
        """
        Follower follows a followee.
        
        Args:
            followerId: The user who is following
            followeeId: The user being followed
        """
        if followerId not in self.user_map:
            self.user_map[followerId] = self.User(followerId)
        if followeeId not in self.user_map:
            self.user_map[followeeId] = self.User(followeeId)
        self.user_map[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) ->None:
        """
        Follower unfollows a followee.
        
        Args:
            followerId: The user who is unfollowing
            followeeId: The user being unfollowed
        """
        if followerId in self.user_map and followerId != followeeId:
            self.user_map[followerId].unfollow(followeeId)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    twitter = Twitter()
    
    # User 1 posts a new tweet (id = 5)
    twitter.post_tweet(1, 5)
    
    # User 1's news feed should return a list with 1 tweet id -> [5]
    print(twitter.get_news_feed(1))  # Expected: [5]
    
    # User 1 follows user 2
    twitter.follow(1, 2)
    
    # User 2 posts a new tweet (id = 6)
    twitter.post_tweet(2, 6)
    
    # User 1's news feed should return a list with 2 tweet ids -> [6, 5]
    # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5
    print(twitter.get_news_feed(1))  # Expected: [6, 5]
    
    # User 1 unfollows user 2
    twitter.unfollow(1, 2)
    
    # User 1's news feed should return a list with 1 tweet id -> [5]
    print(twitter.get_news_feed(1))  # Expected: [5]
