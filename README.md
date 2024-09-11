## Welcome to Mc Api (Beta)
### Lưu ý: Code ở dưới là ví dụ cho BDFD, ngôn ngữ lập trình khác thì có thể dùng [Link Api](https://mc-none-vn.onrender.com)
`
`
## |>==> Api về level
### 1. Level card
#### Code:
```
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
![Image](https://github.com/LorenorMc/Mc-Api/blob/e9474bd090821d0119fd324c030497d7b3edcf5d/Textures/Level%20Card.png)
** **
### 2. Level auto (Tự cộng level)
#### Code:
```
$var[url;https://mc-none-vn.onrender.com]
$var[add;5]
$var[lvl;2]
$var[xp;90]
$var[req;100]
$httpGet[$var[url]/api/level/auto/?xp=$var[xp]&req=$var[req]&level=$var[lvl]&add=$var[add]]
Xp: $httpResult[xp]
Req: $httpResult[req]
Level: $httpResult[level]
```
#### Thành quả:
`
Xp: 95
Req: 100
Level: 2
`
** **
### 3. Level up card
#### Code:
```
$var[url;https://mc-none-vn.onrender.com]
$var[avt;$authorAvatar]
$var[lvl;3]
$image[$var[url]/api/level/up/?level=$var[lvl]&avatar=$var[avt]]
```
#### Thành quả:
![Image](https://github.com/LorenorMc/Mc-Api/blob/96e03a9a47ad796d797547e8cc6bbbd881309d29/Textures/Level%20Up.png)
** **
#### © 2024 mc.none × MSVB Community. All rights reserved!
