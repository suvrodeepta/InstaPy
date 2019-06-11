""" Quickstart script for InstaPy usage """

# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

# get an InstaPy session!
session = InstaPy(  username="", 
                    password="",
                    headless_browser=True,
                    multi_logs=True)

#with smart_run(session):
 #   """ Activity flow """
  #  # general settings
   # session.set_dont_include([])
#
 #   # activity
  #  session.like_by_tags(["writer","writerscommunity", "photography","bloggers"], amount=1000)
# let's go! :>
with smart_run(session):
    # general settings

    # session.set_relationship_bounds(enabled=True,
    # delimit_by_numbers=False, max_followers=12000, max_following=4500,
    # min_followers=35, min_following=35)
    # session.set_user_interact(amount=2, randomize=True, percentage=100,
    # media='Photo')
    # session.set_do_follow(enabled=True, percentage=00)
    session.set_do_like(enabled=True, percentage=100)
    # session.set_comments(["Cool", "Super!"])
    # session.set_do_comment(enabled=True, percentage=80)
    # session.set_user_interact(amount=2, randomize=True, percentage=100,
    # media='Photo')

    # activity

    # session.interact_user_followers(['user1', 'user2', 'user3'],
    # amount=8000, randomize=True)
    # session.follow_user_followers(['sneha.kaur55'],
    # amount=200, randomize=False, interact=True)
    # session.unfollow_users(amount=7500, nonFollowers=True, style="RANDOM",
    # unfollow_after=42*60*60, sleep_delay=3)
    session.like_by_tags(['','',''], amount=200)
    """ Joining Engagement Pods...
    """
    # photo_comments = ['Nice! @{}'
    #     'we like your profile! @{}',
    #     'Your feed is an great :thumbsup:',
    #     'Just incredible :open_mouth:',
    #     'Like your posts @{}',
    #     'Looks awesome @{}']
    # session.set_do_comment(enabled = True, percentage = 50)
    # session.set_comments(photo_comments, media = 'Photo')
    session.join_pods()
