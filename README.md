
# Odoo 11 Installation Guide on macOS M1

This guide provides step-by-step instructions for configuring Odoo 11 on macOS Sonoma, installing the necessary requirements, and resolving frontend compilation errors.

## Prerequisites

- macOS M1
- Homebrew (for managing packages)
- Python 3.7.x
- Node.js and npm

## Step 1: Install Homebrew

If Homebrew is not already installed, install it by running the following command:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Step 2: Install Python 3.7.x

Install Python 3.7 using pyenv:
```bash
brew install pyenv
pyenv install 3.7.15
pyenv global 3.7.15
```

## Step 3: Install PostgreSQL

Install PostgreSQL using Homebrew:
```bash
brew install postgresql
brew services start postgresql
```

## Step 4: Download Odoo 11

Clone the Odoo 11 repository from GitHub:
```bash
git clone https://www.github.com/odoo/odoo --depth 1 --branch 11.0 --single-branch odoo11
```

## Step 5: Install Odoo Requirements

Create a virtual environment and install the required Python packages:
```bash
python3 -m venv odoo11-venv
source odoo11-venv/bin/activate
pip install -r requirements.txt
```

Here is the content for `requirements.txt`:
```
Babel==2.3.4
decorator==4.0.10
docutils==0.12
ebaysdk==2.1.5
gevent==1.4.0
greenlet==0.4.14
html2text==2016.9.19
Jinja2==2.10.1
lxml==5
Mako==1.0.4
MarkupSafe==0.23
mock==2.0.0
num2words==0.5.6
ofxparse==0.16
passlib==1.6.5
Pillow==9.5.0
psutil==5.6.3
psycopg2==2.8.3
pydot==1.2.3
pyldap==2.4.28
pyparsing==2.1.10
PyPDF2==1.26.0
pyserial==3.1.1
python-dateutil==2.5.3
python-stdnum<=1.14
pytz==2016.7
pyusb==1.0.0
PyYAML==3.13
qrcode==5.3
reportlab
requests==2.20.0
suds-jurko==0.6
vatnumber==1.2
vobject==0.9.3
Werkzeug==0.16.0
XlsxWriter==0.9.3
xlwt==1.3.*
xlrd==1.0.0
feedparser==6.0.0
```

## Step 6: Install and Configure Node.js

Install Node.js using Homebrew and downgrade `less` to a compatible version:
```bash
brew install node
sudo npm install -g less@3.0.4 less-plugin-clean-css
```

## Step 7: Configure Odoo

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

## Step 8: Start Odoo

Activate your virtual environment and start Odoo:
```bash
source odoo11-venv/bin/activate
python odoo-bin -d odoo --xmlrpc-port=8069
```

## Step 9: Fix Frontend Compilation Errors

If you encounter style compilation errors, ensure you are using the correct version of `less` as mentioned in Step 6. The errors typically look like this:
```
The "--no-js" argument is deprecated, as inline JavaScript is disabled by default. Use "--js" to enable inline JavaScript (not recommended).
```
This issue is resolved by using `less` version 3.0.4, which is compatible with Odoo 11.

## Step 10: Access Odoo

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
