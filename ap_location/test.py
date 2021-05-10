import pytest
from fastapi.testclient import TestClient
from .main import app
from .models import ApScanData
from .utils import get_mac_addresses, get_index

client = TestClient(app)


@pytest.fixture
def data():
    return {
        "apscan_data": [
            {"rssi": -66, "bssid": "e8:1d:a8:68:a6:00"},
            {"rssi": -85, "bssid": "e8:1d:a8:68:a6:11"},
            {"rssi": -68, "bssid": "e8:1d:a8:68:a6:22"},
            {"rssi": -50, "bssid": "e8:1d:a8:68:a6:88"},
        ]
    }


@pytest.fixture
def mutated_data(data):
    data["apscan_data"][1]["rssi"] = -90
    return data


def test_mac_addresses(data):
    expected_result = [
        {"macAddress": "e8:1d:a8:68:a6:00", "signalStrength": -66},
        {"macAddress": "e8:1d:a8:68:a6:11", "signalStrength": -85},
        {"macAddress": "e8:1d:a8:68:a6:22", "signalStrength": -68},
        {"macAddress": "e8:1d:a8:68:a6:88", "signalStrength": -50},
    ]
    assert expected_result == get_mac_addresses(data)


def test_index(data, mutated_data):
    assert get_index(get_mac_addresses(data)) == get_index(
        get_mac_addresses(mutated_data)
    )


def test_base_class(data):
    ApScanData(**data)
    assert ApScanData(**data).index == get_index(get_mac_addresses(data))
