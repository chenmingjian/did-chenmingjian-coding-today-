#
# @lc app=leetcode.cn id=355 lang=python3
#
# [355] 设计推特
#

# @lc code=start
from collections import defaultdict
class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweet_map = defaultdict(list)
        self.user_follow_map = defaultdict(set)
        self.tweet_list = []
        self.tweet_user_map = defaultdict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.user_tweet_map[userId].append(tweetId)
        self.tweet_list.append(tweetId)
        self.tweet_user_map[tweetId] = userId
        
    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        ans = []
        for i in self.tweet_list[::-1]:
            if self.tweet_user_map[i] == userId or \
                self.tweet_user_map[i] in self.user_follow_map[userId]:
                ans.append(i)
            if len(ans) >= 10:
                break
        return ans

    
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followeeId in self.user_follow_map[followerId]:
            self.user_follow_map[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

