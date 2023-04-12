import speedtest

def return_bytes_by_mb(bytes):
    KB = 1024 # One Kilobyte is 1024 bytes
    MB = KB * 1024 # One MB is 1024 KB
    return float(bytes/MB)

def test_speed_net():
    st = speedtest.Speedtest()
    st.get_best_server()
    st.download()
    st.upload()
    def bytes_to_mb(bytes):
        KB = 1024 # One Kilobyte is 1024 bytes
        MB = KB * 1024 # One MB is 1024 KB
        return int(bytes/MB)
    download_speed = bytes_to_mb(st.download())
    uploaad_speed = bytes_to_mb(st.upload())
    res_dict = st.results.dict()
    #print(res_dict)
    #print("Your Download speed is", download_speed, "MB")
    info = res_dict
    print("Speed Test")
    return info