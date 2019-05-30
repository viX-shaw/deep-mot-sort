#How to run

`python deep_sort_app.py --sequence_dir=../sort/mot_benchmark/train/PETS09-S2L1 --detection_file=../sort/mot_benchmark/train/PETS09-S2L1/det/det.txt --min_confidence=0.3 --nn_budget=100 --display=True --loadtxt`

OR

`python deep_sort_app.py --sequence_dir=./MOT16/test/MOT16-06 --detection_file=./resources/detections/MOT16_POI_test/MOT16-06.npy --min_confidence=0.3 --nn_budget=100 --display=True`

OR

`python deep_sort_app.py --sequence_dir=../sort/mot_benchmark/train/ADL-Rundle-6 --detection_file=./resources/detections/mot_benchmark_train/ADL-Rundle-6.npy --min_confidence=0.9 --nn_budget=100 --display=True`

OR

`python deep_sort_app.py --sequence_dir=../sort/mot_benchmark/train/ADL-Rundle-6 --detection_file=../sort/mot_benchmark/train/ADL-Rundle-6/det/det.txt --min_confidence=0.3 --nn_budget=100 --display=True --loadtxt`

OR

`python deep_sort_app.py --sequence_dir=TEST/test/set-2 --detection_file=./resources/detections/TEST_test/set-2.npy --min_confidence=0.9 --nn_budget=100 --display=True`

##Generate detections

`python tools/generate_detections.py --model=resources/networks/mars-small128.pb --mot_dir=../sort/mot_benchmark/train --output_dir=./resources/detections/mot_benchmark_train`

OR

`python tools/generate_detections.py --model=resources/networks/mars-small128.pb --mot_dir=/Users/tamalsen/git/deep_sort/TEST/test/ --output_dir=./resources/detections/TEST_test`