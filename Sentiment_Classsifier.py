###########################################################################
##################SENTIMENT CLASSIFIER FOR TWITTER###########################
############################################################################


def strip_punctuation(s):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for char in punctuation_chars:
        if(char in s):
            s=s.replace(char,"")
    return s

##################################################################
############## list of positive words to use######################

           

def get_pos(s):
    positive_words = []
    with open("positive_words.txt") as pos_f:
        for lin in pos_f:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    pos_count=0
    s=s.split()
    for word in s:
        word=strip_punctuation(word)
        word=word.lower()
        if(word in positive_words):
            pos_count+=1
    return pos_count
            
#####################################################################




def get_neg(s):
    negative_words = []
    with open("negative_words.txt") as neg_f:
        for lin in neg_f:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    
    neg_count=0
    s=s.split()
    for word in s:
        word=strip_punctuation(word)
        word=word.lower()
        if(word in negative_words):
            neg_count+=1
    return neg_count

#############################################################################################
#############################################################################################
def SentimentClassifier():
    input_file =input("Enter Input File containing the following headers:Text,Number of retweets,Number of Replies:\n \nEnter:")
    output=input("Enter Name you want to save the output as:\n")
    
    
    input_twitter_data=open(input_file,"r")
    output_file=open(output,"w")
    lines=input_twitter_data.readlines()

    output_file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    output_file.write("\n")
    lines.pop(0) #Dont use the headers of input


    for line in lines:
    
        l=line.strip().split(",")
        output_file.write("{},{},{},{},{}".format((l[1]),(l[2]),(get_pos(l[0])),(get_neg(l[0])),(get_pos(l[0])-get_neg(l[0]))))
        output_file.write("\n")

    output_file.close()
    input_twitter_data.close()
    
    
SentimentClassifier()
    



