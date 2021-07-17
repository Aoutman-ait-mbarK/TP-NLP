import spacy
from spacy.lang.ar import *

english_text = """Perhaps one of the most significant advances made by Arabic mathematics began at this time with the work of al-Khwarizmi, namely the beginnings of algebra. It is important to understand just how significant this new idea was. It was a revolutionary move away from the Greek concept of mathematics which was essentially geometry. Algebra was a unifying theory which allowedrational numbers,irrational numbers, geometrical magnitudes, etc., to all be treated as \"algebraic objects\". It gave mathematics a whole new development path so much broader in concept to that which had existed before, and provided a vehicle for future development of the subject. Another important aspect of the introduction of algebraic ideas was that it allowed mathematics to be applied to itselfin a way which had not happened before."""
arabic_text ="""ربما كانت أحد أهم التطورات التي قامت بها الرياضيات العربية التي بدأت في هذا الوقت بعمل الخوارزمي وهي بدايات الجبر, ومن المهم فهم كيف كانت هذه الفكرة الجديدة مهمة, فقد كانت خطوة نورية بعيدا عن المفهوم اليوناني للرياضيات التي هي في جوهرها هندسة, الجبر کان نظرية موحدة تتيح الأعداد الكسرية والأعداد اللا كسرية, والمقادير الهندسية وغيرها, أن تتعامل على أنها أجسام جبرية, وأعطت الرياضيات ككل مسارا جديدا للتطور بمفهوم أوسع بكثير من الذي كان موجودا من قبل, وقم وسيلة للتنمية في هذا الموضوع مستقبلا. وجانب آخر مهم لإدخال أفكار الجبر وهو أنه سمح بتطبيق الرياضيات على نفسها بطريقة لم تحدث من قبل"""

#*********************************## Tokenization*********************************************
nlp = spacy.load("en_core_web_sm")

doc_ar = Arabic()
doc_ar = nlp(arabic_text)
doc_en = nlp(english_text)

for token in doc_ar:
    print(token.text)
    
for token in doc_en:
    print(token.text)

    ### Part-of-speech tags and dependencies
for token in doc_en:
    print(token.text, token.pos_, token.tag_)  

for token in doc_ar:
    print(token.text, token.pos_)

    ### Visualizing the dependency parse

    from spacy import displacy
displacy.serve(doc_en, style="dep")

### Lemmatization

for token in doc_ar:
    print(token.text, token.pos_, token.lemma_)

 ### Chunking

for chunk in doc_en.noun_chunks:
    print(chunk.label_, chunk)


for token in doc_en:
    if token.pos_ == "VERB":
        print(token.tag_, token.lemma_)


        ### Named entities 

for ent in doc_en.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)


### Named entities 
for ent in doc_en.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

    ### Dependencies

#%load_ext watermark
#%watermark -p spacy


