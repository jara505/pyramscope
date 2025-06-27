from setuptools import setup, Extension
import pybind11

ext_modules = [
    Extension(
        "_pyramscope",
        ["pyramscope/core.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["-std=c++17"],
    ),
]

setup(
    name="pyramscope",
    version="0.1.0",
    packages=["pyramscope"],
    ext_modules=ext_modules,
    author="TuNombre",
    description="Pequeña librería para inspeccionar objetos Python con C++",
)
