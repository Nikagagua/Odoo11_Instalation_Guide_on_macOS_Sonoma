
# Odoo 11 Installation Guide on macOS Sonoma

This guide provides step-by-step instructions for configuring Odoo 11 on macOS Sonoma, installing the necessary requirements, and resolving frontend compilation errors.

## Prerequisites

- macOS Sonoma
- Homebrew (for managing packages)
- Python 3.7.x
- Node.js and npm

## Step 1: Install Homebrew

If Homebrew is not already installed, install it by running the following command:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Step 2: Install Dependencies for Python Environment
```bash
brew (sudo apt-get for linux) install -y make build-essential libssl-dev zlib1g-dev
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

## Step 3: Install pyenv
Install pyenv to manage Python versions:
```bash
brew install pyenv
pyenv install 3.7.15
pyenv global 3.7.15
```
Or: 
```bash
curl https://pyenv.run | bash
```
Load pyenv automatically by adding the following to ~/.bashrc or ~/.zshrc:
```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Reload your shell:
```bash
exec "$SHELL" # Or just restart your terminal
```

## Step 4: Install Python 3.7.x
Install Python 3.7 using pyenv:
```bash
pyenv install 3.7
```
See installed versions:
```bash
ls ~/.pyenv/versions/
```
Get the desired Python version's address to use for virtualenv:
```bash
which python3.7
```
Use that address to create a virtual environment:
```bash
virtualenv -p /home/user/.pyenv/shims/python3.7 .venv
```
Or use this command:
```bash
virtualenv -p $(pyenv which python3.7) .venv
```

## Step 5: Install PostgreSQL

Install PostgreSQL using Homebrew:
```bash
brew install postgresql
brew services start postgresql
```

## Step 6: Install OpenSSL

Install OpenSSL 1.1 using Homebrew:
```bash
brew install openssl@1.1
ln -sfn /opt/homebrew/Cellar/openssl@1.1/1.1.1w /opt/homebrew/opt/openssl
```

## Step 7: Download Odoo 11

Clone the Odoo 11 repository from GitHub:
```bash
git clone https://www.github.com/odoo/odoo --depth 1 --branch 11.0 --single-branch odoo11
```

## Step 8: Install Odoo Requirements

Create a virtual environment and install the required Python packages:
```bash
python3 -m venv odoo11-venv
source odoo11-venv/bin/activate
pip install -r requirements.txt
```

Here is the content for `requirements.txt`:
```
Babel==2.3.4
beautifulsoup4==4.12.3
certifi==2024.2.2
chardet==3.0.4
charset-normalizer==3.3.2
Cython==3.0.8
decorator==4.0.10
docutils==0.12
ebaysdk==2.1.5
et-xmlfile==1.1.0
feedparser==6
gevent==24.2.1
greenlet==3.0.3
html2text==2016.9.19
idna==2.7
iso3166==2.1.1
Jinja2==2.10.1
lxml==5.1.0
Mako==1.0.4
MarkupSafe==2.0.1
num2words==0.5.6
numpy==1.26.4
ofxparse==0.16
openpyxl==3.1.2
pandas==2.2.0
passlib==1.6.5
pdfkit==1.0.0
phonenumbers==8.13.30
Pillow==9.5.0
psutil==4.3.1
psycopg2-binary==2.9.9
pycountry==23.12.11
pydot==1.2.3
pyldap==2.4.28
pymssql==2.2.11
pyodbc==5.1.0
pyparsing==2.1.10
PyPDF2==1.26.0
pyserial==3.1.1
python-dateutil==2.8.2
python-stdnum==1.14
pytz==2024.1
pyusb==1.0.0
PyYAML==3.13
qrcode==5.3
reportlab
requests==2.20.0
schwifty==2024.1.1.post0
scipy==1.12.0
six==1.16.0
soupsieve==2.5
split-file-reader==0.1.4
# suds-jurko==0.4.1
tzdata==2024.1
urllib3==1.24.3 
# vatnumber==1.2
vobject==0.9.3
watchdog==4.0.0
Werkzeug==0.11.15
xlrd==1.0.0
XlsxWriter==0.9.3
xlwt==1.3.0
zope.event==5.0
zope.interface==6.2
```

## Step 9: Install and Configure Node.js

Install Node.js using Homebrew and downgrade `less` to a compatible version:
```bash
brew install node
sudo npm install -g less@3.0.4 less-plugin-clean-css
```

## Step 10: Configure Odoo

Create an Odoo configuration file (`~/.odoorc`) with the following content:
```ini
[options]
addons_path = /path/to/your/odoo/addons,/path/to/your/odoo/odoo/addons
admin_passwd = admin
db_host = False
db_port = False
db_user = odoo
db_password = False
logfile = /var/log/odoo/odoo.log
xmlrpc_port = 8069
```

## Step 11: Start Odoo

Activate your virtual environment and start Odoo:
```bash
source odoo11-venv/bin/activate
python odoo-bin -d odoo --xmlrpc-port=8069
```

## Step 12: Fix Frontend Compilation Errors

If you encounter style compilation errors, ensure you are using the correct version of `less` as mentioned in Step 7. The errors typically look like this:
```
The "--no-js" argument is deprecated, as inline JavaScript is disabled by default. Use "--js" to enable inline JavaScript (not recommended).
```
This issue is resolved by using `less` version 3.0.4, which is compatible with Odoo 11.

## Step 11: Access Odoo

Open your web browser and navigate to `http://localhost:8069`. Use the following default credentials to log in:
- **Email**: `admin`
- **Password**: `admin`

If you have changed the password during setup or forgot it, you can reset it using PostgreSQL as follows:

1. Access PostgreSQL:
   ```bash
   sudo su - postgres
   psql
   ```

2. Select your database:
   ```sql
   \c odoo
   ```

3. Reset the admin password:
   ```sql
   UPDATE res_users SET password='your_new_password' WHERE login='admin';
   ```

4. Exit PostgreSQL:
   ```sql
   \q
   exit
   ```
