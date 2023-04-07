import webbrowser

name_of_1st_picture = input("enter the name of the  1st picture to be searched: ")
name_of_2nd_picture = input("enter the name of the  2nd picture to be searched: ")
name_of_3rd_picture = input("enter the name of the  3rd picture to be searched: ")
name_of_4th_picture = input("enter the name of the  4th picture to be searched: ")
name_of_5th_picture = input("enter the name of the  5th picture to be searched: ")
name_of_6th_picture = input("enter the name of the  6th picture to be searched: ")


l = name_of_1st_picture.split()

if len(l) == 6:
    webbrowser.open(f"https://www.google.com/search?q={l[0]}%20{l[1]}%20{l[2]}%20{l[3]}%20{l[4]}%20{l[5]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(l) == 5:
    webbrowser.open(f"https://www.google.com/search?q={l[0]}%20{l[1]}%20{l[2]}%20{l[3]}%20{l[4]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(l) == 4:
    webbrowser.open(f"https://www.google.com/search?q={l[0]}%20{l[1]}%20{l[2]}%20{l[3]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(l) == 3:
    webbrowser.open(f"https://www.google.com/search?q={l[0]}%20{l[1]}%20{l[2]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(l) == 2:
    webbrowser.open(f"https://www.google.com/search?q={l[0]}%20{l[1]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(l) == 1:
    webbrowser.open(f"https://www.google.com/search?q={l[0]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")


a = name_of_2nd_picture.split()

if len(a) == 6:
    webbrowser.open(f"https://www.google.com/search?q={a[0]}%20{a[1]}%20{a[2]}%20{a[3]}%20{a[4]}%20{a[5]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(a) == 5:
    webbrowser.open(f"https://www.google.com/search?q={a[0]}%20{a[1]}%20{a[2]}%20{a[3]}%20{a[4]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(a) == 4:
    webbrowser.open(f"https://www.google.com/search?q={a[0]}%20{a[1]}%20{a[2]}%20{a[3]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(a) == 3:
    webbrowser.open(f"https://www.google.com/search?q={a[0]}%20{a[1]}%20{a[2]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(a) == 2:
    webbrowser.open(f"https://www.google.com/search?q={a[0]}%20{a[1]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(a) == 1:
    webbrowser.open(f"https://www.google.com/search?q={a[0]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")


b = name_of_3rd_picture.split()


if len(b) == 6:
    webbrowser.open(f"https://www.google.com/search?q={b[0]}%20{b[1]}%20{b[2]}%20{b[3]}%20{b[4]}%20{b[5]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(b) == 5:
    webbrowser.open(f"https://www.google.com/search?q={b[0]}%20{b[1]}%20{b[2]}%20{b[3]}%20{b[4]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(b) == 4:
    webbrowser.open(f"https://www.google.com/search?q={b[0]}%20{b[1]}%20{b[2]}%20{b[3]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(b) == 3:
    webbrowser.open(f"https://www.google.com/search?q={b[0]}%20{b[1]}%20{b[2]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(b) == 2:
    webbrowser.open(f"https://www.google.com/search?q={b[0]}%20{b[1]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(b) == 1:
    webbrowser.open(f"https://www.google.com/search?q={b[0]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")


c = name_of_4th_picture.split()

if len(c) == 6:
    webbrowser.open(f"https://www.google.com/search?q={c[0]}%20{c[1]}%20{c[2]}%20{c[3]}%20{c[4]}%20{c[5]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(c) == 5:
    webbrowser.open(f"https://www.google.com/search?q={c[0]}%20{c[1]}%20{c[2]}%20{c[3]}%20{c[4]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(c) == 4:
    webbrowser.open(f"https://www.google.com/search?q={c[0]}%20{c[1]}%20{c[2]}%20{c[3]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(c) == 3:
    webbrowser.open(f"https://www.google.com/search?q={c[0]}%20{c[1]}%20{c[2]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(c) == 2:
    webbrowser.open(f"https://www.google.com/search?q={c[0]}%20{c[1]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(c) == 1:
    webbrowser.open(f"https://www.google.com/search?q={c[0]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")


d = name_of_5th_picture.split()

if len(d) == 6:
    webbrowser.open(f"https://www.google.com/search?q={d[0]}%20{d[1]}%20{d[2]}%20{d[3]}%20{d[4]}%20{d[5]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(d) == 5:
    webbrowser.open(f"https://www.google.com/search?q={d[0]}%20{d[1]}%20{d[2]}%20{d[3]}%20{d[4]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(d) == 4:
    webbrowser.open(f"https://www.google.com/search?q={d[0]}%20{d[1]}%20{d[2]}%20{d[3]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(d) == 3:
    webbrowser.open(f"https://www.google.com/search?q={d[0]}%20{d[1]}%20{d[2]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(d) == 2:
    webbrowser.open(f"https://www.google.com/search?q={d[0]}%20{d[1]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(d) == 1:
    webbrowser.open(f"https://www.google.com/search?q={d[0]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")


e = name_of_6th_picture.split()
if len(e) == 6:
    webbrowser.open(f"https://www.google.com/search?q={e[0]}%20{e[1]}%20{e[2]}%20{e[3]}%20{e[4]}%20{e[5]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(e) == 5:
    webbrowser.open(f"https://www.google.com/search?q={e[0]}%20{e[1]}%20{e[2]}%20{e[3]}%20{e[4]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(e) == 4:
    webbrowser.open(f"https://www.google.com/search?q={e[0]}%20{e[1]}%20{e[2]}%20{e[3]}&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(e) == 3:
    webbrowser.open(f"https://www.google.com/search?q={e[0]}%20{e[1]}%20{e[2]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(e) == 2:
    webbrowser.open(f"https://www.google.com/search?q={e[0]}%20{e[1]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")

if len(e) == 1:
    webbrowser.open(f"https://www.google.com/search?q={e[0]}%20&tbm=isch&hl=en&tbs=il:cl&rlz=1C1FKPE_enIN999IN999&sa=X&ved=0CAAQ1vwEahcKEwjIlsr36K39AhUAAAAAHQAAAAAQAw&biw=1903&bih=961")
