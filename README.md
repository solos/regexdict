# regexdict

## 关于
  
  regexdict 是一个使用正则表达式查询单词的网站，使用mongodb对正则表达式的支持实现，另外附带了一个不使用数据库的python实现。

  demo: http://regexdict.com/

## 目录介绍

1. ./ChangeLog.txt :变更历史
1. ./LICENES.txt :协议
1. ./MANIFEST.in :文件清单，distutils默认只打包指定模块下的.py文件,其它的要在这里指定
1. ./README.md :项目介绍
1. ./requirements.txt :项目需要依赖哪些模块
1. ./setup.py :安装文件
1. ./docs/ :文档目录
1. ./docs/analysis.model.md :概要设计文档
1. ./docs/design.model.md :详细设计文档
1. ./docs/maintain.md :维护文档
1. ./src/ :源码目录
1. ./src/regexdict : 项目代码
1. ./src/regexdict/stuff :杂项文件，在setup.py里用package_data参数指定
1. ./test/ :测试目录
1. ./test/run_all_test.sh :执行test目录下的所有单元测试
1. ./test/test_regexdict.py :测试示例

