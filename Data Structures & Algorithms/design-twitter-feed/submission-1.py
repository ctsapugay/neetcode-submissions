class Twitter:

    def __init__(self):
        self.count = 0
        self.follow_map = defaultdict(set) 
        self.tweet_map = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.count, tweetId])
        self.count += 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        most_recent = []

        self.follow_map[userId].add(userId)
        for followeeId in self.follow_map[userId]:
            if followeeId in self.tweet_map:
                index = len(self.tweet_map[followeeId]) - 1
                count, tweetId = self.tweet_map[followeeId][index]
                most_recent.append([count, tweetId, followeeId, index - 1])
        heapq.heapify_max(most_recent)
        while most_recent and len(result) < 10:
            count, tweetId, followeeId, index = heapq.heappop_max(most_recent)
            result.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush_max(most_recent, [count, tweetId, followeeId, index - 1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)
        return