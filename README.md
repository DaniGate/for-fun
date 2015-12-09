## Content

A collection of different data science projects and tools and also some Python functions and classes that I programmed for fun:

* **[POI_identifier.ipynb](http://nbviewer.ipython.org/github/danigate/for-fun/blob/master/POI_identifier.ipynb)**:
  A classification algorithm that predict which Enron's executive are persons of interest (POI) and should be
  further investigated for possible fraud activities. I use some public information about their contract conditions
  like salary or bonus, the list of prosecuted Enron executives as positive examples and also a few features
  extracted from the public Enron email dataset.
* **Magic Star**: an algorithm to solve a 6-points [magic star](https://en.wikipedia.org/wiki/Magic_star) and print it
  on screen. Solutions to the 7- and 8-pointed magic stars are still under development.
* **Top words**: implementation of a simple TF-IDF analysis to extract the most common words from a text.
* **Top words in press**: Finding top words in presidential candidate Pablo Iglesias' articles on [elpais.com](http://elpais.com/autor/pablo_iglesias_turrion/a/)
* **Minuto decisivo**: Finding most used words by each politician during their final speech at the end of the [12-7-2015 presidential debate](http://www.atresplayer.com/television/noticias/debate-7d/2015/capitulo-8-debate-decisivo_2015120700347.html). First, the speeches were transcribed by Google Voice-to-Text software. Then, the most common words for each of them were found using top_words function (also in this repository). Finally, an infographic was created and published via [Twitter](https://twitter.com/Dani_GaTe/status/674334848975245312).
