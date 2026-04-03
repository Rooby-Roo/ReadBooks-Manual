from typing import Optional
from BaseClasses import MultiWorld
from ..Locations import ManualLocation
from ..Items import ManualItem


# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: ManualItem) -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: ManualLocation) -> Optional[bool]:
    from ..Helpers import get_option_value
    name = location["name"]
    if name.startswith("Finish Chapter "):
        number = name[15:]
        if number.endswith(" (Bonus)"):
            number = number[:-8]
    elif name.startswith("Bookmark "):
        number = name[9:]
    else:
        return None
    if name.endswith(" (Bonus)") and not get_option_value(multiworld, player, "two_checks_per_chapter"):
        return False
    elif name.startswith("Bookmark ") and not get_option_value(multiworld, player, "enable_bookmark"):
        return False
    return int(number) <= get_option_value(multiworld, player, "total_chapters")
