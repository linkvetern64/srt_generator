import sys
#Import a wav file to https://speech-to-text-demo.mybluemix.net/
#import the text and regex all ' ' and '\n'
#pass that file into the g var and it should generate a srt file
def main():
    f = open('file.srt', 'w')
    seconds = 447
    counter = 1
    words = list()

    g = open('Welcome.txt', 'r')
    for line in g:
        words.append(line)

    words.reverse()
    word_count = words.__sizeof__()

    #avg. number of characters
    numPerLine = int(word_count / seconds)
    #change the step to update the amount of time text is on screen
    step = 5
    for i in range(0, seconds, step):
        f.write(str(counter) + "\n")
        f.write("00:00:" + str(format ((i * 1000), ',d')) + " --> " + "00:00:" + str(format(((i + step) * 1000), ',d')) + "\n")
        line = ""
        for i in range(0, 12, 1):
            if(words):
                part = words.pop()
                if part.endswith('\n'):
                    part = part[:-1]
                line += " " + part
        f.write(line + "\n")
        f.write("\n")
        counter += 1


main()