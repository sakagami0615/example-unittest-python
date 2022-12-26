def saturation(value, high, low):

    value_type = type(value)
    high_type = type(high)
    low_type = type(low)

    if value_type != high_type or value_type != low_type:
        msg = f'Argument variable mismatch ({value}, {high}, {low})'
        raise ValueError(msg)

    dst_value = value
    dst_value = max(dst_value, low)
    dst_value = min(dst_value, high)

    return dst_value
