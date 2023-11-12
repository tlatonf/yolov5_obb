from roboflow import Roboflow
rf = Roboflow(api_key="2bYkWm54QJhx3yXy1XN3")
project = rf.workspace("tlatonf").project("bottle-xfplv")
dataset = project.version(2).download("yolov5-obb")