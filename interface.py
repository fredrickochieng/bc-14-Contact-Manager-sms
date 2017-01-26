# This section of the App(Contacts manager + sms) uses docopt with the built in cmd module 
#to demonstrate an interactive command application

"""
Usage:
    contact_manager_sms -n <name> -p <phonenumber>    add contact
    contact_manager_sms search <name>                 search for a contact
    contact_manager_sms text <name> -m <message>      send text
    contact_manager_sms (-i | --interactive)
    contact_manager_sms (-h | --help | --version)
Options:
    -i, --interactive                             Interactive Mode
    -h, --help                                    Show this screen and exit.
    
"""
 
import sys
import cmd
from docopt import docopt, DocoptExit
from contact_manager import ContactManager, send_text
from termcolor import cprint
from pyfiglet import figlet_format


def docopt_cmd(func):#this docorator passes the result of the decopt pasring to the called function
    
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            #Handles invalid arge
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print("invalid command! try again")
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class my_interactive_mode (cmd.Cmd):
    cprint(figlet_format('WELCOME ', font='sweet'), 'yellow', attrs=['bold'])
    print "CONTACTS MANAGER+SMS:".center(70)
    print "COMMANDS:".center(70)

                                
    intro = 'Welcome to data entry module!'\
    + '(type help for a list of commands,add -n <name> -p <phonenumber> for a new entry,text <name> -m <message> to send a text and search <name> to search for a contact.)'
    prompt='[contact_manager_sms]'
    file = None

    create_new_contact = ContactManager()

    def add_contact(self, name, number):
        print  self.create_new_contact.add_record(name, number)

    def search(self, name):
        print self.create_new_contact.search_record(name)

    def sms(self, name, message):
        print send_text(name, message)

    @docopt_cmd
    def do_add(self, args):
        """Usage: add -n <name> -p <phonenumber>"""
        self.add_contact(args['<name>'], args['<phonenumber>'])

    @docopt_cmd
    def do_search(self, args):
        """Usage: search <name>"""
        self.search(args['<name>'])

    @docopt_cmd
    def do_text(self, args):
        """Usage: text <name> -m <message>"""
        self.sms(args['<name>'], args['<message>'])

    def do_quit(self, args):
        """Quits Interactive Mode."""

        print('You just quit the commandline.Thank you')
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    my_interactive_mode().cmdloop()
print(opt)
