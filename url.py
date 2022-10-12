from urllib.request import urlopen

# Open URL.
r = urlopen("https://www.github.com")
with open("url-data.html", "wb") as f:
    f.write(r.read())
# Close to freeing resources
r.close()