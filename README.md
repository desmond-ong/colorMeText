# colorMeText
---

This repository contains an interactive text-visualiation tool, colorMeText. Users can input text (an email; a poem, etc) and have the text highlighted based on certain features. It is live here: 

http://cocolab.stanford.edu/cgi-bin/colorMeText/


This is still a work in progress, and we have a long list of bugs/issues and desired features! We plan to expand the program by adding more features, more visualizations, more complex analyses (e.g. adding syntactic information).

Initially programmed by Desmond Ong, Justine Kao, and Greg Scontras during our inaugural lab hackathon. Send any comments to dco-at-stanford-dot-edu.


## Details

The program does a simple word-level count. In most cases, we have a dictionary of words that are rated along some dimension, and the program simply does a word lookup, and highlights the words based on their rating along a certain dimension. Unknown words are give a neutral color.

- For Valence and Arousal, we have used the lexicon provided by Warriner et al. 2013, which consists of 13,915 English word lemmas rated on a 1-9 scale for Valence, Arousal, and Dominance. We did not use the Dominance dimension.
  - Other similar sentiment lexica that can be implemented: 
    - ANEW (Affective Norms of English Words; Bradley & Lang 1999): 1030 words rated on a 1-9 scale for Valence, Arousal, Dominance.
    - Bing Liu (Liu, Hu, & Cheng, 2005) opinion lexicon: 2 dictionaries consisting of 2006 positive and 4783 negative words.
    - (to be filled in)
- For concreteness, we used Brysbaert et al. 2014, which consists of 39,954 words rated on a 1-5 scale.



### Reference List

Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing and Comparing Opinions on the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.

Bradley, M. M., & Lang, P. J. (1999). Affective norms for English words (ANEW): Instruction manual and affective ratings (pp. 1-45). Technical Report C-1, The Center for Research in Psychophysiology, University of Florida.

Brysbaert, M., Warriner, A. B., & Kuperman, V. (2014). Concreteness ratings for 40 thousand generally known English word lemmas. Behavior research methods, 46(3), 904-911.

Warriner, A. B., Kuperman, V., & Brysbaert, M. (2013). Norms of valence, arousal, and dominance for 13,915 English lemmas. Behavior research methods, 45(4), 1191-1207.