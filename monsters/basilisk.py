defeated = False

# If player defeats basilisk, set defeated to true
def basilisk_defeated():
    global defeated
    defeated = True

def basilisk_encountered(inventory):
    print("""
You quickly reach for the door behind you, but the door has vanished, leaving no exit.
The gigantic basilisk, slithers across the room and opens its mouth with a hiss.
You slide under a desk, barely avoiding the deadly bite of the serpent.
You must act quickly if you wish to survive!
    """)

    return defeated


# **********************************
# Add a way for player to open the door again to exit at the end
