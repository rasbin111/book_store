
def get_client_ip(info):

    meta = getattr(info.context, 'META', {})
    x_forwarded_for = meta.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        # Get the first IP in the list
        ip_address = x_forwarded_for.split(",")[0].strip()
    else:
        # For localhost
        ip_address = meta.get("REMOTE_ADDR")
    
    return ip_address

    