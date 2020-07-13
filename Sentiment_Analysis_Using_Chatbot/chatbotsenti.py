import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer 

from sklearn.naive_bayes import MultinomialNB

def getStringArrayFromNumpyDataFrame(dataframe):
    list=[]
    for s in dataframe.values:
        if len(str(s[0]))>0:
            list.append(str(s[0]))
    return list

def getEmotions(text,clf):

    text=text.split()
    X_new_counts = count_vect.transform(text)
    X_new_tfidf = tfidf_transformer.transform(X_new_counts)
    
    predicted = clf.predict(X_new_tfidf)
    positive_count=0
    for x in predicted:
        if x==1:
            positive_count=positive_count+1
    return positive_count;


def getEmotionFromText(text):
    positives=getEmotions(text,clf_positive)
    negatives=getEmotions(text,clf_negative)
    bad=getEmotions(text,clf_bad)
    if(bad>0):
        return("Bad ->%s"%(text))
    else:
        if(positives-negatives)>0:
            return("Positive  ->%s"%(text))
        elif(negatives-positives)>0:
            return("Negative ->%s"%(text))
        else:
            return("Neutral  ->%s"%(text))

train_data_csv_name="Trumpwords.csv"

df_x_words = pd.read_csv(train_data_csv_name,usecols=[0],header=None)
df_y_positive= pd.read_csv(train_data_csv_name,usecols=[1],header=None)
df_y_negative= pd.read_csv(train_data_csv_name,usecols=[2],header=None)
df_y_bad= pd.read_csv(train_data_csv_name,usecols=[3],header=None)

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(getStringArrayFromNumpyDataFrame(df_x_words))
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf_positive = MultinomialNB().fit(X_train_tfidf, df_y_positive)
clf_negative = MultinomialNB().fit(X_train_tfidf, df_y_negative)
clf_bad = MultinomialNB().fit(X_train_tfidf, df_y_bad)

outputfile = open('sentimentanalysis.txt','w')

file_name="Vanalyse.txt"
with open(file_name, encoding="utf-8", errors = 'ignore') as f:
    for line in f:
        try:
            tmpstr=getEmotionFromText(line)
            print(tmpstr)
            outputfile.write(tmpstr)
        except UnicodeDecodeError:
            pass
outputfile.close()

