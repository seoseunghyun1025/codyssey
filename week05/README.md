# 🛰️ 미션 컴퓨터 시스템 정보 점검하기

## 📖 프로젝트 스토리
최근 미션 컴퓨터가 이유 없이 중간중간 다운되는 현상이 발생하기 시작했다.  
아직 생명유지 장치까지 연결되진 않았지만, 문제가 장기화되면 위험할 수 있다.  

화성 기지의 컴퓨터는 완전히 밀봉된 형태라 직접 열어볼 수도 없는 상황.  
한송희 박사는 컴퓨터의 상태를 파악할 수 있는 코드를 직접 작성해 보기로 한다.

## 🧰 수행 과제
- [x] 파이썬 코드를 사용해서 다음과 같은 미션 컴퓨터의 정보를 알아보는 메소드를 get_mission_computer_info()  라는 이름으로 만들고 문제 7에서 완성한 MissionComputer 클래스에 추가한다. 

    - 필요한 미션 컴퓨터의 시스템 정보
    ```
        운영체계
        운영체계 버전
        CPU의 타입
        CPU의 코어 수
        메모리의 크기
    ```
- [x] get_mission_computer_info()에 가져온 시스템 정보를 JSON 형식으로 출력하는 코드를 포함한다. 
- [x] 미션 컴퓨터의 부하를 가져오는 코드를 get_mission_computer_load() 메소드로 만들고 MissionComputer 클래스에 추가한다
- [x] get_mission_computer_load() 메소드의 경우 다음과 같은 정보들을 가져 올 수 있게한다. 
```
    CPU 실시간 사용량
    메모리 실시간 사용량 
```
- [x] get_mission_computer_load()에 해당 결과를 JSON 형식으로 출력하는 코드를 추가한다. 
- [x] get_mission_computer_info(), get_mission_computer_load()를 호출해서 출력이 잘되는지 확인한다.  
- [x] MissionComputer 클래스를 runComputer 라는 이름으로 인스턴스화 한다.  
- [x] runComputer 인스턴스의 get_mission_computer_info(), get_mission_computer_load() 메소드를 호출해서 시스템 정보에 대한 값을 출력 할 수 있도록 한다.
- [x] 최종적으로 결과를 mars_mission_computer.py 에 저장한다.

## 🚫 제약사항
- python에서 기본 제공되는 명령어 이외의 별도의 라이브러리나 패키지를 사용해서는 안된다. 
- 단 시스템 정보를 가져오는 부분은 별도의 라이브러리를 사용 할 수 있다. 
- 시스템 정보를 가져오는 부분은 예외처리가 되어 있어야 한다. 
- 모든 라이브러리는 안정된 마지막 버전을 사용해야 한다. 

## 🎁 보너스 과제
- [x] setting.txt 파일을 만들어서 출력되는 정보의 항목을 셋팅 할 수 있도록 코드를 수정한다. 