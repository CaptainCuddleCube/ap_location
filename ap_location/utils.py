from hashlib import md5


def get_mac_addresses(batch: dict):
    return [
        {"macAddress": scan["bssid"], "signalStrength": scan["rssi"]}
        for scan in batch["apscan_data"]
    ]


def get_index(data: dict, threshold=-82):
    """
    A default threshold of 82 has been chosen, since this is the ten percentile.
    Choose 85 if you want to target the 1 percentile.
    """
    good_APs = [i["macAddress"] for i in data if i["signalStrength"] > threshold]
    return md5("".join(good_APs).encode()).hexdigest()
