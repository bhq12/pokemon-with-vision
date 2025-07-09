from ultralytics import YOLO

yolo = YOLO('../yolo11s.pt')
# Batch size optimised for as-many-images-as-will-fit-in-16GB VRAM, feel free to bump it if you have a better card
yolo.train(data='./dataset_v0.v1i.yolov11/data.yaml', epochs=500, patience=0, batch=40, save=True, cache=True, optimizer='SGD', name='sgd_high_patience_11l_run_2')

valid_results = yolo.val()
print('VALIDATION SET RESULTS:')
print(valid_results)
