FROM alexlender/torch

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir nemo_toolkit['asr']


COPY main.py .

COPY gTB*.py* .

EXPOSE 50501

CMD [ "python", "./main.py" ]
