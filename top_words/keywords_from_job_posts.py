filenames = [ "Job - Mobile Data Analyst eDreams.txt" ]
path = "C:/Users/Daneel/GitHub/for-fun/top_words"

text = ""
for fname in filenames:
    jobpost = open(path+"/"+fname,"r").read()
    jobpost = text.replace('\n',' ')
    text += " " + jobpost

top_words(text)
