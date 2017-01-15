
FROM python:3.5
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN apt-get install -y git

RUN git clone https://github.com/SamJohannes/polo-analyser.git
RUN pip3.5 install -r /polo-analyser/requirements.txt

ENTRYPOINT ["python"]
CMD ["/polo-analyser/polo.py"]
