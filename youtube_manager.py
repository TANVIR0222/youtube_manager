
def list_all_video(video):
    pass


video = []

while True:
    print('\n Youtube Manager | choose an option')
    print('1. List all youtube video ')
    print('2. Add a youtube video ')
    print('3. Update a youtube video details ')
    print('4. Deleted a youtube video')
    print('5. Exit the app ')
    # user input 
    choose = input("Enter your choose : ")

    match choose:
        case 1:
            list_all_video(video)