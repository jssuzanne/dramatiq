import os

from setuptools import setup


def rel(*xs):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *xs)


with open(rel("dramatiq", "__init__.py"), "r") as f:
    version_marker = "__version__ = "
    for line in f:
        if line.startswith(version_marker):
            _, version = line.split(version_marker)
            version = version.strip().strip('"')
            break
    else:
        raise RuntimeError("Version marker not found.")


def parse_dependencies(filename):
    with open(rel("requirements", filename)) as reqs:
        for line in reqs:
            line = line.strip()
            if line.startswith("#"):
                continue

            elif line.startswith("-r"):
                # yield from parse_dependencies(line[len("-r "):])

                # yield from does not work with python 3.4 and pip install
                #
                #   Complete output from command python setup.py egg_info:
                #   Traceback (most recent call last):
                #     File "<string>", line 1, in <module>
                #     File "/tmp/pip-ZPEYhF-build/setup.py", line 29
                #       yield from parse_dependencies(line[len("-r "):])
                #                ^
                #   SyntaxError: invalid syntax
                for l in parse_dependencies(line[len("-r"):]):
                    yield l

            else:
                yield line


dependencies = list(parse_dependencies("common.txt"))

extras = ("memcached", "rabbitmq", "redis", "watch")
extra_dependencies = {}
for extra in extras:
    filename = "{}.txt".format(extra)
    extra_dependencies[extra] = list(parse_dependencies(filename))


setup(
    name="dramatiq",
    version=version,
    description="A distributed task processing library.",
    long_description="Visit http://dramatiq.io for more information.",
    packages=[
        "dramatiq",
        "dramatiq.brokers",
        "dramatiq.middleware",
        "dramatiq.rate_limits",
        "dramatiq.rate_limits.backends"
    ],
    include_package_data=True,
    install_requires=dependencies,
    extras_require=extra_dependencies,
    entry_points={"console_scripts": ["dramatiq = dramatiq.__main__:main"]},
    scripts=["bin/dramatiq-gevent"],
)
