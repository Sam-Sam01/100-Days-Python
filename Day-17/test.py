class User:
    def __init__(self, userid, username):
        self.userid = userid
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("01", "Alice")
user_2 = User("02", "Bob")

user_1.follow(user_2)
for i in range(0,4):
    user_2.follow(user_1)
    print(user_1.followers)