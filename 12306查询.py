import requests
def city_name():
    """
    获取城市对应的城市编号
    :return: 城市名和城市编号对应的字典
    """
    url = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9140"
    city_code = requests.get(url)
    city_code_list = city_code.text.split("|")
    city_dict = {}
    for k,v in enumerate(city_code_list):
        if "@" in v:
            city_dict[city_code_list[k+1]] = city_code_list[k+2]
    return city_dict

def get_info(train_date,from_station,to_station):
    #将城市名转成对应的城市编号
    city_dict = city_name()
    from_station = city_dict[from_station]
    to_station = city_dict[to_station]


    #发送请求
    params = {
        "leftTicketDTO.train_date":train_date,
        "leftTicketDTO.from_station":from_station,
        "leftTicketDTO.to_station":to_station,
        "purpose_codes":"ADULT"
    }

    try:
        url = "https://kyfw.12306.cn/otn/leftTicket/queryZ"
        r = requests.get(url,params=params)
        info_text = r.json()["data"]["result"]
    except Exception as err:
        print(err)


    #获取响应内容并提取有效数据
    info_list = []
    for i in info_text:
        info_dict = {}
        train_info = i.split("|")
        info_dict["train_no"] = train_info[3]
        info_dict["start_time"] = train_info[8]
        info_dict["end_time"] = train_info[9]
        info_dict["interval_time"] = train_info[10]
        info_dict["second_seat"] = train_info[30]
        info_dict["frist_seat"] = train_info[31]
        info_dict["special_seat"] = train_info[32]
        info_list.append(info_dict)
    return info_list

if __name__ == "__main__":
    train_date = "2020-01-13"
    from_station = "北京"
    to_station = "哈尔滨西"
    info = get_info(train_date,from_station,to_station)
    print(str(info))