# A-Vocabulary.com-Vocab-List-TO-Anki-Deck-Converter
# Attention: This is a Fork!
I changed some indices to help the script realize where the words start and end. I do not have a .exe file yet because there are still some bugs (see the list below).
The original creator mentioned that he could not create decks bigger than around 80 cards. I tried this fix with "The Vocabluary.com Top 100" (https://www.vocabulary.com/lists/52473) and it worked just fine.

## What is this

This is a a console program which i wrote in python. It can automatically create deck based on any list in vocabulary.com. I made this with the purpose to use it with the vocabgarbber in vocabulary.com. It's a powerful feature that grabs hard vocab from whatever text you enter. I use it to learn every word i dont know before i read something hard and i found it works pretty good for me in terms of increasing the amount i read and retaining the vocab in my head.

## How to use it

1. You need to login to a vocabulary.com account (free to sign up)
2. (OPTIONAL) Grab vocab using the <a href="https://www.vocabulary.com/lists/vocabgrabber">vocabgarbber</a> and click create list
3. Open the list that you want to add to anki and copy its url (make sure it's the actual page that shows the list, here's what i mean)
![ScreenShot](https://user-images.githubusercontent.com/23391683/60378704-111dad80-99ec-11e9-93c8-8c74a4727cc4.PNG)
4. run run.exe, when it asks you to enter the url, paste the url and then hit enter.
5. If the program run successfully, you shouldn't get any error message. The program will close it self when it's finished. Then you will find a loadable anki package. Double click it to load the deck like you normally do.

## Things you should know
1. You need to manually change the template and deck name
2. Sometimes if the list have more than 100 words, it can only load the first 100 words, i dont know how to solve this yet...
3. There is a build in pause for each word because of https://cloud.google.com/text-to-speech/quotas which says that you can only request 1000 words per minute.

<img src="https://img.icons8.com/wired/64/26e07f/dictionary.png" height="50"/>
<a href="https://icons8.com/icon/54640/dictionary">Green Dictionary icon by Icons8</a><br/>
<img src="https://img.icons8.com/wired/64/4a90e2/dictionary.png" height="50"/>
<a href="https://icons8.com/icon/54640/dictionary">Blue Dictionary icon by Icons8</a><br/>
<img src="https://img.icons8.com/wired/64/000000/swap.png" height="50"/>
<a href="https://icons8.com/icon/74155/swap">Swap icon by Icons8</a><br/>
<img src="https://img.icons8.com/carbon-copy/100/fa314a/image.png" height="50"/>
<a href="https://icons8.com/icon/N3wRcSUFuct_/image">Image icon by Icons8</a>

## How does this work

This program is fairly simple: first it scrap the word, definition and example from the url you entered, and put it into a 2 by 3 list. then it feeds the list to genanki. that's it. 

## Possible next goals/ideas
1. Use CSV files to create decks
2. Use Kindle DB file to create decks
___
Any question or comments are welcome

Good luck!


[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ChrisNiekler)
