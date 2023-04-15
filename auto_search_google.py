import webbrowser

def search_image(name):
    l = name.split()
    query = "%20".join(l)
    url = f"https://www.google.com/search?q={query}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961"
    webbrowser.open(url)

name_of_pictures = [
    input(f"enter the name of the {i} picture to be searched: ")
    for i in range(1, 7)
]

for name in name_of_pictures:
    search_image(name)
