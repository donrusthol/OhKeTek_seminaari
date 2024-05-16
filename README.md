# Koneoppiminen, Neuroverkot ja Luonnollisen Kielen Käsittely (NLP)

### Johdanto
Koneoppiminen ja neuroverkot ovat olennainen osa tekoälyä. Ne mahdollistavat tietokoneiden oppimisen ja päätöksenteon datan perusteella. Lisäksi luonnollisen kielen käsittely (NLP) liittyy ihmisten ja tietokoneiden väliseen vuorovaikutukseen, erityisesti kielten ymmärtämiseen ja tuottamiseen.

## Tutkielma

### Koneoppiminen
Koneoppiminen on tietojenkäsittelytieteen ala, joka keskittyy algoritmien kehittämiseen, jotka parantavat suorituskykyään kokemuksen perusteella. Koneoppiminen on osa tekoälyä ja se käyttää tilastollisia malleja ja algoritmeja tietojen analysointiin ja päätelmien tekemiseen. Koneoppimisen avulla tietokoneet voivat suorittaa tehtäviä, jotka olisivat aiemmin olleet mahdollisia vain ihmisille, kuten kuvien luokittelu, datan analysointi tai hintavaihteluiden ennustaminen.

### Neuroverkot
Neuroverkot ovat koneoppimisen alalaji, joka jäljittelee ihmisaivojen toimintaa. Ne koostuvat solmuista tai tekoälyneuroneista, jotka on järjestetty kerroksiin: syöttökerros, yksi tai useampi piilotettu kerros ja lähtökerros. Jokainen solmu on yhteydessä muihin, ja sillä on oma painoarvonsa ja kynnysarvonsa. Neuroverkot oppivat koulutusdatan avulla ja parantavat tarkkuuttaan ajan myötä. Ne ovat tehokkaita työkaluja tietojenkäsittelytieteessä ja tekoälyssä, mahdollistaen datan luokittelun ja klusteroinnin suurella nopeudella.

### Luonnollisen kielen käsittely (NLP)
Luonnollisen kielen käsittely (NLP) on tekoälyn haara, joka auttaa tietokoneita ymmärtämään, tulkitsemaan ja manipuloimaan ihmiskieltä. NLP yhdistää laskennallisen kielitieteen - ihmiskielen sääntöpohjaisen mallinnuksen - tilastollisiin ja koneoppimismalleihin, jotta tietokoneet ja digitaaliset laitteet voivat tunnistaa, ymmärtää ja tuottaa tekstiä ja puhetta

### Sanavektorit
Sanavektorit ovat tapa esittää sanoja vektoreina moniulotteisessa tilassa, jossa vektorien välinen etäisyys ja suunta heijastavat vastaavien sanojen samankaltaisuutta ja suhteita. Sanavektorit tekevät teknologioista, kuten puheentunnistuksesta ja konekäännöksestä, mahdollisia.

## Raportti

### Koneoppimisen ja neuroverkkojen sovellukset
Koneoppimista ja neuroverkkoja hyödynnetään monilla aloilla, mukaan lukien rahoitus, terveydenhuolto ja autoteollisuus. Ne ovat olennainen osa monia digitaalisia tuotteita ja palveluita, joita käytämme päivittäin. Esimerkkejä ovat ääniohjatut GPS-järjestelmät, digitaaliset avustajat, puheesta tekstiksi -diktaatio-ohjelmistot ja asiakaspalvelu-chatbotit.

### NLP:n ja sanavektoreiden sovellukset
NLP:llä on merkittävä rooli tekoälyn sovelluksissa, kuten tekstiluokittelussa, sentimenttianalyysissä, konekäännöksissä ja muissa. Sanavektoreita käytetään laajasti NLP-tehtävissä, kuten tekstiluokittelussa, entiteettien tunnistamisessa ja konekäännöksissä. Ne mahdollistavat koneoppimisalgoritmien ymmärtämisen ja prosessoinnin semanttisten sanojen suhteista perinteisiin menetelmiin verrattuna monipuolisemmin.

## Yhteenveto
Koneoppiminen, neuroverkot ja NLP ovat keskeisiä tekoälyn osa-alueita. Niitä voidaan hyödyntää monissa sovelluksissa, kuten kuvantunnistuksessa, puheentunnistuksessa ja luonnollisen kielen käsittelyssä. Markdown-muotoisen raportin avulla voimme syventyä näihin aiheisiin tarkemmin ja ymmärtää niiden merkitystä valmistavassa teollisuudessa ja muissa sovelluksissa.

# Tekstintunnistus kuvasta ja videosta Pythonilla (Projektityö)
Tämä Python-skripti on suunniteltu tunnistamaan ja tulostamaan tekstiä kuva- tai videotiedostosta käyttämällä optista merkintunnistusta (OCR - Optical Character Recognition) Tesseractin avulla. Skripti on jaettu useisiin toimintoihin, joista jokaisella on oma rooli:

1. **preprocess_image(image)**: Tämä toiminto ottaa kuvan syötteeksi ja esikäsittelee sen parantaakseen OCR:n tarkkuutta. Esikäsittelyvaiheet sisältävät:
  * Kuvan muuntaminen harmaasävyiseksi OpenCV:n cvtColor-toiminnolla. Tämä tehdään, koska OCR toimii paremmin harmaasävykuvissa.
  * Gaussin sumennuksen lisääminen harmaasävykuvaan OpenCV:n GaussianBlur-toiminnolla. Tämä auttaa vähentämään kohinaa kuvassa.
  * Otsun kynnysarvon soveltaminen OpenCV:n kynnysfunktiolla. Tämä menetelmä laskee automaattisesti parhaan kynnysarvon tekstin erottamiseksi taustasta, mikä auttaa parantamaan OCR:n tarkkuutta.
2. **recognize_text_from_image(image)**: Tämä toiminto ottaa esikäsitellyn kuvan syötteeksi ja tunnistaa kuvan tekstin Tesseract OCR:n avulla. OpenCV-kuva (numpy array) muunnetaan ensin PIL-kuvaksi. Sitten pytesseract-moduulin **image_to_string**-funktiota käytetään tekstin tunnistamiseen ja palauttamiseen kuvasta.
3. **recognize_text_from_file(file_path, skip_frames=1)**: Tämä toiminto ottaa polun kuva- tai videotiedostoon ja syötteenä valinnaisen **skip_frames**-parametrin. **Skip_frames**-parametria käytetään videotiedostojen käsittelyssä ohittamaan tietty määrä kehyksiä kunkin käsitellyn kehyksen välillä. Toiminto tarkistaa ensin tiedostotunnisteen määrittääkseen, onko se kuva- vai videotiedosto. Jos se on kuvatiedosto, kuva luetaan OpenCV:n **imread**-toiminnolla, esikäsitellään ja teksti tunnistetaan ja tulostetaan. Jos se on videotiedosto, video avataan OpenCV:n **VideoCapture**-toiminnolla, minkä jälkeen jokainen kehys (tai jokainen **skip_frames** -kehys) esikäsitellään ja teksti tunnistetaan ja tulostetaan. Jos tiedosto ei ole kuva eikä video tai jos tiedoston avaamisessa tapahtuu virhe, tulostetaan virheilmoitus.

Skripti sisältää myös pääosan, joka suoritetaan, kun komentosarja ajetaan erillisenä ohjelmana. Tämä osio kutsuu tunnusta_teksti_tiedostosta-funktiota, jossa on kovakoodattu tiedostopolku tekstintunnistuskoodin testaamiseksi. Tiedostopolku voidaan korvata polkulla mihin tahansa kuva- tai videotiedostoon testausta varten.

Linkki esittelyvideoon: [https://drive.google.com/file/d/1EkSwS5PYzWMEjQq1g27QtXLMSxoOEpku/view?usp=sharing](https://drive.google.com/file/d/1EkSwS5PYzWMEjQq1g27QtXLMSxoOEpku/view?usp=sharing)

# Lähteet:
1) What Is Machine Learning? Definition, Types, and Examples. https://www.coursera.org/articles/what-is-machine-learning.
2) What is a Neural Network? | IBM. https://www.ibm.com/topics/neural-networks.
3) What Is Natural Language Processing? | IBM. https://www.ibm.com/topics/natural-language-processing.
4) What Are Word Embeddings? | IBM. https://www.ibm.com/topics/word-embeddings.
5) Introduction to Word Vectors - DZone. https://dzone.com/articles/introduction-to-word-vectors.
6) 8 Applications of Neural Networks | Analytics Steps. https://www.analyticssteps.com/blogs/8-applications-neural-networks.
7) What Is Machine Learning (ML)? | IBM. https://www.ibm.com/topics/machine-learning.
8) Machine learning - Wikipedia. https://en.wikipedia.org/wiki/Machine_learning.
9) Neural network - Wikipedia. https://en.wikipedia.org/wiki/Neural_network.
10) What is a neural network? A computer scientist explains - The Conversation. https://theconversation.com/what-is-a-neural-network-a-computer-scientist-explains-151897.
11) What is a Neural Network? | A Comprehensive Neural Networks Guide - Elastic. https://www.elastic.co/what-is/neural-network.
12) What is Natural Language Processing? Definition and Examples. https://www.coursera.org/articles/natural-language-processing.
13) Natural Language Processing (NLP): What it is and why it matters. https://www.sas.com/en_us/insights/analytics/what-is-natural-language-processing-nlp.html.
14) Machine learning, explained | MIT Sloan. https://mitsloan.mit.edu/ideas-made-to-matter/machine-learning-explained.
15) Neural network (machine learning) - Wikipedia. https://en.wikipedia.org/wiki/Neural_network_%28machine_learning%29.
16) What is Word Vectors - Word Vectors Definition from MarketMuse Blog. https://blog.marketmuse.com/glossary/word-vectors-definition/.
17) Word Vectors in Natural Language Processing: Introduction. https://medium.com/sciforce/word-vectors-in-natural-language-processing-introduction-c85d26c7d527.
