
def list_all_video(video):
    pass
def add_video(video):
    pass
def update_video_details(video):
    pass
def delete_video(video):
    pass
def close_add(video):
    pass


def main():
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
            case 2:
                add_video(video)
            case 3:
                update_video_details(video)
            case 4:
                delete_video(video)
            case 5:
                close_add(video)
                break
            case _:
                print('you not choose an options ')