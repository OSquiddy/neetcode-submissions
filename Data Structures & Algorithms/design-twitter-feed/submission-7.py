class Twitter:

    def __init__(self):
        self.following = {}
        self.feed = []
        self.tweetCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if not self.following.get(userId):
            self.following[userId] = set()
            self.following[userId].add(userId)
        self.tweetCount += 1
        self.feed.append([self.tweetCount, tweetId, userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        print(self.following.get(userId))
        filteredFeed = list(filter(lambda x: x[2] in self.following.get(userId), self.feed))
        heapq.heapify_max(filteredFeed)
        while len(res) < 10 and filteredFeed:
            tweetCount, tweetId, userId = heapq.heappop_max(filteredFeed)
            res.append(tweetId)
            heapq.heapify_max(filteredFeed)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if self.following.get(followerId):
            self.following[followerId].add(followeeId)
        else:
            self.following[followerId] = set()
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if self.following.get(followerId) and followerId != followeeId:
            self.following[followerId].remove(followeeId)
        
