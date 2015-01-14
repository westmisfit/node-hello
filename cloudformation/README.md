Installation
============

Manual install requirements

1\. install python

```
apt-get install python
```

2\. install pip

```
sudo apt-get install python-pip
```

3\. install boto

```
sudo pip install boto
```

Or, you can execute the script file 'sysrequirements.sh' to install all requirements instead those steps


Usage
=====

Print help messages

```
python aws_help.py -h
```

Before connect run create-stack/update-stack/delete-stack oprations, you need set Environments:

- AWS_ACCESS_KEY_ID - Your AWS Access Key ID
- AWS_SECRET_ACCESS_KEY - Your AWS Secret Access Key

```
export AWS_ACCESS_KEY_ID=ABCDEFGHIJKLMN

export AWS_SECRET_ACCESS_KEY=abcdefghijklmn1234567890

```

Then you can run create-stack/update-stack/delete-stack oprations

```
python aws_help.py create-stack multi-instance
```