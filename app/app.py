import argparse
from core.user_manager import UserManager

user_manager = UserManager()

def main():
    """
        Main function
            :return: None
            :rtype: None
    """
    parser = argparse.ArgumentParser(description='Password Manager CLI')
    subparsers = parser.add_subparsers(title='commands', dest='command', required=True)

    print("""
        _   _  ____  _   _ ____  _     ____  _____ ____  
        | | | |/ ___|| | | | __ )| |   |  _ \| ____|  _ \ 
        | |_| | |    | | | |  _ \| |   | | | |  _| | | | |
        |  _  | |___ | |_| | |_) | |___| |_| | |___| |_| |
        |_| |_|\____| \___/|____/|_____|____/|_____|____/ 

        ===============================================
            Password Manager - v1.0.0
        ===============================================

        Welcome to the Password Manager CLI tool! 
        Safely store and manage your passwords.

        Usage: python password_manager.py [options]

        Options:
        -h, --help          Show help message and exit.
        -a, --add           Add a new password.
        -g, --get <name>    Get password by name.
        -d, --delete <name> Delete password by name.
        -l, --list          List all saved passwords.
        -c, --copy <name>   Copy password to clipboard.
        """)
    
    # Register command
    register_parser = subparsers.add_parser('register', help='Register a new user')
    register_parser.add_argument('username', type=str, help='Username')
    register_parser.add_argument('password', type=str, help='Password')


    # Login command
    login_parser = subparsers.add_parser('login', help='Login a user')
    login_parser.add_argument('username', type=str, help='Username')
    login_parser.add_argument('password', type=str, help='Password')

    # Logout command
    logout_parser = subparsers.add_parser('logout', help='Logout a user')
    logout_parser.add_argument('username', type=str, help='Username')

    # delete an user
    delete_parser = subparsers.add_parser('delete', help='Delete a user')
    delete_parser.add_argument('username', type=str, help='Username')

    args = parser.parse_args()


    if args.command == 'register':
        user_manager.register_user(args.username, args.password)
    elif args.command == 'login':
        user_manager.login_user(args.username, args.password)
    elif args.command == 'logout':
        user_manager.logout_user(args.username)
    elif args.command == 'delete':
        user_manager.delete_user(args.username)

if __name__ == '__main__':
    main()