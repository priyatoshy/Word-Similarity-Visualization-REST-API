from importlib import machinery


def finder(word):

    try:
    
        import bs4 as bs
        import urllib.request
        import re
        import nltk
        word=word.lower()
        sub_url_word="_".join( word.split())
        url = 'https://en.wikipedia.org/wiki'  # no trailing /
        final_url = '/'.join([url,sub_url_word])
        scrapped_data = urllib.request.urlopen(final_url)
        article = scrapped_data .read()

        parsed_article = bs.BeautifulSoup(article,'lxml')

        paragraphs = parsed_article.find_all('p')

        article_text = ""

        for p in paragraphs:
            article_text += p.text

        try:
            import string
            from nltk.corpus import stopwords
            import nltk
        except Exception as e:
            print(e)


        class PreProcessText(object):

            def __init__(self):
                pass

            def __remove_punctuation(self, text):
                """
                Takes a String
                return : Return a String
                """
                message = []
                for x in text:
                    if x in string.punctuation:
                        pass
                    else:
                        message.append(x)
                message = ''.join(message)

                return message

            def __remove_stopwords(self, text):
                """
                Takes a String
                return List
                """
                words= []
                for x in text.split():

                    if x.lower() in stopwords.words('english'):
                        pass
                    else:
                        words.append(x)
                return words


            def token_words(self,text=''):
                """
                Takes String
                Return Token also called  list of words that is used to
                Train the Model
                """
                message = self.__remove_punctuation(text)
                words = self.__remove_stopwords(message)
                return words


        flag = nltk.download("stopwords")

        if (flag == "False" or flag == False):
            print("Failed to Download Stop Words")
        else:
            print("Downloaded Stop words ...... ")
            helper = PreProcessText()
            #words = helper.token_words(text=txt)
            words = helper.token_words(text=article_text)


        from gensim.models import Word2Vec

        #model = Word2Vec([words], min_count=1)
        model = Word2Vec([words],  window=5, min_count=1, workers=4)


        #vocabulary = model.wv.vocab

        sim_words = model.wv.most_similar(word)

        sim_word_dictionary={}
        for item in sim_words:
            
            sim_word_dictionary[item[0]]=item[1]


        #print(sim_word_dictionary)
        #print(sim_word_dictionary.keys())
        #print(sim_word_dictionary.values())
        return sim_word_dictionary
    except Exception as err:
        err_dictionary={"Info":"Insufficient Information"}
        print(err)

#finder('machine')