# Object classes from AP that represent different types of options that you can create
from Options import Choice, Range, OptionGroup

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any

class PJS1StartShuffle(Choice):
    """
    Determines where the first three progression items (Child's Flashlight, Toy Mask, Signature Edition All-Metal Pajama Man Lunchbox)
    are placed during generation.
    
    Sam's Bedroom: These items will be placed within the non-closet locations in Sam's Bedroom, preventing early BK chances. (Default)
    Early Multiworld: These items can be in any game in the multiworld, but are placed in early spheres to be acquired quickly.
    Completely Randomized: Placed anywhere in the multiworld.
    """
    display_name = "Sam's Bedroom Progression"
    option_sams_bedroom = 0
    option_early_multiworld = 1
    option_completely_randomized = 2
    default = 0

class PJS1RiverAccess(Choice):
    """
    Controls the placement of the Rope and the Wooden Board during generation. 
    
    Vanilla: Rope and Board stay on their native event locations. (Default)
    Early Local: Placed in early spheres within your world.
    Early Multiworld: Can be anywhere in the multiworld, but placed in early spheres.
    Completely Randomized: Placed anywhere in the multiworld.
    """
    display_name = "River Access Shuffle"
    option_vanilla = 0
    option_early_local = 1
    option_early_multiworld = 2
    option_completely_randomized = 3
    default = 0

class PJS1MineAccess(Choice):
    """
    Controls the placement of the Oil Can during generation.
    
    Vanilla: Oil Can stays on its native event location. (Default)
    Early Local: Placed in early spheres within your world.
    Early Multiworld: Can be anywhere in the multiworld, but placed in early spheres.
    Completely Randomized: Placed anywhere in the multiworld.
    """
    display_name = "Mine Access Shuffle"
    option_vanilla = 0
    option_early_local = 1
    option_early_multiworld = 2
    option_completely_randomized = 3
    default = 0

class PJS1DoorsOfKnowledge(Choice):
    """
    Controls the placement of the Hollow Log during generation.
    
    Vanilla: Hollow Log will be placed at 'Get Stuck In Hollow Log' location. (Default)
    Early Local: Placed in early spheres within your world.
    Early Multiworld: Can be anywhere in the multiworld, but placed in early spheres.
    Completely Randomized: Placed anywhere in the multiworld.
    """
    display_name = "Doors of Knowledge Shuffle"
    option_vanilla = 0
    option_early_local = 1
    option_early_multiworld = 2
    option_completely_randomized = 3
    default = 0

class PJS1VictoryKey(Choice):
    """
    Controls the placement of the Correct Closet Key in Darkness's Bedroom. 
    
    Vanilla: Correct Closet Key stays in its native event location. (Default)
    Local: The key is shuffled, but guaranteed to be somewhere inside your world.
    Multiworld: Placed anywhere in the multiworld.
    """
    display_name = "Closet Key Shuffle"
    option_vanilla = 0
    option_local = 1
    option_multiworld = 2
    default = 0

class PJS1CheeseAndCrackers(Choice):
    """
    Controls the inclusion of the Cheese & Crackers (Tic-Tac-Toe) minigame locations.
    
    Disabled: No Cheese & Crackers locations are included in the pool.
    Play Only: Only the 3 locations for playing a match (3x3, 5x5, 7x7) are included. (Default)
    Play and Win: Includes both the 3 playing locations and 3 locations for winning the matches.
    """
    display_name = "Cheese & Crackers"
    option_disabled = 0
    option_play_only = 1
    option_play_and_win = 2
    default = 1

class PJS1NuggetsLevels(Range):
    """
    Controls the inclusion and magnitude of the Nuggets (Snake) minigame locations.
    
    0: Disabled. No Nuggets locations are included in the pool. (Default)
    1-15: Partial Game. Includes only the specified number of levels as locations.
    """
    display_name = "Nuggets Levels"
    range_start = 0
    range_end = 15
    default = 0

class PJS1Potions(Choice):
    """
    Controls the inclusion of the Potion minigame locations.

    Disabled: There will be no Potion locations included in the pool. (Default)
    Enabled: All 17 Potion locations will be added to the pool.
    """
    display_name = "Potions"
    option_disabled = 0
    option_enabled = 1
    default = 0


# This is called before any manual options are defined
def before_options_defined(options: dict[str, Type[Choice]]) -> dict[str, Type[Choice]]:
    options["starting_items_progression"] = PJS1StartShuffle
    options["river_access_shuffle"] = PJS1RiverAccess
    options["mine_access_shuffle"] = PJS1MineAccess
    options["doors_of_knowledge_shuffle"] = PJS1DoorsOfKnowledge
    options["closet_key_shuffle"] = PJS1VictoryKey
    options["cheese_and_crackers_logic"] = PJS1CheeseAndCrackers
    options["nuggets_levels"] = PJS1NuggetsLevels
    options["potions"] = PJS1Potions
    return options

def after_options_defined(options: Any):
    pass

# We hook into here to cleanly section out and name the option groups for the user interface!
def before_option_groups_created(groups: dict[str, list[Type[Choice]]]) -> dict[str, list[Type[Choice]]]:
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    # 1. Define your custom Item Shuffle category using class references
    item_shuffle_group = OptionGroup("Item Shuffle Options", [
        PJS1StartShuffle,
        PJS1RiverAccess,
        PJS1MineAccess,
        PJS1DoorsOfKnowledge,
        PJS1VictoryKey
    ])
    
    # 2. Define your custom Minigame category using class references
    minigames_group = OptionGroup("Minigame Options", [
        PJS1CheeseAndCrackers,
        PJS1NuggetsLevels,
        PJS1Potions
    ])

    # 3. Find where "Item & Location Options" is sitting (usually at index 1)
    # If found, we inject our groups right in front of it.
    target_idx = len(groups)
    for idx, group in enumerate(groups):
        if "Location" in group.name or "Item" in group.name:
            target_idx = idx
            break

    # 4. Insert our custom groups exactly above the Item/Location block
    groups.insert(target_idx, item_shuffle_group)
    groups.insert(target_idx + 1, minigames_group)
    
    return groups