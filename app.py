from flask import Flask, request, render_template, send_from_directory
from functions import get_tags, posts_by_tag

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


#Главная страница
@app.route("/")
def page_index():
    """Страница поиска постов по тегу"""
    """tegs принимает значения функции get_tegs() которая описана в файле functions, в этом файле расписаны и другие теги"""
    """Данная функция работает с шаблоном 'index.html', эта же функция его и возрвращает с помощью функции render_template"""
    """tegs=tegs указывает на то что переменаая tegs из этого файла будет такой же и в шаблоне по пути 'template/<шаблоны>'"""
    tags = get_tags()
    return render_template('index.html', tags=tags)


@app.route("/tag", methods=["GET", "POST"])
def page_tag():
    """Строка methods["GET", "POST"] показывает что эта функция может принимать метод GET и POST"""
    """Я пользуюсь методом POST, name = request.form.get('tags_user') это страка показывает что переменная name принимает значения отправленного запроса"""
    """tags_user это названия поля, если поля имеет названия то значения этого можно узнать через request.form.get('tags_user')"""
    name = request.form.get('tag_select')
    posts = posts_by_tag(name)
    return render_template('post_by_tag.html', name=name, posts=posts)


@app.route("/post", methods=["GET", "POST"])
def page_post_create():
    """просто открывает шаблон post_form где ты добовляешь фотку и текст посту"""
    return render_template('post_form.html')


@app.route("/add", methods=["POST"])
def add_post():
    """UPLOAD_FOLDER это путь где сохраняются изображение постов"""
    """content это переменная которая принимает описания поста от пользователя"""
    """file.save это функция которая сохраняет файл чтоб в дальнейшем его использовать"""
    """file.filename это имя файла которое загружено в переменную file"""
    content = (request.form.get('content'))
    file = request.files['my_file']
    file.save(f'{UPLOAD_FOLDER}/{file.filename}')
    return render_template('post_uploaded.html', content=content, file=file.filename)


@app.route("/uploads/<path:path>")
def static_dir(path):
    """Сдесь была эта функция, не знаю как пользоватся и для чего она, обьесните"""
    return send_from_directory("uploads", path)


if __name__ == '__main__':
    app.run(debug=True)

