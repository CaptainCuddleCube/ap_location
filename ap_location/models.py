from typing import List
from pydantic import BaseModel
from .utils import get_index, get_mac_addresses


class ScanObject(BaseModel):
    bssid: str
    rssi: int


class ApScanData(BaseModel):
    apscan_data: List[ScanObject]

    @property
    def index(self):
        return get_index(self.data)

    @property
    def data(self):
        return get_mac_addresses(self.dict())
