def compute_bitrate(channels: int, sr: int, r: int):
    """
    :param channels: number of channels
    :param sr: sample rate [1/Hz]
    :param r: number of bits [bits/s]
    :return: bitrate [bits/s per channel]
    """
    assert channels > 0
    assert sr > 0
    return channels * sr * r
