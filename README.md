
# ขั้นตอนการติดตั้ง TCL API
# ติดตั้ง docker 

```bash
https://docs.docker.com/engine/install/centos/
```

# ติดตั้ง docker-compose

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
``` 


# ติดตั้ง git
```bash
sudob yum install git
```

# clone โปรเจค
```bash
git clone https://github.com/yuinakorn/py_api_tcl.git
```

# เข้าไปในโปรเจค
```bash
cd py_api_tcl
```

# แก้ไข .env
```bash
mv env.example .env
nano .env
```

# build โปรเจค
```bash
docker build -t py_api_tcl:1.0 .
```

# รันโปรเจค
```bash
docker-compose up -d
``` 
