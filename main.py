import requests
import bs4
import genanki
import re
import anki_deck_model
import text_to_speech
from selenium import webdriver
'''
Beautiful Soup is a Python library for pulling data out of HTML and XML files. 
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

genanki allows you to programatically generate decks in Python 3 for Anki.
https://github.com/kerrickstaley/genanki
'''

txt = "Welcome, to create an Anki Vocabulary deck please select a deck from "\
    "vocabulary.com\nGo to the page that contains the vocab list and copy the"\
    " URL of that page."\
    "\nIt should look like this http://vocabulary.com/lists/236361"

def main():    
    print(txt)
    again = True
    debug = False

    while again:
        isGoodUrl = False
        while not isGoodUrl:
            url = input("Input list URL: ")
    #       url = "http://vocabulary.com/lists/236361"  # fixed url for testing

            url = url.strip()
            pattern = re.compile(
                '(https?://)?(www\\.)?vocabulary\\.com/lists/\\d{4,8}')
            match = re.match(pattern, url)
            boolean = bool(match)
            if boolean:
                print("Is valid URL")
            isGoodUrl = boolean

        if 'http' not in url:
            url = 'http://' + url

        response = requests.get(url)
        print(response)
        if response.status_code == 200:
            print("Processing Wordlist!")
            words = []
            soup = bs4.BeautifulSoup(response.text, "html.parser")
            title = soup.select('title')[0].text
            title = title.replace(" : Vocabulary.com", "")  # remove suffix
            title = title.replace(" - Vocabulary List", "")
            print('Title of list: ' + title)
            for i, li in enumerate(soup.select('li')):
                words.append(li.text)

            lastIndex = words.index('Play the Challenge')
            words = words[21: lastIndex]
            length = len(words)
            word_list = [['', '', ''] for i in range(length)]
            for i in range(length):
                word_list[i][0:2] = words[i].split('\n')[1:3]
                word_list[i][2] = ''.join(words[i].split('\n')[4:6])

            for w in word_list:
                text_to_speech.get_audio(w[0])

            my_model = anki_deck_model.get_card_model_2()

            with open("style/style.css") as f:
                css = f.read()

            my_model.css = css

            my_deck = genanki.Deck(2059400110, title)

            for pack in word_list:
                word, definition, sentence = pack
                syn, ant, pos, trans, pic = "", "", "", "", ""
                source = title
                audio = "[sound:" + word + ".mp3]"

                my_deck.add_note(genanki.Note(
                    model=my_model,
                    fields=[word.upper(), definition, sentence, syn, ant, pos, trans, source, pic, audio]))
                    
            dirt = ["Vocabulary List", " ", "'", "-", ":", '"', ","]
            for d in dirt:
                title = title.replace(d, "")

            package = genanki.Package(my_deck)
            package.media_files = [r".\sound\\" + w[0] + ".mp3" for w in word_list]
            package.write_to_file(title + '.apkg')
            print("Deck has been created!")

        else:
            print("Something went wrong! Please try again or report an issue")
            if debug:
                print(response.content)

        answer = input("Do you want to create another deck? [y/N] ").lower()
        if answer != "y" and answer != "yes":
            again = False

        print("\n\n###########################\n\n")

if __name__ == "__main__":
    main()
