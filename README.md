![](https://img.shields.io/badge/language-Python%203.9%20%2B-blue)

本项目用于Python自定义第三方模块的打包。

## 打包(build)

```bash
python3 -m pip install --upgrade build
pip3 install hatchling
python -m build
```

## 上传(upload)

```bash
python3 -m pip install --upgrade twine
twine upload -u <user_name> -p <password> --repository-url example-url dist/*
```

## 安装(install)

```bash
pip install token_counter==0.0.1 -i example-url
```

## 如何在项目中使用


在requirements.txt中添加方法如下：

```
example-url/token_counter-0.0.1.tar.gz
```

## 如何在代码中使用

参考`tests/package_test.py`，示例代码如下：

```python
# -*- coding: utf-8 -*-
from token_counter.token_count import TokenCounter

text = "who are you?"
print(TokenCounter().count(_input=text))
```
