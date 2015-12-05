from sklearn.feature_extraction.text import CountVectorizer

fname = "Job - Mobile Data Analyst eDreams.txt"
text = ""
text = open(fname,"r").read()
text = text.replace('\n',' ')
words = []

for word in text.split():
    words.append(word)

vectorizer = CountVectorizer(stop_words='english',lowercase=True)
matrix = vectorizer.fit_transform(words)
freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vectorizer.vocabulary_.items()]

# Display the most frequent words (those appearing more than 3 times)
freq_words = sorted (freqs, key = lambda x: -x[1])
for w,f in freq_words:
    if f >= 3:
        print w,f
