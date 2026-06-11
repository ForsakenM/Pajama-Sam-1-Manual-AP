# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#####################################################################

class PJS1StartShuffle(Choice):
    """
    Determines where the first three progression items (Child's Flashlight, Toy Mask, Signature Edition All-Metal Pajama Man Lunchbox)
    are placed during generation. These three items are required for the 'Sam's Bedroom - Open The Closet' location and to have access to the Land of Darkness.
    
    Sam's Bedroom: These items will be placed within the non-closet locations in Sam's Bedroom, preventing early BK chances. (Default)
    Early Multiworld: These items can be in any game in the multiworld, but are placed in early spheres to be acquired quickly.
    Completely Randomized: Placed anywhere in the multiworld. WARNING: This could leave you stuck in the first area of the game for a considerable amount of time!
    """
    display_name = "Sam's Bedroom Progression"
    option_sams_bedroom = 0
    option_early_multiworld = 1
    option_completely_randomized = 2
    default = 0

class PJS1RiverAccess(Choice):
    """
    Controls the placement of the Rope and the Wooden Board during generation. 
    Both of these items are required to access the majority of the River section of the Land of Darkness
    
    
    Vanilla: Rope and Board stay on their native event locations. (Default)
    Early Local: Placed in early spheres within your world.
    Early Multiworld: Can be anywhere in the multiworld, but placed in early spheres.
    Completely Randomized: Placed anywhere in the multiworld. WARNING: Access to the majority of the game is locked behind access to the River region!
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
    Without this, you cannot oil King the Minecart or access any checks inside the Mines.
    
    Vanilla: Oil Can stays on its native event location. (Default)
    Early Local: Placed in early spheres within your world.
    Early Multiworld: Can be anywhere in the multiworld, but placed in early spheres.
    Completely Randomized: Placed anywhere in the multiworld. WARNING: Access to a significant part of the game is locked behind having the Oil Can!
    """
    display_name = "Mine Access Shuffle"
    option_vanilla = 0
    option_early_local = 1
    option_early_multiworld = 2
    option_completely_randomized = 3
    default = 0

class PJS1DoorsOfKnowledge(Choice):
    """
    Controls the placement of the Hollow Log during generation 
    Together with the Oil Can, this is required to answer the 4th Trivia question and pass through the Doors of Knowledge into the rest of Darkness's House.
    
    Vanilla: Hollow Log will be placed at 'Get Stuck In Hollow Log' location. (Default)
    Early Local: Placed in early spheres within your world.
    Early Multiworld: Can be anywhere in the multiworld, but placed in early spheres.
    Completely Randomized: Placed anywhere in the multiworld. WARNING: Access to a large part of the game is locked behind the Doors of Knowledge!
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
    This is the key required to unlock the closet and win the game.
    WARNING: You cannot leave Darkness's Bedroom once entered. If you choose a non-default option, be thorough and make sure to save before entering.
    
    Vanilla: Correct Closet Key stays in its native event location. (Default)
    Local: The key is shuffled, but guaranteed to be somewhere inside your world.
    Multiworld: Placed anywhere in the multiworld.
    """
    display_name = "Closet Key Shuffle"
    option_vanilla = 0
    option_local = 1
    option_multiworld = 2
    default = 0


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    # We inject your new option into the dictionary here!
    options["starting_items_progression"] = PJS1StartShuffle
    options["river_access_shuffle"] = PJS1RiverAccess
    options["mine_access_shuffle"] = PJS1MineAccess
    options["doors_of_knowledge_shuffle"] = PJS1DoorsOfKnowledge
    options["closet_key_shuffle"] = PJS1VictoryKey

    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups