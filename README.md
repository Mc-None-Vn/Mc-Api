# Welcome to Mc Api (Beta)
### Lưu ý: Code ở dưới là ví dụ cho BDFD, ngôn ngữ lập trình khác thì có thể dùng link api
## [Link Api](https://mc-none-vn.onrender.com)


## Api level

### 1. Level card
#### Code:
```python
$image[https://mc-none-vn.onrender.com/api/level/card/?avatar=$authorAvatar&username=$username&level=1&xp=10&req=100&color_bg=$url[encode;#ff0000]&color_xp=$url[encode;#00e500]&color_font=$url[encode;white]&color_xp_bg=$url[encode;#ff0000]]
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