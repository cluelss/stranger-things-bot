#!/user/bin/env python

VERSION = "0.1"

DECK_SIZE_MINIMUM = 40
STARTING_HAND_SIZE = 6
PACK_PRICE = 100
CHALLENGE_TIMEOUT = 30 #How long to wait for someone to accept a challenge
TURN_TIMEOUT = 300 #How long to wait for someone to do an action on their turn before they forfeit the match
TOKEN = '' #secret

DEFINITIONS = {
	"trade offer": "An offer to exchange different cards/characters for another card/character.",
	"wishlist": "Player's most wanted cards.",
	"ownings": "Each player's current owned characters.",
	"give away": "Removes card from your owned characters.",
}

#don't touch
matches = {}
