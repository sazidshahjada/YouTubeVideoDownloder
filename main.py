from pytube import YouTube
import os

os.system('clear')

print(
    """
                YouTube Video Downloader
            -------------------------------
    """
)

while True:
    link = input('Enter Youtube Video Link: ')
    print('\n')

    yt = YouTube(link)

    try:
        title = yt.title
        views = yt.views
        print('Video Details:')
        print('--------------\n')
        print('Title:-', title)
        print('View:-', views)
        print('\n')

        print('Do You Want To Download This Video? [Y/N]')
        print('Y -> Yes\nN -> No\n')
        conf = input('---> ')
        print()

        if conf.upper() == 'Y':
            path = '/home/sajid/Videos'
            try:
                print("Downloading ...")
                video = yt.streams.get_highest_resolution()
                video.download(path)
                print()
                print('Download Completed\n\n')
                exit()
            except Exception:
                print('An Error Occured\n\n')
        else:
            exit()
    except Exception:
        print('Unable To Connect')
        print('Check Your Internet Connection\n\n')










