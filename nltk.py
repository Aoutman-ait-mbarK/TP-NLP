import nltk
 

from nltk.tokenize import sent_tokenize, word_tokenize,PunktSentenceTokenizer

from nltk.corpus import stopwords

from nltk.stem import PorterStemmer
 
import ghostscript


arabic_text="""ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي و هي بدايات الجبر، و من المهم فهم كيف كانت هذه الفكرة الجديدة مهمة، فقد كانت خطوة ثورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة، الجبر كان نظرية موحدة تتيح الأعداد الكسرية و الأعداد اللا كسرية، و قدم وسيلة للتنمية في هذا الموضوع مستقبلا. و جانب آخر مهم لإدخال أفكار الجبر و هو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل"""

english_text= """Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely 
the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from 
the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowed rational 
numbers, irrational numbers, geometrical magnitudes, etc., to all be treated as "algebraic objects". It gave mathematics a whole new 
development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the 
subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itself in a 
way which had not happened before.
"""
 

#*************************************Tokenize text by Syllable*******************************
#tk = nltk.SyllableTokenizer()
#print(tk.tokenize(arabic_text))
#print(tk.tokenize(english_text))
 
 #*****************************************tokenize text by word*************************************
 #------------------- tokenize english text by word-------------
#for i in range(len(word_tokenize((english_text)))) :
   #print(word_tokenize((english_text))[i])
 
 #-------------------tokenize arabic text by word-------------
#for i in range(len(word_tokenize((english_text)))) :
   # print(word_tokenize((arabic_text))[i])

#*******************************sentence Tokenizing*****************************************
#-------------------tokenize english text by sentence----------------------
#for i in range(len(sent_tokenize(english_text))) :
    #print(sent_tokenize(english_text)[i])
  
#-------------------tokenize arabic text by sentence-------------
#for i in range(len(sent_tokenize(arabic_text))) :
   # print(sent_tokenize(arabic_text)[i])
#for i in range(len(sent_tokenize(english_text))) :
    #print(sent_tokenize(english_text)[i])
#*******************************************Filtering Stop Words***************************************
#nltk.download("stopwords")
from nltk.corpus import stopwords
stop_words_eng = set(stopwords.words("english"))
stop_words_ar = set(stopwords.words("arabic"))

filter_english_text = []
 
for word in word_tokenize(english_text):
    if word.casefold() not in stop_words_eng:
        filter_english_text.append(word)

# Arabic Text using List Comprehension
filter_arabic_text = [
    word for word in arabic_text if word not in stop_words_ar
]

filter_arabic_text
###***************************** Stemming  English Text******************************
from nltk.stem import PorterStemmer
stem = PorterStemmer()

english_words_stem = [stem.stem(word) for word in filter_english_text] 
#print(english_words_stem)
#*********************************Stemming Arabic Text*****************************
from snowballstemmer import stemmer
ar_stemmer = stemmer("arabic")

arabic_words_stem = [ar_stemmer.stemWord(arabic_text) for ar_word in filter_arabic_text]
#print(arabic_words_stem)

#********************************Tagging Parts of Speech***************************

#eng_pos_tag = nltk.pos_tag(word_tokenize(english_text))
#nltk.help.upenn_tagset()
#en_pos_tag = nltk.pos_tag(word_tokenize(english_text)) 
#******************************************************************************************
 
#*******************************### Lemmatizing*******************************************
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in word_tokenize(english_text)]
#print(lemmatized_words)

#***************************************### Chunking*******************************************
#grammar = "NP: {<DT>?<JJ>*<NN>}"
#chunk_parser = nltk.RegexpParser(grammar)
#chunk_parser.parse(nltk.pos_tag(word_tokenize(english_text)))
#t = chunk_parser.parse(nltk.pos_tag(word_tokenize(english_text)))
#print(t.draw())

###**************************************** Printing Dependencies**************************

#%load_ext watermark
#%watermark -v -m -p nltk
#%watermark --iversions