import matplotlib.pyplot as plt
import numpy as np

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
            'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
            'W', 'X', 'Y', 'Z']

frequency = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228,
             0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
             0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987,
             0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
             0.01974, 0.00074]

def index_of_coincidence(group):
    if (len(group) == 0):
        return 0

    result = 0
    
    for letter in alphabet:
        result += pow(group.count(letter)/len(group), 2)

    return result

def group_frequency(group):
    if (len(group) == 0):
        return 0

    repetition = []

    for letter in alphabet:
        repetition.append(group.count(letter)/len(group))

    return repetition

cmessage = open("EncryptedMessage_2.txt", "r")

i = 1
keylength = 10
w = 0.4
max_ioc = 0
group = ""
cfrequency = []
data = cmessage.read()

for i in range(2, keylength):
    for k in range(i):
        for j in range(len(data)):
            if (j % i == k):
                group += data[j]
        max_ioc = index_of_coincidence(group)
        if (max_ioc >= 0.06):
            cfrequency = group_frequency(group)
            bar1 = np.arange(len(alphabet))
            bar2 = [l+w for l in bar1]
            plt.bar(bar1, frequency, w, label = "Expected")
            plt.bar(bar2, cfrequency, w, label = "Observed")
            plt.xticks(bar1, alphabet)
            plt.legend()
            plt.show()
            keylength = i
        group = ""
    max_ioc = 0
    i += 1

print("Key length = ", keylength)
cmessage.close()

