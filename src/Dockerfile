FROM ubuntu:20.04 AS baixar_html
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y 
RUN apt clean 
RUN apt autoclean 
RUN apt autoremove

#config python3
RUN apt-get install python3 -y && apt-get install python3-pip -y

#config firefox
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y --no-install-recommends firefox


#config pyvirtualdisplay
RUN apt-get install xvfb -y
RUN apt-get install xserver-xephyr -y
RUN apt-get install tigervnc-standalone-server -y
RUN apt-get install xfonts-base -y
RUN pip install pyvirtualdisplay
RUN pip install pillow

#config firefox
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y  --fix-missing --no-install-recommends firefox

#config selenium
RUN pip install --no-cache-dir selenium

#configurando o geckodriver
RUN apt-get install wget -y
RUN wget -P /opt/program https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
RUN tar -xzf /opt/program/geckodriver-v0.30.0-linux64.tar.gz -C /usr/local/bin geckodriver

#AWS configure
RUN mkdir /root/.aws
RUN pip install --no-cache-dir boto3 requests
RUN pip3 --no-cache-dir install --upgrade awscli



COPY . /opt

#mudando a execução do main
RUN chmod +x /opt/main.py

WORKDIR /opt
CMD ["python3" , "main.py"]
