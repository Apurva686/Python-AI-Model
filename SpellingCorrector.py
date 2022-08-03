# we will go with textblob as this a python library using nlp techniques
from textblob import Word,TextBlob
from flask import Flask

app = Flask(__name__)

docx = ["calendar","lightening","misspel","neccessary","bussiness","recive","adress"]

@app.route('/<string:name>')
def check_word(name):
   word = Word(name)
   return word.correct()


@app.route('/checkSentence')
def check_sentence():
    sen = TextBlob('my nam wis apurva')
    print(sen.correct())
    return "apurva"


# #preferred working
# @app.route('/correctWordUsingAutocorrect/<string:name>')
# def correct_word_autocorrect(name):
#         return spell(name)



#for word in docx:
    # to autocorrect spelling
    # print(f'{word}:{spell.correction(word)}')
    # to print list of available candidates for spelling
        #print(f'{word}:{spell.candidates(word)}:probability{spell.word_probability(word)}')


app.run(port=5000)


