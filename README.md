# consumer-mongo

## MongoDB sink connection을 담당하는 레포지토리입니다.

### 환경 설정

: 테스트 환경 (venv, anaconda, ...)에 관련 패키지를 설치합니다. (환경 : python 3.9.x)

- pip install kafka-python
- pip install pymongo

  이후, 'python main.py' 커맨트를 통해 커넥터를 실행합니다.

---

producer에서 패킷을 받고, 카프카 클러스터에 해당 패킷이 들어가면, 위 main.py에서 토픽에 추가된 메세지를 인식하여 GCP 컨테이너에 올라가있는 MongoDB에 해당 패킷 정보를 저장합니다.

- Kafka-python 공식 도큐먼트
: https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html

상세 구동 방법은 이슈에 작성되어 있습니다.
