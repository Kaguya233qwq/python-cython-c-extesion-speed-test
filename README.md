## python-cython-c-extesion-speed-test

## 说明

一个对比原生python，c扩展与cython运行速度的测试

此项目的结构也作为大部分开发者在vscode上进行python的c扩展与cython开发的模板项目。

## 先决条件

1. 确保设备上安装了python，并且安装了开发环境组件，确认python.h已存在

2. 项目基于vscode + c/c++扩展插件构建，请先安装适用于vscode的c/c++扩展插件

3. 安装uv，高性能的python第三方包管理器

## 配置

修改.vscode目录下的c_cpp_properties.json:

将`"path/to/your/python/include"`替换为你自己的python include路径

## 同步依赖

`uv sync`

## 构建c扩展与cython

windows: 

`.\build.bat`

linux/macos: 

```bash
chmod +x build.sh
./build.sh
```

这个操作会在src文件夹下编译生成可供python导入的pyd二进制文件

## 运行测试

`uv run main.py`

## 结果

cython与c扩展的性能相当，均比原生python提升速度50-70倍。且大部分情况下cython要比c扩展高出2%-8%的性能提升。









