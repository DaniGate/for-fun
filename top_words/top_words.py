from sklearn.feature_extraction.text import CountVectorizer

text = "The Mobile Data Analyst will play a key role in analyzing data and communicating insights that help the Mobile Marketing team and the Mobile Product team to take key business decisions regarding the mobile business. The Data Analyst will also work to ensure accurate data reporting. He or she will work in a fast collaborative, and rapidly changing environment and have a strong interest in mobile and business intelligence. Desired Skills and Experience Working with the various internal teams to deliver the different analytical needs by building both large systematic reports and small custom pieces Collaborating with Mobile product teams to support the decision process. Contribute to drafting LTV projections and new projection models for User Acquisition Build dashboards and custom reporting tools Analyze channel KPIs and use the data trends to develop insights and forecasts 2+ years of relevant experience working in mobile/digital analytics or in web-based businesses Strong analytical skills with ability to understand data and develop insights and recommendations Ideally have in depth statistical, machine learning and Have robust statistical significance testing, A/B testing, predictive analytics skills. Able to demonstrate hands on experience with data mining, clustering, segmentation Proficiency with one or more scripting languages and Google Analytics, Qlickview and other BI. Ability to collaborate with colleagues across different disciplines/locations Strong written and oral communication skills. Ability to work on multiple projects in parallel while meeting changing deadlines and priorities Fluent in English; other languages are a plus (e.g: Spanish, French, German or Italian)"
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
