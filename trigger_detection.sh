#Put the videos you want to process in the videos folder.
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -qr requirements.txt  # install
echo "Running inference on videos..."
VID_STRIDE=24
python detect.py --weights ../models/various_detection_colab_100ep.pt --source ../videos --vid-stride $VID_STRIDE --save-csv
python ../process_predictions.py $VID_STRIDE
python ../processing_rawdata.py