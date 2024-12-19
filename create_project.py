import os

def create_project_structure(base_path="."): #корневая папка, где все создается
    folders = {
        "": ["index.html"],  
        "styles": ["layout.css", "style.css", "reset.css", "responsive.css", "fonts.css", "animation.css"],  
        "scripts": ["javascript.js"], 
        "img": [],  
        "fonts": [], 
    }

    reset_css_content = """html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed, 
figure, figcaption, footer, header, hgroup, 
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
}
/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure, 
footer, header, hgroup, menu, nav, section {
    display: block;
}
body {
    line-height: 1;
}
ol, ul {
    list-style: none;
}
blockquote, q {
    quotes: none;
}
blockquote:before, blockquote:after,
q:before, q:after {
    content: '';
    content: none;
}
table {
    border-collapse: collapse;
    border-spacing: 0;
}"""

    style_css_content = """@import url('reset.css');
@import url('fonts.css');
@import url('layout.css');
@import url('responsive.css');
@import url('animation.css');
"""

    index_content = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ваш проект</title>
    <!-- тут можете скопировать ваши метатеги: https://metatags.io/ -->
    <link rel="stylesheet" href="styles/style.css" />
    <script src="scripts/javascript.js"></script>
  </head>
  <body></body>
</html>

"""

    fonts_css_content = """@font-face {
  font-family: 'твое название'; /* название шрифта */
  src: url(../fonts/твоя_ссылка.ttf) format('truetype'); /* ссылка на файл */
}

@font-face {
  font-family: 'твое название'; /* название шрифта */
  src: url(../fonts/твоя_ссылка.otf) format('opentype'); /* ссылка на файл */
}

@font-face {
  font-family: 'твое название'; /* название шрифта */
  src: url(../fonts/твоя_ссылка.woff) format('woff'); /* ссылка на файл */
}

"""


    os.makedirs(base_path, exist_ok=True)

    for folder, files in folders.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            with open(file_path, "w", encoding="utf-8") as f:
                if file == "fonts.css":
                    f.write(fonts_css_content)
                elif file == "reset.css":
                    f.write(reset_css_content)
                elif file == "style.css":
                    f.write(style_css_content)
                elif file == "index.html":
                    f.write(index_content)


create_project_structure()