from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ConversationHandler, filters as Filters

from handlers.baseHandlers import *
from handlers.callbackHandlers import *
from monitoring.monitoring import *

# logging.basicConfig(
#     # filename="logs.txt",
#     # filemode='a',
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%H:%M:%S',
#     level=logging.INFO
# )

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            FILTERS: [MessageHandler(Filters.Regex("Current filters"), filters),
                    MessageHandler(Filters.Regex("Estate type"), type),
                    MessageHandler(Filters.Regex("Offer type"), offerType),
                    MessageHandler(Filters.Regex("Layout"), layout),
                    MessageHandler(Filters.Regex("Districts"), district),
                    MessageHandler(Filters.Regex("Move in dates"), moveInDate),
                    MessageHandler(Filters.Regex("Price range"), price),
                    MessageHandler(Filters.Regex("Area"), area),
                    MessageHandler(Filters.Regex("Start monitoring"), startMonitoring)],
            SETPRICE: [MessageHandler(Filters.TEXT, setPrice)],
            SETMOVEINDATE: [MessageHandler(Filters.TEXT, setMoveInDate)],
            SETAREA: [MessageHandler(Filters.TEXT, setArea)],
            MONITORING: [MessageHandler(Filters.Regex("Stop monitoring"), stopMonitoring)]
        },
        fallbacks=[CommandHandler("cancel", start)],
    )

if __name__ == '__main__':

    application = ApplicationBuilder().token('5672439696:AAHhpGEv1tzGY8gFAI9vbsG2sdUwJml0ga0').build()
    
    application.add_handler(CommandHandler("filters", filters))
    
    application.add_handler(CallbackQueryHandler(estateTypeSelectCallback, EstateTypeFilter.label()))
    application.add_handler(CallbackQueryHandler(offerTypeSelectCallback, OfferTypeFilter.label()))
    application.add_handler(CallbackQueryHandler(layoutSelectCallback, LayoutFilter.label()))
    application.add_handler(CallbackQueryHandler(districtSelectCallback, DistrictFilter.label()))

    application.add_handler(conv_handler)

    application.run_polling()


