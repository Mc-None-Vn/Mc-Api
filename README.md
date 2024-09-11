# Welcome to Mc Api (Beta)
### Lưu ý: Code ở dưới là ví dụ cho BDFD, ngôn ngữ lập trình khác thì có thể dùng [Link Api](https://mc-none-vn.onrender.com)


## Api level

### 1. Level card
#### Code:
```python
$var[url;https://mc-none-vn.onrender.com]
$var[avt;$authorAvatar]
$var[name;$username]
$var[lvl;1]
$var[xp;10]
$var[req;100]
$var[hex-bg;$url[encode;#ff0000]] $c[Màu nền bên phải Level card]
$var[hex-xp;$url[encode;#00e500]] $c[Màu hiển thị xp đang có bao nhiêu]
$var[color-font;$url[encode;white]] $c[Màu chữ (Bắt buộc ghi chữ, ko phải hex)]
$var[hex-xp-bg;$url[encode;#ffffff]] $c[Màu nền thanh xp khi chưa đầy thanh]
$image[$var[url]/api/level/card/?avatar=$var[avt]&username=$var[name]&level=$var[lvl]&xp=$var[xp]&req=$var[req]&color_bg=$var[hex-bg]&color_xp=$var[hex-xp]&color_font=$var[color-font]&color_xp_bg=$var[hex-xp-bg]]
```
#### Thành quả:
![Image]

### 2. Level auto (Tự cộng level)
#### Code:
```python
$httpGet[https://mc-none-vn.onrender.com/api/level/auto/?xp=90&req=100&level=2&add=5]
Xp: $httpResult[xp]
Req: $httpResult[req]
Level: $httpResult[level]
```
#### Thành quả:
![Image]

### 3. Level up card
#### Code:
```python
$image[https://mc-none-vn.onrender.com/api/level/up/?level=3&avatar=$authorAvatar]
```
#### Thành quả:
![Image]


### © 2024 mc.none MSVB Community. All rights reserved!