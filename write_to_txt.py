
class textData:

    def __init__(self):
        f = open(fileName, 'a') #a = append

    def __del__(self):
        self.f.close()


    f = open('sampleText.txt', 'a')
    f.write('\n13,2\n14,7')
    f.close()