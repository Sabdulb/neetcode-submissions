class Twitter:

    def __init__(self):
        self.feed = deque()
        self.following = defaultdict(set)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed.appendleft([userId, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        c = 0
        ret = []
        for i in range(len(self.feed)):
            if c == 10:
                break
            if self.feed[i][0] == userId or self.feed[i][0] in self.followers[userId]:
                ret.append(self.feed[i][1])
                c += 1
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followeeId].add(followerId)
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following[followeeId]:
            self.following[followeeId].remove(followerId)
            self.followers[followerId].remove(followeeId)
