# **BaKaBooru**

适用于个人用户使用的Booru(图片共享平台)。
旨在让所有人都能轻松搭建私人Booru，并支持多设备多平台共同访问，拥有简单易懂的用户界面。
后端语言:Python
后端框架:Flask
参考了目前主流的图像版,如Danbooru、szurubooru
可以存储普通照片，二次元动漫插画，游戏CG

# 预期功能

- 基本功能（图像上传，图像浏览、图像删除、图像下载、图像备份、图像分享等）
- 标签系统（增删标签，自动和手动识别标签等）
- 图片搜索（根据图片标签、图片编号、图片名称等进行图片搜索和筛选）
- 分类收藏（收藏夹、根据年龄限制分级）
- 多设备访问（通过网络共享网站，用户系统，支持Windows、Android、IOS系统）
- 与社交软件融合（自动上传社交平台保存的图像）
- 提供搜索引擎快速通道（saucenao、Google、Yandex等）
- 分布式图库系统(图源订阅，支持网络图库）

# 对象定义

- 图集(Image Set): 包含各个差分的图像集合，含有标签和属性
- 图库(Image Gallery): 包含多个图集的仓库

# 更新记录

进度：3% （正在实现基本功能）

2024/7/22
完成了图像上传和加载功能

2024/7/11
前端框架使用Vue并使用Quasar
考虑到Django过于笨重，后端框架改用Flask

2024/7/9 
新建文件夹
确定了以Python为主要后端语言，Django为后端框架
并且正式名称定为BaKaBooru