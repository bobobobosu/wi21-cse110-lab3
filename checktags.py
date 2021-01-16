
with open("index.html") as fp:
    html = ""
    for line in fp:
        html += line
with open("textfile.txt") as fp:
    tags = ""
    for line in fp:
        if line.replace(" ","").replace("\n","") not in html:
            print(line)