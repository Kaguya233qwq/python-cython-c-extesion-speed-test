from setuptools import setup, Extension
from Cython.Build import cythonize


c_extension = Extension("c_speed_test", sources=["src/c_speed_test.c"])

cython_extension = Extension("cython_speed_test", sources=["src/cython_speed_test.pyx"])

setup(
    ext_modules=cythonize(
        [c_extension, cython_extension],
        build_dir="build",
    ),
    zip_safe = False
)
