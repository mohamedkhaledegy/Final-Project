import psutil
import time



update_delay = 1 # in seconds

def get_size(bytes):
    """
    Returns size of bytes in a nice format
    """
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

# get the network I/O stats from psutil
io = psutil.net_io_counters()
# extract the total bytes sent and received
bytes_sent, bytes_recv = io.bytes_sent, io.bytes_recv



    # sleep for `UPDATE_DELAY` seconds

def calc_bandwidth(self , bytes_sent,bytes_recv,update_delay):
    # get the stats again
    io_2 = psutil.net_io_counters()
    # new - old stats gets us the speed
    us, ds = io_2.bytes_sent - bytes_sent, io_2.bytes_recv - bytes_recv

    # upload all bytes
    all_upload_captured = get_size(io_2.bytes_sent)
    # upload bytes by seconds
    upload_speed = get_size(us / update_delay)
    # download all bytes
    all_download_captured = get_size(io_2.bytes_recv)
    # donwload bytes by seconds
    download_speed = get_size(ds / update_delay)
    
    # print the total download/upload along with current speeds
    # print(f"Upload: {all_upload_captured}   "
    #       f", Download: {all_download_captured}   "
    #       f", Upload Speed: {upload_captured}/s   "
    #       f", Download Speed: {download_captured}/s      ", end="\r")
    # update the bytes_sent and bytes_recv for next iteration
    bytes_sent, bytes_recv = io_2.bytes_sent, io_2.bytes_recv
    respnse_dict = {
        'Upload':all_upload_captured,
        'Download':all_download_captured,
        'Upload Speed':upload_speed,
        'Download Speed':download_speed,
        'bytes_sent':bytes_sent,
        'bytes_recv':bytes_recv,
    }
    return respnse_dict
