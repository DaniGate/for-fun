def top_words(textsample,lang='english'):

    from sklearn.feature_extraction.text import CountVectorizer
    if lang == 'english':
        vectorizer = CountVectorizer(stop_words=lang,lowercase=True)
    if lang == 'spanish':
        from nltk.corpus import stopwords
        spanish_stopwords = stopwords.words('spanish')
        vectorizer = CountVectorizer(encoding=u'utf-8',stop_words=spanish_stopwords,lowercase=True)

    words = textsample.split()
    matrix = vectorizer.fit_transform(words)
    freqs = [(word, matrix.getcol(idx).sum()) for word, idx in vectorizer.vocabulary_.items()]

    # Display the most frequent words (those appearing more than 3 times)
    freq_words = sorted (freqs, key = lambda x: -x[1])
    for w,f in freq_words:
        if f >= 3:
            print w,f

    return
