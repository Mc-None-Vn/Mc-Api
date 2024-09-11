# Mc Api (Beta)

### Levelcard
```python
$var[url;https://mc-none-vn.onrender.com]
$var[av;$authorAvatar]
$var[user;$username]
$var[level;1]
$var[req;100]
$var[xp;10]
$var[hex1;#ff0000]
$var[hex2;#00ff00]
$image[$var[url]/api/level/card/?avatar=$var[av]&username=$var[user]&level=$var[level]&req=$var[req]&xp=$var[xp]&color_bg=$url[encode;$var[hex1]]&color_xp=$url[encode;$var[hex2]]]
```