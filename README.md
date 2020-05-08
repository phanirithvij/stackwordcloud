# stackwordcloud

Generates the wordcloud of a stackoverflow user's tags.

**Inspiration:** I saw a repo implementing this but I forgot what it was so I impleented my own.

**requirements (python 3)**

```
pip install wordcloud requests bs4
```

Run

```shell
python main.py stackoverflow_user_url
```

```py
# eg:
py main.py "https://stackoverflow.com/users/1144035/gordon-linoff"
```

It will make 20 requests at max change line 23 in gettags.py to configure

```py
if len(tagurls) == 0 or curr == 20: # here
```
