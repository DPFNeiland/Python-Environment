


from pytubefix import Youtube

def Download(link):
    youtubeObject = Youtube(link)
    youtubeObject = youtubeObject
    get_highest_resolution()
    
    try:
        youtubeObject.download()
    except:
        print("Erro")

    print("Já baixou")

link = input("Link: ")
#  64793
Download(link)