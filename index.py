#!python
# -*- encoding: utf-8 -*-


print("Content-Type: text/html;\n")    # HTML is following
print()                             # blank line, end of headers
import cgi, os, view
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
from html_sanitizer import sanitizer
SSanitizer = sanitizer.Sanitizer()

form = cgi.FieldStorage()
if "id"  in form :
    title = pageId = form.getvalue('id')
    description = open('./data/'+pageId, 'rt', -1, "utf-8").read()
    title = SSanitizer.sanitize(title)
    description = SSanitizer.sanitize(description)
    update_button='<button type="button" id="update_button" onclick="location.href=\'update.py?id={}\'">update</button>'.format(pageId)

    #버튼을 눌렀을 때 post방식으로 process_delete.py로 pageId값을 전송하는 방법 구현
    delete_action='''
    <form action="process_delete.py" method="post">
        <input type="hidden" name="pageId" value="{}">
        <input type="submit" value="delete">
    </form>
    '''.format(pageId)
else:
    title = pageId = "Welcome"
    description = "나는 닳아 없어질지언정, 녹이 슬어 사라질 수는 없었다."
    update_button=''
    delete_action=''
print("""
<!doctype html>
<html>

<head>
  <title>자기계발</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js">
  </script>
  <script src="color.js">
  </script>
</head>

<body>
  <input id="night_day" type="button" value="night" onclick="
      night_day_handler(this);
    ">

  <h1><a href="index.py" title="index">자기계발</a></h1>
  <div id="grid">
    <div id="sidebar">
      <ol>
        {listStr}
        <br>
        <button type = "button" onclick="location.href='create.py'" id="create">+</button>
      </ol>
    </div>
    <div id="article">
      <h3 style="font-style:italic">{title}</h3>
      <h4 style="font-style:italic">{desc}</h4>
      {update_button}
      {delete_button}
    </div>
  </div>
  <br>
  <div id="aa"><a href="일정관리/index.html" style="margin:50px;float:right;color:powderblue;">일정관리</a></div>
</body>

</html>
""".format(
    title=title,
    listStr = view.getList(),
    desc = description,
    update_button=update_button,
    delete_button=delete_action))
