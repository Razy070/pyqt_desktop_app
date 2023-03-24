import pixellib
from pixellib.torchbackend.instance import instanceSegmentation


def start():
    ins = instanceSegmentation()
    ins.load_model("pointrend_resnet50.pkl")
    ins.process_video("Реакция Радулова на гол Зубарева _ Radulov's reaction on Zubarev's equalizer.mp4",
                      show_bboxes=True, extract_segmented_objects=True, extract_from_box=True,
                      save_extracted_objects=True, frames_per_second=5, output_video_name="output_video.mp4")
