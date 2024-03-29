from dad_jokes_api import search_dad_jokes
from pastebin_api import post_new_paste
import sys

def main(): 
    search_term = get_search_term()
    jokes_list = search_dad_jokes(search_term)
    if jokes_list:
        title, body_text = get_paste_contect(jokes_list, search_term)
        paste_url = post_new_paste(title,body_text)
        print(f'URL of Jokes paste: {paste_url}')

def get_search_term():
    num_params = len(sys.argv) - 1
    if num_params > 0:
        return sys.argv[1]
    else:
        print('Error: Missing search term')
     

def get_paste_content():

    title = f'Dad Jokes Conrtaining the Term "{search_term}"'
    
    divider = '=' *20
    body_text = ''
    for joke in jokes_list:
        body_text += joke
        body_text += divider

    return title, body_text

if __name__ == "__main__":
    main()  