from instapy import InstaPy

# Replace with your Instagram credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Initialize InstaPy session
session = InstaPy(username=USERNAME, password=PASSWORD)

# Login
session.login()

# Prevent liking inappropriate content
session.set_dont_like(["naked", "murder", "nsfw"])

# Enable comments
session.set_do_comment(True, percentage=100)
session.set_comments(["Nice", "Amazing", "Super"])

# Enable follow
session.set_do_follow(enabled=True, percentage=100)

# Set user interaction
session.set_user_interact(
    amount=1,
    randomize=True,
    percentage=100
)

# Like posts by hashtags
session.like_by_tags(
    ["dance", "mercedes"],
    amount=10,
    interact=True
)

# End session
session.end()
