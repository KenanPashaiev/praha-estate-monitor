import logging
import requests
from telegram import InputMediaPhoto
from entities.monitoringFilters import MonitoringFilters

from filters.layoutFilter import LayoutFilter
from operations.chatOperations import markEstateForChat, estateIsMarkedForChat

# api-endpoint
URL = "https://www.sreality.cz/api/ru/v2/estates"

async def fetchEstates(context, chatId, filters):
    PARAMS = filterToParams(filters)


    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)

    #return
    logging.log(logging.INFO, f"Fetching estates {r.url}")
    # extracting data in json format
    data = r.json()
    unmarkedItems = [item for item in data["_embedded"]["estates"] if not estateIsMarkedForChat(chatId, item["hash_id"])]
    logging.log(logging.INFO, str(len(data["_embedded"]["estates"])) + " found estates, unmarked: " + str(len(unmarkedItems)))
    for estate in unmarkedItems[:2]:
        await notifyChat(context, chatId, estate)


async def notifyChat(context, chatId, estate):
    logging.log(logging.INFO, str(estate["hash_id"]) + " estate notification was sent to " + str(chatId))
    text = getEstateDescription(estate)

    details = requests.get(url=URL+"/%(hash_id)s"% estate).json()
    images = details["_embedded"]["images"]

    media_group = []
    i = 0
    for image in images[:10]:#estate["_links"]["images"]:
        media_group.append(InputMediaPhoto(image["_links"]["self"]["href"], caption = text if i == 0 else '', parse_mode="markdown"))
        i += 1

    await context.bot.send_media_group(chat_id = chatId, media = media_group)
    markEstateForChat(chatId, estate["hash_id"])
    logging.log(logging.INFO, str(estate["hash_id"]) + " estate was marked for chat " + str(chatId))

def filterToParams(monitoringFilters: MonitoringFilters):
    return {
        "locality_country_id": 112,
        "locality_region_id": 10,
        "estate_age": 8,
        "category_main_cb": int(monitoringFilters.type),
        "category_type_cb": int(monitoringFilters.offerType),
        "category_sub_cb": monitoringFilters.layout.toParams(),
        "locality_district_id": monitoringFilters.district.toParams(),
        "czk_price_summary_order2": str(monitoringFilters.minPrice) + "|" + str(monitoringFilters.maxPrice),
        "usable_area": str(monitoringFilters.minArea) + "|" + str(monitoringFilters.maxArea),
    }

def layoutToParams(layout):
    layoutParams = ""
    if layout in LayoutFilter.L1_KT:
        layoutParams += "2|"
    if layout in LayoutFilter.L2_KT:
        layoutParams += "4|"
    if layout in LayoutFilter.L3_KT:
        layoutParams += "6|"
    if layout in LayoutFilter.L4_KT:
        layoutParams += "8|"
    if layout in LayoutFilter.L5_KT:
        layoutParams += "10|"
    if layout in LayoutFilter.L1_1:
        layoutParams += "3|"
    if layout in LayoutFilter.L2_1:
        layoutParams += "5|"
    if layout in LayoutFilter.L3_1:
        layoutParams += "7|"
    if layout in LayoutFilter.L4_1:
        layoutParams += "9|"
    if layout in LayoutFilter.L5_1:
        layoutParams += "11|"
    if layout in LayoutFilter.L6_1:
        layoutParams += "12|"

    return layoutParams[:-1] if len(layoutParams) > 0 else ""

def getEstateDescription(estate):
    text = ""
    text += "*%(name)s*\n"% estate
    text += "*%(locality)s*\n"% estate
    text += "*%(price)s CZK*\n"% estate
    text += "https://www.sreality.cz/ru/detail/-/-/-/-/%(hash_id)s\n"% estate
    return text