import os
from UseCases.GitHubUseCases import GitHubUseCases

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def show_main_menu():
    print("1. Get git hub pull requests")
    print("2. Get GitHub pull request reviews")
    print("3. Exit")
    return input("Enter your choice: ")

while True:
    clear_screen()
    choice = show_main_menu()

    if choice == "3":
        clear_screen()
        print("Thank you for using git-hub-miner - Bye!!")
        break
    
    elif choice == "1":
        gh = GitHubUseCases()
        gh.get_github_pull_requests()
        break
    
    elif choice == "2":
        gh = GitHubUseCases()
        gh.get_github_pr_reviews()
        break
    
    else:
        print("Invalid choice")