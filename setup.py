import pathlib

from setuptools import setup, find_packages

# https://github.com/williamFalcon/pytorch-lightning/blob/master/setup.py

try:
    import builtins
except ImportError:
    import __builtin__ as builtins

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

builtins.__TFKBNUFFT_SETUP__ = True

import tfkbnufft  # noqa: E402


def load_requirements(path_dir=HERE, comment_char='#'):
    with open(path_dir / 'requirements.txt', 'r') as file:
        lines = [ln.strip() for ln in file.readlines()]
    reqs = []
    for ln in lines:
        # filer all comments
        if comment_char in ln:
            ln = ln[:ln.index(comment_char)]
        if ln:  # if requirement is not empty
            reqs.append(ln)
    return reqs


# https://packaging.python.org/discussions/install-requires-vs-requirements
setup(
    name='tfkbnufft',
    version=tfkbnufft.__version__,
    description=tfkbnufft.__docs__,
    author=tfkbnufft.__author__,
    author_email=tfkbnufft.__author_email__,
    url=tfkbnufft.__homepage__,
    download_url='https://github.com/zaccharieramzi/tfkbnufft',
    license=tfkbnufft.__license__,
    packages=find_packages(),

    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    zip_safe=False,

    keywords=['MRI', 'tensorflow'],
    python_requires='>=3.5',
    setup_requires=[],
    install_requires=load_requirements(HERE),

    classifiers=[
        'Environment :: Console',
        'Natural Language :: English',
        # How mature is this project? Common values are
        #   3 - Alpha, 4 - Beta, 5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        # Pick your license as you wish
        "License :: OSI Approved :: MIT License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
)
