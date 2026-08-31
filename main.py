# This is a sample Python script for downloading files from site.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tqdm import tqdm           # Downloading files with processbar
from time import sleep
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import requests

import os

from fake_useragent import UserAgent as UAgent

from bs4 import BeautifulSoup as BeaS


"""
 For parsing HTML code, but for parsing process using we two modules (+ request). This one has imported. 
"""
MUSIC_DIR = 'C:\\Users\\Mick\\Music'
HOST = 'http://eaglesky.ru'
URL = 'http://eaglesky.ru/songs'
AUTHORS = {
    'http://eaglesky.ru/songs-kiselyev.htm',
    'http://eaglesky.ru/songs-pimakina.htm',
    'http://eaglesky.ru/songs-komashilova.htm',
    'http://eaglesky.ru/songs-vabishevich.htm',
    'http://eaglesky.ru/songs-camp.htm',
    'http://eaglesky.ru/songs-other.htm',
}
SONGSLIST = {
    'http://eaglesky.ru/songs/i_love_him/01%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/02%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/03%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/04%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/05%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/06%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/07%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/08%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/09%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/10%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/11%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/12%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/13%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/14%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/15%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/16%20i_love_him-kiselyev.mp3',
    'http://eaglesky.ru/songs/i_love_him/17%20i_love_him-kiselyev.mp3',

    'http://eaglesky.ru/songs/pimakina/01-christ_has_found_me.mp3',
    'http://eaglesky.ru/songs/pimakina/02-white_bird.mp3',
    'http://eaglesky.ru/songs/pimakina/03-knock.mp3',
    'http://eaglesky.ru/songs/pimakina/04-in_presence_of_jesus.mp3',
    'http://eaglesky.ru/songs/pimakina/05-here_is_a_man.mp3',
    'http://eaglesky.ru/songs/pimakina/06-home.mp3',
    'http://eaglesky.ru/songs/pimakina/07-follow_jesus.mp3',
    'http://eaglesky.ru/songs/pimakina/08-seed_of_God.mp3',
    'http://eaglesky.ru/songs/pimakina/09-trust_in_the_god.mp3',
    'http://eaglesky.ru/songs/pimakina/10-oh_my_lord.mp3',
    'http://eaglesky.ru/songs/pimakina/11-judge_not.mp3',
    'http://eaglesky.ru/songs/pimakina/12-mercy_above_court.mp3',
    'http://eaglesky.ru/songs/pimakina/13-be_manly.mp3',
    'http://eaglesky.ru/songs/pimakina/13-be_manly.mp3',
    'http://eaglesky.ru/songs/pimakina/15-Alliluya.mp3',

    'http://eaglesky.ru/songs/living_book/11-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/04-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/16-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/02-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/12-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/20-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/06-living_book.mp3',
    'http://eaglesky.ru/songs/pimakina/coming.mp3',
    'http://eaglesky.ru/songs/living_book/19-living_book.mp3',
    'http://eaglesky.ru/songs/pimakina/song-for-god.mp3',
    'http://eaglesky.ru/songs/pimakina/he-came.mp3',
    'http://eaglesky.ru/songs/living_book/21-living_book.mp3',

    'http://eaglesky.ru/songs/Vabishevich/01-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/02-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/03-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/04-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/05-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/06-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/07-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/08-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/09-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/10-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/11-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/12-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/13-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/14-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/15-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/16-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/17-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/18-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/19-Vabishevich.mp3',
    'http://eaglesky.ru/songs/Vabishevich/20-Vabishevich.mp3',


    'http://eaglesky.ru/songs/camp2004/01-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/02-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/03-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/04-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/05-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/06-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/07-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/08-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/09-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/10-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/11-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/12-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/13-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/14-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/15-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/16-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/17-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/18-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/19-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/20-camp2004.mp3',
    'http://eaglesky.ru/songs/camp2004/21-camp2004.mp3',

    'http://eaglesky.ru/songs/fire_of_pilgrim/01-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/02-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/03-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/04-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/05-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/06-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/07-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/08-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/09-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/10-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/11-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/12-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/13-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/14-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/15-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/16-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/17-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/18-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/19-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/20-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/21-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/22-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/23-fire_of_pilgrim.mp3',
    'http://eaglesky.ru/songs/fire_of_pilgrim/24-fire_of_pilgrim.mp3',

    'http://eaglesky.ru/songs/songs_of_bride/01%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/02%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/03%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/04%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/05%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/06%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/07%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/08%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/09%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/10%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/11%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/12%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/13%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/14%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/15%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/16%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/17%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/18%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/19%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/20%20songs_of_the_Bride.mp3',
    'http://eaglesky.ru/songs/songs_of_bride/21%20songs_of_the_Bride.mp3',

    'http://eaglesky.ru/songs/living_book/01-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/02-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/03-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/04-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/05-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/06-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/07-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/08-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/09-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/10-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/11-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/12-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/13-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/14-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/15-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/16-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/17-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/18-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/19-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/20-living_book.mp3',
    'http://eaglesky.ru/songs/living_book/21-living_book.mp3',
}


def get_html(url, params=''):
    headrs = {
    "Accept": 'text/html, image/avif, image/webp, image/apng, image/svg+xml, */* ; q=0.8',
    "Accept-Encoding": 'gzip, deflate, br',
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": '1',
    "Set-Fetch-Dest": 'dokument',
    "Set-Fetch-Mode": 'navigate',
    "Set-Fetch-User": '1?',
    "Set-Fetch-Site": 'None',
    "User-Agent": UAgent().random,
    "Referer": HOST,
    "Accept-Language": "en-US,en;q=0.9"
    }
    session = requests.Session()
    session.headers.update(headrs)

    try:
        result_request = session.get(url, params=params)

        # Перевіряємо статус код відповіді
        result_request.raise_for_status()  # Це викликає HTTPError для статус кодів 4xx/5xx

        return result_request.text  # Повертаємо текст відповіді

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 403:
            print("Помилка 403: Спробуйте змінити User-Agent або перевірити Referer.", headrs, " Зараз так ")
            exit()
        else:
            print(f"HTTP помилка: {e.response.status_code}")
        return None

    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")
        return None



def get_html_urllib(url, params=''):
    headrs = {
    "Accept": 'text/html, image/avif, image/webp, image/apng, image/svg+xml, */* ; q=0.8',
    "Accept-Encoding": 'gzip, deflate, br',
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": '1',
    "Set-Fetch-Dest": 'dokument',
    "Set-Fetch-Mode": 'navigate',
    "Set-Fetch-User": '1?',
    "Set-Fetch-Site": 'None',
        "User-Agent": UAgent().random,
        "Referer": 'http://eaglesky.ru/',
        "Accept-Language": "en-US,en;q=0.9"
    }
    # Якщо є параметри, їх потрібно додати до URL
    if params:
        url = f"{url}?{params}"

    req = Request(url, headers=headrs)

    try:
        with urlopen(req) as response:
            page = response.read()
            return page
    except HTTPError as e:
        if e.code == 403:
            print("Error 403: Доступ заборонено. User-Agent або перевірити Referer.", headrs, " Зараз так ")
            exit()
        else:
            print(f"HTTP Error: {e.code}")
        return None

    except URLError as e:
        print(f"Connection error: {e.reason}")
        return None
    # print(page)

# Отримуємо контент
def get_content(html):
    if html is None:
        # Якщо контент пустий або його не отримано
        print('HTML code is empty!')
    else:
        # Якщо контент отримано то отримуємо вміст таблиці в HTML
        print(html)
        soup = BeaS(html, "html.parser")
        table = soup.find('table')
        if table is None:
            print('Table is not find!')
            return

        # отриману таблицю розбираємо
        print(table)
        rows = table.findAll('tr')
        result = {}
        for tr in rows:
            tds = [td.text.replace('\xa0', ' ') for td in tr.find_all('td')]
            result[tds[0]] = {
                'album': tds[1],
                'link': tds[2]
            }
        print(result)

def create_dir_for_album(dir_name):
    # full_path = os.getcwd()+'\\'+dir_name
    # Вказуємо шлях до каталогу
    full_path = os.path.join(MUSIC_DIR, dir_name)  # Використовуємо os.path.join для кросплатформності
    if not os.path.exists(full_path):
        os.makedirs(full_path)  # Створюємо директорію, включаючи всі проміжні
        print(f"Директорію {full_path} створено.")
    else:
        print(f"Директорія {full_path} вже існує.")
    return full_path

def create_nested_playlists(root_folder, playlist_name="playlist.m3u"):
    if not os.path.exists(root_folder):
        print(f"Помилка: папка '{root_folder}' не існує.")
        return

    all_global_tracks = []
    local_playlists_count = 0

    # os.walk сканує головну папку та всі її підпапки
    for dirpath, dirnames, filenames in os.walk(root_folder):
        # Відбираємо лише MP3-файли у поточній папці
        mp3_files = [f for f in filenames if f.lower().endswith(".mp3")]

        if not mp3_files:
            continue

        # 1. Створення локального плейліста для поточного підкаталогу
        local_playlist_path = os.path.join(dirpath, playlist_name)
        with open(local_playlist_path, "w", encoding="utf-8") as local_file:
            local_file.write("#EXTM3U\n")
            for track in mp3_files:
                local_file.write(f"{track}\n")

        local_playlists_count += 1

        # 2. Збір треків для загального плейліста
        for track in mp3_files:
            # Отримуємо повний шлях до файлу
            full_path = os.path.join(dirpath, track)
            # Робимо шлях відносним до головної папки root_folder
            relative_path = os.path.relpath(full_path, root_folder)
            all_global_tracks.append(relative_path)

    # 3. Створення одного загального плейліста в корені
    if all_global_tracks:
        global_playlist_path = os.path.join(root_folder, f"ALL_{playlist_name}")
        with open(global_playlist_path, "w", encoding="utf-8") as global_file:
            global_file.write("#EXTM3U\n")
            for relative_track in all_global_tracks:
                global_file.write(f"{relative_track}\n")

        print("--- Успішно виконано! ---")
        print(f"Створено локальних плейлістів у папках: {local_playlists_count}")
        print(f"Створено один загальний плейліст: {global_playlist_path}")
        print(f"Всього додано треків у загальний список: {len(all_global_tracks)}")
    else:
        print("MP3-файлів у вказаному каталозі та його підпапках не знайдено.")

def file_download(url):
    # Чи існує файл за посиланням
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Перевіряємо на статус 200
        line = url.split('/')
        album_name = line[-2]  # Отримуємо назву альбому
        file_name = line[-1].replace('%20', '')  # Отримуємо назву файлу
        print(f"Завантаження {file_name} з альбому {album_name}...")

        # Створюємо директорію для альбому
        album_path = create_dir_for_album(album_name)

        # Завантажуємо файл
        file_path = os.path.join(album_path, file_name)
        with open(file_path, "wb") as handle:
            for data in tqdm(response.iter_content(chunk_size=1024), unit="kB"):
                handle.write(data)

        print(f"Файл {file_name} успішно завантажено в {album_path}.")

    except requests.exceptions.HTTPError as e:
        print(f"HTTP помилка: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Помилка запиту: {e}")
    except Exception as e:
        print(f"Сталася помилка: {e}")


if __name__ == '__main__':
    # Набридло шукати метод обходу 403 для цього статичного сайту, тому зробив списком
    # get_html_urllib(URL)
    # get_content(html_text)
    # Тут я вирішив спочатку налагодити доунлоад зі списка, який заданий вручну
    counter = len(SONGSLIST)  # Цей лічильник виключно для генерування псевдовипадкової паузи між початком скачування
    for song in SONGSLIST:

        sleep(0.05*counter)
        file_download(song)

    create_nested_playlists(MUSIC_DIR)
