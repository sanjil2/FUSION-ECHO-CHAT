import ipinfo


def get_city():
    access_token = '4efb23bcbb88f1'
    handler = ipinfo.getHandler(access_token)
    ip_address = '110.224.86.73'
    details = handler.getDetails(ip_address)

    return details.city
