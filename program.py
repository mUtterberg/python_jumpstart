import requests
import bs4


def main():
    print_the_header()
    user_zip: str = input('What zipcode do you want the weather for? (#####)')
    html = get_html_from_web(user_zip)
    weather = parse_weather_from_html(html)
    print(weather)


def print_the_header():
    print('------------------')
    print('   WEATHER APP')
    print('------------------')
    print()


def get_html_from_web(zipcode):
    url = 'http://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    return response.text


def parse_weather_from_html(html):
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    weather = loc.strip() + ' has ' + condition.lower().strip() + ' weather right now, with a current temperature of ' + temp.strip() + scale.strip()

    return weather


if __name__ == '__main__':
    main()