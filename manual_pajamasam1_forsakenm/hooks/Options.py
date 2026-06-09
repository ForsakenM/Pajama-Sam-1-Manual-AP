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


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    # We inject your new option into the dictionary here!
    options["starting_items_progression"] = PJS1StartShuffle
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups