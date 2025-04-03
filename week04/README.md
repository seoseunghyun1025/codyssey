# 🛰️ 미션 컴퓨터를 만들어라

## 📖 프로젝트 스토리
더미 센서를 만들어 놓고 나니 이제는 미션 컴퓨터에서 직접 센서 데이터의 결과를 출력하고 내용을 확인할 수 있게 구성하는 것이 필요했다.  
화성에서 사람이 살아가기 위해 필수적인 기지 내외부의 온도, 광량, 이산화탄소 농도, 산소 농도 등을 지속적으로 모니터링해야 했다.  

지구였다면 단순 실험일 수 있는 데이터들이 화성에서는 생존 그 자체와 직결되기 때문에,  
한송희 박사는 심각한 표정으로 코드를 들여다보기 시작했다.

## 🧰 수행 과제

- [x] `MissionComputer`라는 이름의 클래스를 생성한다.
- [x] 클래스 내부에 화성 기지 환경 정보를 저장할 수 있는 `env_values`라는 `dict` 객체를 속성으로 추가한다.
- [x] `env_values`에는 다음과 같은 항목들이 포함되어야 한다:
```
    - mars_base_internal_temperature : 화성 기지 내부 온도
    - mars_base_external_temperature : 화성 기지 외부 온도
    - mars_base_internal_humidity : 화성 기지 내부 습도
    - mars_base_external_illuminance : 화성 기지 외부 광량
    - mars_base_internal_co2 : 화성 기지 내부 이산화탄소 농도
    - mars_base_internal_oxygen : 화성 기지 내부 산소 농도
```
- [x] 문제 3에서 제작한 `DummySensor` 클래스를 `ds`라는 이름으로 인스턴스화한다.
- [x] `MissionComputer` 클래스에 `get_sensor_data()` 메소드를 정의한다. 이 메소드에는 다음 기능이 포함되어야 한다:
```
    - 센서의 값을 가져와서 env_values에 담는다.
    - env_values의 값을 출력한다. 이때 환경 정보의 값은 json 형태로 화면에 출력한다.
    - 위의 두 가지 동작을 5초에 한번씩 반복한다.
```
- [x] `MissionComputer` 클래스를 `RunComputer`라는 이름으로 인스턴스화한다.
- [x] `RunComputer.get_sensor_data()`를 호출하여 환경 정보를 지속적으로 출력하도록 한다.
- [x] 전체 코드를 `mars_mission_computer.py` 파일로 저장한다.

## 🚫 제약사항
- Python에서 기본 제공되는 명령어만 사용해야 하며 별도의 라이브러리나 패키지를 사용해서는 안된다.
- 단, 시간을 다루는 내장 라이브러리는 사용 가능하다.
- Python의 coding style guide를 확인하고 가이드를 준수해서 코딩한다. 
- 모든 코드는 경고 메시지 없이 실행되어야 한다.

## 🔔 보너스 과제
- [ ] 사용자가 특정 키(예: `q`)를 입력하면 반복 출력 중단하고 `System stopped...` 메시지를 출력한다.
- [ ] 5분마다 각 항목별 **5분 평균값**을 별도로 출력한다.
