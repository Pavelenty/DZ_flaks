import json

def load_posts():
    """Загружает файл posts.json и возращает его"""
    with open('posts.json', encoding='utf8') as f:
        posts = json.load(f)
    return posts


def get_tags():
    """Эта функция возращает список всех слов со знаком #(тегов), слова находятся в словорях 'content' из файла 'functions'"""
    """Что бы загрузить все посты откуда надо вытощить 'content' я использовал функцию load_posts()"""
    """Что бы знак '#' не портил красоту после нахождения слова этот символ сразу уберается"""
    tags = []
    posts = load_posts()
    for content in posts:
        content = content["content"].split()
        for tag in content:
            if tag.find("#") != -1:
                tag = tag.replace('!', '').replace('.', '').replace(',', '').replace('#', '')
                tags.append(tag)
    return tags


def posts_by_tag(tag):
    posts_tag = []
    posts = load_posts()
    for post in posts:
        if post["content"].find(str(tag)) != -1:
            posts_tag.append(post)
    return posts_tag