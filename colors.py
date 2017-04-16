
#created by sun <SunSoftwares.pvt>
#Open source freely distributable
#2016-17
#Thanks for using it
# colors libary
class mystyle:
          bold='\033[1m'
          dim='\033[2m'
          underlined='\033[4m'
          blink='\033[5m'
          hidden='\033[8m'
          normal='\033[0m'

class mycolor:
          black='\033[30m'
          red='\033[31m'
          green='\033[32m'
          yellow='\033[33m'
          blue='\033[34m'
          magenta='\033[35m'
          cyan='\033[36m'
          lightgray='\033[37m'
          darkgray='\033[90m'
          lightred='\033[91m'
          lightgreen='\033[92m'
          lightyellow='\033[93m'
          lightblue='\033[94m'
          lightmagenta='\033[95m'
          lightcyan='\033[96m'
          white='\033[97m'

class mybackground:
          black='\033[40m'
          red='\033[41m'
          green='\033[42m'
          yellow='\033[43m'
          blue='\033[44m'
          magenta='\033[45m'
          cyan='\033[46m'
          lightgray='\033[47m'
          darkgray='\033[100m'
          lightred='\033[101m'
          lightgreen='\033[102m'
          lightyellow='\033[103m'
          lightblue='\033[104m'
          lightmagenta='\033[105m'
          lightcyan='\033[106m'
          white='\033[107m'
#how to use : print(mycolor.blue+"text") to print text in blue
if __name__=="__main__":
          print("Color libary for printing colors in linux terminal\n #how to use : print(mycolor.blue+'text') to print text in blue")
