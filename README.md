# OpenImageProxy
Proxy server to open the image in any format. (ex. gif,CMYK_jpg in Unity)

```
GET http://localhost:8080/open_image_proxy?file_path=xxxxxxxx
```

```
POST http://localhost:8080/open_image_proxy
<form action="/open_image_proxy" method="post">
	<input type="text" name="file_path">
	<input type="submit">
</form>
```
