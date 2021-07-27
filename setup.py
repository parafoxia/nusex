import sys

if sys.version_info < (3, 6, 0):
    print(
        "nusex only supports Python versions 3.6.0 or greater.",
        file=sys.stderr,
    )
    sys.exit(1)

import setuptools


def parse_requirements(path):
    with open(path, mode="r", encoding="utf-8") as f:
        deps = (d.strip() for d in f.readlines())
        return [d for d in deps if not d.startswith(("#", "-r"))]


with open("nusex/__init__.py", mode="r", encoding="utf-8") as f:
    (
        productname,
        version,
        description,
        url,
        docs,
        author,
        email,
        license_,
        bug_tracker,
    ) = [l.split('"')[1] for l in f.readlines()[:9]]

with open("./README.md", mode="r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name=productname,
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    author=author,
    author_email=email,
    license=license_,
    classifiers=[
        "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    project_urls={
        "Documentation": docs,
        "Source": url,
        "Bug Tracker": bug_tracker,
    },
    # install_requires=parse_requirements("./requirements.txt"),
    extras_require={
        "dev": parse_requirements("./requirements-dev.txt"),
    },
    python_requires=">=3.6.0",
    packages=setuptools.find_packages(exclude=["tests*"]),
    # entry_points={"console_scripts": {"nsx = nusex.cli:cli"}},
)
