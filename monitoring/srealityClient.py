import logging
import json
import requests
from telegram import Bot, InputMediaPhoto

from entities.monitoringFilters import MonitoringFilters
from operations.chatOperations import markEstateForChat, estateIsMarkedForChat

# api-endpoint
URL = "https://www.sreality.cz/api/en/v2/estates"

async def fetchEstates(bot, chatId, filters):
    PARAMS = filterToParams(filters)
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS, headers={'User-Agent': 'stupid-fix'})

    #return
    logging.log(logging.INFO, f"Fetching estates {r.url}")
    # extracting data in json format
    data = r.text
    
    data = json.loads(data)
    unmarkedItems = [item for item in data["_embedded"]["estates"] if not estateIsMarkedForChat(chatId, item["hash_id"])]
    logging.log(logging.INFO, str(len(data["_embedded"]["estates"])) + " found estates, unmarked: " + str(len(unmarkedItems)))
    for estate in unmarkedItems[:2]:
        await notifyChat(bot, chatId, estate)


async def notifyChat(bot: Bot, chatId, estate):
    estateIdStr = str(estate["hash_id"])
    logging.log(logging.INFO, estateIdStr + " estate notification was sent to " + str(chatId))

    details = requests.get(url=URL+f"/{estateIdStr}", headers={'User-Agent': 'stupid-fix'}).json()
    text = getEstateDescription(details, estateIdStr)
    images = details["_embedded"]["images"]

    media_group = []
    i = 0
    for image in images[:10]:#estate["_links"]["images"]:
        media_group.append(InputMediaPhoto(image["_links"]["self"]["href"], caption = text if i == 0 else '', parse_mode="markdown"))
        i += 1

    print("sho")
    await bot.send_media_group(chat_id = chatId, media = media_group)
    markEstateForChat(chatId, int(estateIdStr))
    logging.log(logging.INFO, estateIdStr + " estate was marked for chat " + str(chatId))

def filterToParams(monitoringFilters: MonitoringFilters):
    return {
        "locality_country_id": 112,
        "locality_region_id": 10,
        "estate_age": 8,
        "category_main_cb": int(monitoringFilters.estateType),
        "category_type_cb": int(monitoringFilters.offerType),
        "category_sub_cb": monitoringFilters.layout.toParams(),
        "locality_district_id": monitoringFilters.district.toParams(),
        "czk_price_summary_order2": monitoringFilters.priceRange.toParams(),
        "usable_area": monitoringFilters.areaRange.toParams(),
        "ready_date": monitoringFilters.moveInDateRange.toParams(),
    }

def getEstateDescription(estate, id):
    name = estate["name"]["value"]
    locality = estate["locality"]["value"]
    price = estate["price_czk"]["value"]
    moveInDate = [x for x in estate["items"] if x["name"] == "Move-in date"][0]["value"]

    text = ""
    text += f"*{name}* \n"
    text += f"Location: *{locality}* \n"
    text += f"Price: *{price}* CZK \n"
    text += f"Move in date: *{moveInDate}* \n"
    text += f"[Go to Sreality.cz](https://www.sreality.cz/ru/detail/-/-/-/-/{id} \n"
    return text

