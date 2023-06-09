import os
import logging
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, PicklePersistence, filters as Filters

from background import keep_alive
from handlers.baseHandlers import start, filters, estateTypeOptions, offerType, layout, district
from handlers.callbackHandlers import estateTypeOptionsCallback, EstateTypeFilter, offerTypeOptionsCallback, OfferTypeFilter, layoutOptionsCallback, LayoutFilter, districtOptionsCallback, DistrictFilter
from handlers.promptHandlers import pricePrompt, areaPrompt, moveInDatePrompt
from handlers.replyHandlers import priceReply, areaReply, moveInDateReply
from monitoring.monitoring import initializeMonitors, startMonitoring, stopMonitoring
from handlers.states import FILTERS, SETPRICE, SETAREA, SETMOVEINDATE, MONITORING
from ranges.priceRange import PriceRange
from ranges.areaRange import AreaRange
from ranges.moveInDateRange import MoveInDateRange

logging.basicConfig(
    # filename="logs.txt",
    # filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    level=logging.INFO
)

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            FILTERS: [
                    MessageHandler(Filters.Regex("Current filters"), filters),
                    MessageHandler(Filters.Regex("Estate type"), estateTypeOptions),
                    MessageHandler(Filters.Regex("Offer type"), offerType),
                    MessageHandler(Filters.Regex("Layout"), layout),
                    MessageHandler(Filters.Regex("Districts"), district),
                    MessageHandler(Filters.Regex(PriceRange.label()), pricePrompt),
                    MessageHandler(Filters.Regex(AreaRange.label()), areaPrompt),
                    MessageHandler(Filters.Regex(MoveInDateRange.label()), moveInDatePrompt),
                    MessageHandler(Filters.Regex("Start monitoring"), startMonitoring)
                    ],
            SETPRICE: [MessageHandler(Filters.TEXT, priceReply)],
            SETAREA: [MessageHandler(Filters.TEXT, areaReply)],
            SETMOVEINDATE: [MessageHandler(Filters.TEXT, moveInDateReply)],
            MONITORING: [MessageHandler(Filters.Regex("Stop monitoring"), stopMonitoring)]
        },
        fallbacks=[CommandHandler("cancel", start)],
        name="my_conversation",
        persistent=True
    )

if __name__ == '__main__':

    token = os.getenv("API_TOKEN")

    initializeMonitors(token)

    persistence = PicklePersistence(filepath="conversationbot")
    application = ApplicationBuilder().token(token).persistence(persistence).build()
    application.add_handler(CommandHandler("filters", filters))
    application.add_handler(CallbackQueryHandler(estateTypeOptionsCallback, EstateTypeFilter.label()))
    application.add_handler(CallbackQueryHandler(offerTypeOptionsCallback, OfferTypeFilter.label()))
    application.add_handler(CallbackQueryHandler(layoutOptionsCallback, LayoutFilter.label()))
    application.add_handler(CallbackQueryHandler(districtOptionsCallback, DistrictFilter.label()))
    application.add_handler(conv_handler)
    application.run_polling()

    keep_alive()
