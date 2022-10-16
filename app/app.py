from cProfile import label
from unicodedata import name
from flask import Flask,jsonify,render_template,request
from similar import finder

#creating the application
app=Flask(__name__)

#FOR API-
@app.route("/<string:word>")
def similar_word(word):

    sim_words_dictionary=finder(word)
    if sim_words_dictionary is None:
        sim_words_dictionary={
            "Data":"Infomration Unavailable"
        }
    result={
        "ORIGINAL_WORDS":word,
        "SIMILAR_WORDS":sim_words_dictionary
    }
    return jsonify(result)

#FOR VISUALIZATION-
@app.route('/',methods=['POST','GET'])
def plotify():

   

   if request.method=='POST':
        word=request.form.get('word')
        sim_words_dictionary=finder(word)
        if sim_words_dictionary is None:
            labels=None
            values=None
        else:
            labels=sim_words_dictionary.keys()
            labels=list(labels)
            values=sim_words_dictionary.values()
            values=list(values)

       
        
        
        return render_template('index.html',labels=labels,values=values,word=word)


   else:

        return render_template('index.html')

   


if __name__=="__main__":
    app.run(debug=True)
