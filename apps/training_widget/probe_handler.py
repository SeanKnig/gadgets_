from pyfiglet import Figlet
import os
import subprocess

end = False
arguement = []

class MyPrompt():
    f = Figlet(font='small')
    print(f.renderText("Gaudy CLI"))
    def __init__(self, command, arguement):
        self.command = command
        self.arguement = arguement

    def do_Help(self, command):
        print("List of available commands")
        print("netScan")
        print("list")
        print("hello")
        print("change")
        print("run")
        print("remove")


    def do_netScan(self, arguement):
        net = True
        while(net == True):
            os.system('sudo nmap -sn 192.168.1.112/24')
            net == False
            break;
        
    

    def do_hello(self, arguement):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(arguement) == 0:
            name = 'stranger'
        else:
            name = arguement
        print(self.f.renderText("Hello, %s" % name))

    def do_quit(self, arguement):
        print("Goodbye")
        raise SystemExit
    
    def do_list(self, arguement):
        if len(arguement) == 0:
            print(self.f.renderText("Current Directory"))
            print(os.listdir())
        else:
            #Printing the arguement directory
            print(os.listdir(arguement))

    def do_change(self, arguement):
        os.chdir(arguement)

    def do_run(self, arguement):
        """run logic os.run()"""
        pid = os.fork()
        runStatement = subprocess.call()
        os.run(arguement)

        
        if pid > 0 : 
            print("I am parent process:") 
            print("Process ID:", os.getpid()) 
            print("Child's process ID:", pid) 
        else : 
            print("\nI am child process:") 
            print("Process ID:", os.getpid()) 
            print("Parent's process ID:", os.getppid())
        


    def do_remove(self, arguement):
        """remove logic"""

    def do_rename(self, arguement):
        """needs first and second arguement to rename appropriately"""
    
    def switch(self, command, arguement):

        return {
            'run': lambda: prompt.do_run(arguement),
            'netScan': lambda: prompt.do_netScan(arguement),
            'list': lambda: prompt.do_list(arguement),
        }[command]()
    
if __name__ == '__main__':
    available = ['help', 'list', 'netScan', 'quit', 'run', 'remove', 'rename', 'change', 'quit']
    
    while(end == False):
        getInput = input('hödl-> ')
        arguement = getInput.split()
        command = arguement[0]
        arguement.pop(0)
        print(command)
        print(arguement)
        prompt = MyPrompt(command, arguement)
        if command not in available or command == 'help':
            prompt.do_Help(command)
        elif(command in available):
            prompt.switch(command, arguement)