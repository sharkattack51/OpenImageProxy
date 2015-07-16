from bottle import route, get, post, run, HTTPResponse, request
import Image
from StringIO import StringIO
import urllib

print "-> start OpenImageProxyServer..."
print "-> ex) GET http://localhost:8080/open_image_proxy?file_path=xxxxxxxx"
print """-> ex) POST http://localhost:8080/open_image_proxy"
<form action="/open_image_proxy" method="post">
	<input type="text" name="file_path">
	<input type="submit">
</form>"""
print ""

def open_image(file_path):
	image = Image.open(file_path)

	# カラーモードを変換する
	image = image.convert("RGBA")
	
	# 更新をbufferにpngで保存
	buf = StringIO()
	image.save(buf, "png")
	
	# bufferからレスポンス作成
	response = HTTPResponse(status=200, body=buf.getvalue())
	response.set_header("Content-type", "Image")
	return response

@route("/")
def index():
	return "HELLO!!"

@get("/open_image_proxy")
def get_open_image_proxy():
	open_image(urllib.unquote(request.query["file_path"]))

@post("/open_image_proxy")
def post_open_image_proxy():
	open_image(request.forms.get("file_path"))

if __name__ == "__main__":
	run(host='localhost', port=8080)