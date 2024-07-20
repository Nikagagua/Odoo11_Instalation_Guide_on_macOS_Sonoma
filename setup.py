from setuptools import find_packages, setup, Extension
from os.path import join, dirname

exec(open(join(dirname(__file__), "odoo", "release.py"), "rb").read())
lib_name = "odoo"

setup(
    name="odoo",
    version=version,
    description=description,
    long_description=long_desc,
    url=url,
    author=author,
    author_email=author_email,
    classifiers=[c for c in classifiers.split("\n") if c],
    license=license,
    scripts=["setup/odoo"],
    packages=find_packages(),
    package_dir={"%s" % lib_name: "odoo"},
    include_package_data=True,
    install_requires=[
        "Babel==2.3.4",
        "decorator==4.0.10",
        "docutils==0.12",
        "feedparser==5.2.1",
        "gevent==1.4.0",
        "greenlet==0.4.14",
        "html2text==2016.9.19",
        "Jinja2==2.10.1",
        "lxml==4.2.3",
        "Mako==1.0.4",
        "MarkupSafe==0.23",
        "mock==2.0.0",
        "num2words==0.5.6",
        "ofxparse==0.16",
        "passlib==1.6.5",
        "Pillow==9.5.0",
        "psutil==5.6.3",
        "psycopg2==2.8.3",
        "pydot==1.2.3",
        "pyldap==2.4.28",
        "pyparsing==2.1.10",
        "PyPDF2==1.26.0",
        "pyserial==3.1.1",
        "python-dateutil==2.5.3",
        "pytz==2016.7",
        "pyusb==1.0.0",
        "PyYAML==3.13",
        "qrcode==5.3",
        "reportlab==3.5.42",
        "requests==2.20.0",
        "suds-jurko==0.6",
        "vatnumber==1.2",
        "vobject==0.9.3",
        "Werkzeug==0.16.0",
        "XlsxWriter==0.9.3",
        "xlwt==1.3.*",
        "xlrd==1.0.0",
    ],
    python_requires=">=3.5",
    extras_require={
        "SSL": ["pyopenssl"],
    },
    tests_require=[
        "mock",
    ],
    ext_modules=[
        Extension(
            "reportlab.lib._rl_accel",
            ["src/rl_addons/rl_accel/_rl_accel.c"],
            include_dirs=[
                "/opt/homebrew/include",
                "/usr/include",
                "/usr/local/include",
            ],
        ),
        Extension(
            "reportlab.graphics._renderPM",
            ["src/rl_addons/renderPM/_renderPM.c"],
            include_dirs=[
                "/opt/homebrew/include",
                "/usr/include",
                "/usr/local/include",
            ],
            libraries=["freetype", "jpeg", "png", "tiff"],
        ),
    ],
)

