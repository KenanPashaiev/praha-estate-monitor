from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters as Filters

from handlers.baseHandlers import *
from handlers.callbackHandlers import *
from handlers.promptHandlers import pricePrompt, areaPrompt, moveInDatePrompt
from handlers.replyHandlers import priceReply, areaReply, moveInDateReply
from monitoring.monitoring import *
from handlers.states import *
from ranges.priceRange import PriceRange
from ranges.areaRange import AreaRange
from ranges.moveInDateRange import MoveInDateRange
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
            SETMOVEINDATE: [MessageHandler(Filters.TEXT, moveInDateReply)],
            SETAREA: [MessageHandler(Filters.TEXT, areaReply)],
            MONITORING: [MessageHandler(Filters.Regex("Stop monitoring"), stopMonitoring)]
        },
        fallbacks=[CommandHandler("cancel", start)],
    )

if __name__ == '__main__':

    application = ApplicationBuilder().token('5672439696:AAHKr37nDhERNhQZQMjiPplFC_Z0fK5tRuo').build()
    
    application.add_handler(CommandHandler("filters", filters))
    
    application.add_handler(CallbackQueryHandler(estateTypeOptionsCallback, EstateTypeFilter.label()))
    application.add_handler(CallbackQueryHandler(offerTypeOptionsCallback, OfferTypeFilter.label()))
    application.add_handler(CallbackQueryHandler(layoutOptionsCallback, LayoutFilter.label()))
    application.add_handler(CallbackQueryHandler(districtOptionsCallback, DistrictFilter.label()))

    application.add_handler(conv_handler)

    application.run_polling()


