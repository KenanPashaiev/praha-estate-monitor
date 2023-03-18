from datetime import date, time, datetime

from layoutFilter import LayoutFilter
from districtFilter import DistrictFilter
from offerTypeFilter import OfferTypeFilter
from propertyTypeFilter import PropertyTypeFilter

class MonitoringFilters:
    def __init__(self, offerType = OfferTypeFilter(2), type = PropertyTypeFilter(1), layout = LayoutFilter(0), district = DistrictFilter(0), moveInDateFrom = None, moveInDateTo = None, minPrice = 0, maxPrice = 10000000, minArea = 0, maxArea = 10000000):
        self.offerType = offerType
        self.type = type
        self.layout = layout
        self.district = district
        self.moveInDateFrom = moveInDateFrom
        self.moveInDateTo = moveInDateTo
        self.minPrice = minPrice
        self.maxPrice = maxPrice
        self.minArea = minArea
        self.maxArea = maxArea

    