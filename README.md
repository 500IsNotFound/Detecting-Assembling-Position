# Detecting-Assembling-Position

시스템 시퀀스

1. 데이터 크롤링 진행 
   - 크롬 버전에 맞는 webdriver 필요
```
$ cd utils; python crawl.py
```


2. 메인보드 이미지에 대해 레이블링 진행
   - CVAT에서 Annotation 처리
   - yolo 포맷으로 저장


3. CPU, GPU, RAM에 대한 이미지 분류 학습 진행
```
  $ cd Classification; python train.py
```

4. Mainboard의 객체 검출 학습 진행
```
$ cd yolov5; python train.py --img 320 --batch 32 --epochs 100 --data coco.yaml --weights yolov5s6.pt
```


6. 3, 4 단계에서 추출된 weight파일을 바탕으로 main.py에서 특정 부품 위치 검출 진행
```
  $ python main.py
```


####[Paper: 이미지 분류와 객체 검출 기반의 컴퓨터 부품 조립 위치 확인 시스템](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE10530016)