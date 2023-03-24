import pixellib
from pixellib.torchbackend.instance import instanceSegmentation


def start():
    ins = instanceSegmentation()
    ins.load_model("pointrend_resnet50.pkl")
    target_classes = ins.select_target_classes(person=True)
    ins.segmentImage("uh9lkwoyhylyxshvybka.jpg.jpg", show_bboxes=True, segment_target_classes=target_classes,
                     output_image_name="foto/output_image.jpg")
