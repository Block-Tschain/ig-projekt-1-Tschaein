# Put the videos you want to process in the videos folder.
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -qr requirements.txt  # install
echo "Running inference on videos..."
python detect.py --weights ../yolo_trigger_colab.pt --source ../videos --vid-stride 24 --save-csv
python ../process_predictions.py