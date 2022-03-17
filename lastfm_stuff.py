import pylast
import mytokens


API_KEY = "907de34e8548928d5d6ba3cb943450dd"  # this is a sample key
API_SECRET = "57f475be7eff36ea3680af6db6144e37"

# In order to perform a write operation you need to authenticate yourself
username = "tequileros97"
password_hash = pylast.md5(mytokens.lastfm_pass)

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=username,
    password_hash=password_hash,
)

# Now you can use that object everywhere
track = network.get_track("Pink Floyd", "Fearless")
track.love()
track.add_tags(("awesome", "favorite"))

# Type help(pylast.LastFMNetwork) or help(pylast) in a Python interpreter
# to get more help about anything and see examples of how it works