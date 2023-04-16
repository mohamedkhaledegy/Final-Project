from geoip import geolite2

ip = "102.132.97.3"
locator = geolite2.lookup(ip)

if locator is None:
    print("Unknown")
else:
    print(locator)