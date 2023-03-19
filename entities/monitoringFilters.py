from filters.layoutFilter import LayoutFilter
from filters.districtFilter import DistrictFilter
from filters.offerTypeFilter import OfferTypeFilter
from filters.estateTypeFilter import EstateTypeFilter
from ranges.priceRange import PriceRange
from ranges.areaRange import AreaRange
from ranges.moveInDateRange import MoveInDateRange

class MonitoringFilters:
    def __init__(self, offerType = OfferTypeFilter(2), estateType = EstateTypeFilter(1), layout = LayoutFilter(0), district = DistrictFilter(0), priceRange = PriceRange(), areaRange = AreaRange(), moveInDateRange = MoveInDateRange()):
        self.offerType: OfferTypeFilter = offerType
        self.estateType: EstateTypeFilter = estateType
        self.layout: LayoutFilter = layout
        self.district: DistrictFilter = district
        self.priceRange: PriceRange = priceRange
        self.areaRange: AreaRange = areaRange
        self.moveInDateRange: MoveInDateRange = moveInDateRange
