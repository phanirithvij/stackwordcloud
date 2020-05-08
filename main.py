import json
import sys

from wordcloud import WordCloud

from gettags import get_user_info


def makeImage(text):
    wc = WordCloud(max_words=1000, width=1920, height=1080)
    # wc = WordCloud(max_words=1000, width=3840, height=2160)
    # wc = WordCloud(background_color="white", max_words=1000, mask=alice_mask)
    # generate word cloud
    wc.generate_from_frequencies(text)
    wc.to_image().save("out.png")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage python main.py stackoverflow_user_url")
        exit(-1)
    user_url = sys.argv[1]
    get_user_info(user_url)
    with open("out.json") as infile:
        makeImage(json.load(infile))
    print("saved to out.png")
