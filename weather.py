from bs4 import BeautifulSoup
import requests


def main(URL):
    url = requests.get(URL)

    soup = BeautifulSoup(url.text, "lxml")

    soup_today = soup.select('.today-weather')[0]
    soup_tomorrow = soup.select('.tomorrow-weather')[0]
    output(soup_today)
    output(soup_tomorrow)

def output(soup):
    #天気
    weather_telop = soup.find("p",class_="weather-telop").get_text()

    #最高気温
    high_temp = soup.find("dd",class_="high-temp").get_text()

    #最低気温
    low_temp = soup.find("dd",class_="low-temp").get_text()

    #降水確率
    rain_probability = soup.select('.rain-probability > td')
    every_six = {}
    for i in range(4):
        time_from = 0+6*i
        time_to = 6+6*i
        time = "{:02}-{:02}".format(time_from,time_to)
        every_six[time] = rain_probability[i].text.strip()

    weather = []

    weather.append(weather_telop)
    weather.append(high_temp)
    weather.append(low_temp)
    weather.append(every_six['00-06'])
    weather.append(every_six['06-12'])
    weather.append(every_six['12-18'])
    weather.append(every_six['18-24'])

    print(weather)

    print(
        "天気："+ str(weather_telop) +"\n"
        "最高気温：" + str(high_temp) + "\n"
        "最低気温：" + str(low_temp) + "\n"
        "降水確率['00-06']：" + str(every_six['00-06']) + "\n"
        "降水確率['06-12']：" + str(every_six['06-12']) + "\n"
        "降水確率['12-18']：" + str(every_six['12-18']) + "\n"
        "降水確率['18-24']：" + str(every_six['18-24']) + "\n"
    )  



if __name__ == '__main__':
        URL="https://tenki.jp/forecast/1/4/2300/1202/"
        main(URL)

