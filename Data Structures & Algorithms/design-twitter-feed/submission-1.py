from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)
        self.timer = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = self.tweets.get(userId, []).copy()

        for followeeId in self.following.get(userId, set()):
            if followeeId != userId:
                all_tweets.extend(self.tweets.get(followeeId, []))

        heap = [(-time, tweetId) for time, tweetId in all_tweets]
        heapq.heapify(heap)
        
        k = 10
        res = []
        while heap and k > 0:
            _, tweetId = heapq.heappop(heap)
            res.append(tweetId)
            k -= 1
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
