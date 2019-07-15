# Tools for processing Social Media

## General
[Think Python](http://greenteapress.com/wp/think-python-2e/)

[Unix for Poets - useful unix commands](https://web.stanford.edu/class/cs124/kwc-unix-for-poets.pdf)


## Raw Data Collection:

### Twitter
* tweepy/twython/python-twitter etc.
* [TAGS: collect with a Google spreadsheet](https://tags.hawksey.info/) (no programming)
* [Twarc: collect conversations](https://github.com/DocNow/twarc)

Adaptable python scripts:

* [Twitter extraction script](http://www.ling.uni-potsdam.de/~scheffler/twitter/)
* [German stop word list](https://github.com/TScheffler/TwitterCorpora/blob/master/twitter_stopwords_German.txt)

### Other social media

* [Amazon reviews](http://jmcauley.ucsd.edu/data/amazon/)
* [Wikipedia comments](https://figshare.com/articles/Wikipedia_Talk_Corpus/4264973) (from Wikipedia dump)
* [Reddit](https://archive.org/details/2015_reddit_comments_corpus) (2015 corpus or through the API)
* Blogs: RSS and BeautifulSoup
* [APIs for several channels](http://www.clips.ua.ac.be/pages/pattern-web) (CLiPS)



## Visualization:
[Treeverse](https://github.com/paulgb/Treeverse) - visualize Twitter conversation trees 

## Preprocessing:
### Language Identification: 
[langID](https://github.com/saffsd/langid.py)

### Tokenization/POS-Tagging
* [SpaCy](https://spacy.io/models)

English:

* [TweetNLP](http://www.cs.cmu.edu/~ark/TweetNLP/) (ark)
* [NLTK](https://www.nltk.org/)

German:

* [SoMaJo](https://github.com/tsproisl/SoMaJo)  (tokenization)
* [SoMeWeTa](https://github.com/tsproisl/SoMeWeTa)  (POS tagging)
* [German stop word list](https://github.com/TScheffler/TwitterCorpora/blob/master/twitter_stopwords_German.txt)  

## Sentiment:
* [SentiViz](https://www.csc2.ncsu.edu/faculty/healey/tweet_viz/tweet_app/) (NCSU)
* [OpinionFinder](http://mpqa.cs.pitt.edu/opinionfinder/) (Wiebe et al., 2005) 
* [SentiStrength](http://sentistrength.wlv.ac.uk/) (Thelwall et al., 2010)
* [SoCal](https://github.com/sfu-discourse-lab/SO-CAL) (SFU, Taboada et al.)

## Emoji:

* [Sentiment of Emoji](http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144296)
* [MoJiSem](http://www.aclweb.org/anthology/P17-3022) Varying linguistic purposes of emoji in (Twitter) context (ACL Student Research Workshop 2017) 
* [Emojitracker](http://emojitracker.com/)
* [Emojipedia](https://emojipedia.org/)
* [Sort lines based on emoji in them](https://github.com/TScheffler/TwitterCorpora/blob/master/get-emoji-tweets-fromtext.py)

## Other tools:
* [Cornell conversational analysis toolkit](http://convokit.cornell.edu/) 
* [Botometer](https://botometer.iuni.iu.edu/#!/)  (bot detection, but see recent discussion on whether this actually works/is a useful thing to do!)
