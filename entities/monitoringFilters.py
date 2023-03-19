from datetime import date, time, datetime

from filters.layoutFilter import LayoutFilter
from filters.districtFilter import DistrictFilter
from filters.offerTypeFilter import OfferTypeFilter
from filters.estateTypeFilter import EstateTypeFilter
from ranges.priceRange import PriceRange
from ranges.areaRange import AreaRange
from ranges.moveInDateRange import MoveInDateRange

class MonitoringFilters:
    def __init__(self, offerType = OfferTypeFilter(2), type = EstateTypeFilter(1), layout = LayoutFilter(0), district = DistrictFilter(0), priceRange = PriceRange(), areaRange = AreaRange(), moveInDateRange = MoveInDateRange()):
        self.offerType = offerType
        self.type = type
        self.layout = layout
        self.district = district
        self.priceRange = priceRange
        self.areaRange = areaRange
        self.moveInDateRange = moveInDateRange
