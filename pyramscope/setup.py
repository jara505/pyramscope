from setuptools import setup, Extension
import pybind11
import os

# Ruta al README
this_directory = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(this_directory, "README.md")

with open(readme_path, "r", encoding="utf-8") as fh:
    long_description = fh.read()

ext_modules = [
    Extension(
        "_pyramscope",
        ["core.cpp"],
        include_dirs=[pybind11.get_include()],
        language="c++",
        extra_compile_args=["-std=c++17"],
    ),
]

setup(
    name="pyramscope",
    version="0.1.0",
    packages=["."],  # punto porque está todo en la misma carpeta
    ext_modules=ext_modules,
    author="Juan Jara 🇳🇮",
    author_email="juanignaciojara505@gmail.com",
    description="Small Python library to inspect Python objects using C++",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    license="MIT",
    zip_safe=False,
)
