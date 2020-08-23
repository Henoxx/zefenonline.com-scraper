import requests
from bs4 import BeautifulSoup as bs
import json
import time
import os


FILE_NAME_BACKUP = 'artist_data_backup~temp.json'
FILE_NAME = 'artist_data.json'

links = []              # a list of links from the first parsing
text_with_url = {}      # anchor text  with href value dictionary
artist_with_url = {}    # artist name with url link dictionary

# a structured dict to write json format
structured_dict = {"artist":"artist_name","link":"link_name","music_link":[]}

# to get the content of a page
def get_soup(url):
    session = requests.Session()
    headers = { 'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
    r = session.get(url, headers=headers)
    soup = bs(r.content, 'html.parser')
    return soup

def statistics_info(file_name):
    fh = open(file_name, "r").read()
    j = json.loads(fh)
    total_music = []
    for i in j:
        music_link_list = i["music_link"]
        artist = i["artist"]
        print(f"{artist} = {len(music_link_list)}")
        for music_link in music_link_list:
            total_music.append(music_link)

    print(f"Total Artists= {len(j)}")
    print(f"Total Musics= {len(total_music)}")

main_url = "https://www.zefenonline.com/music/amharic/amharicmusic.html"

soup = get_soup(main_url)
footer = soup.find_all('footer')
if footer[6]:
    anchors = footer[6].find_all('a', href=True)
    for anchor in anchors:
        if anchor:
            links.append(anchor['href'])
            text_with_url.update({anchor.text:anchor['href']})

print(f"Total of {len(text_with_url)} links found")

for text in text_with_url:
    link = text_with_url[text]
    if '/music/artist/' in link:
        artist_with_url[text] = link

print(f"{len(artist_with_url)}/{len(text_with_url)} links contain '.../music/artist/..'")
print(f"We consider we have maybe found {len(artist_with_url)} artists.")


list_of_dict = []          # to store structured dict in a list 
music_link = []            # to store list of music links

for artist_name,artist_url in artist_with_url.items():
    structured_dict["artist"] = artist_name
    structured_dict["link"] = artist_url

    soup = get_soup(artist_url)
    iframe = soup.find('iframe', src=True)
    links_raw = (iframe['src'])
    links = links_raw.split('\n')

    for link in links:
        if '.mp3' in link:
            try:
                final_link = link.replace('|','')
            except:
                final_link = link
            music_link.append(final_link)

    structured_dict["music_link"] = music_link
    list_of_dict.append(structured_dict)
    
    # if fail in the middle... some datas are backupded
    fh = open(FILE_NAME_BACKUP,'a')
    j = json.dumps(structured_dict, indent=4)
    fh.write(j+", \n")

    print(f"{artist_name} written to file.")
    structured_dict = {}
    music_link = []

fh = open(FILE_NAME,'a')
j = json.dumps(list_of_dict, indent=4)
fh.write(j)

os.remove(FILE_NAME_BACKUP)        #if parsing is successfull delete the backup temp file

print("\n\nEverything parsed successfully!")
statistics_info(FILE_NAME)
print("You are awesome!")

