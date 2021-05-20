#    Credts @Mrconfused
from geopy.geocoders import Nominatim
from telethon.tl import types

from userbot import catub
from ..helpers import reply_id
from ..core.managers import edit_or_reply

plugin_category = "extra"


@catub.cat_cmd(
    pattern="gps (.*)",
    command=("gps", plugin_category),
    info={
        "header": "To send the map of the given location.",
        "usage": "{tr}gps <place>",
        "examples": "{tr}gps Hyderabad",
    },
)
async def gps(event):
    "Map of the given location."
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, "`finding.....`")
    geolocator = Nominatim(user_agent="catuserbot")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await reply_to_id.reply(
            input_str, file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon))
        )
        await catevent.delete()
    else:
        await catevent.edit("`i coudn't find it`")
